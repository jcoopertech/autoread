#!/usr/bin/env python3
# - Run in a py3 environment.
# No additional packages required, only using py standard lib.

import COM_CONFIG
import socket
import struct

_debug_ = True


# Set up instance, this is possibly unique to our environment.
"""

This is EXCLUSIVELY AR_read but for Kinesys axes.
The main differences between Kinesys and Simotion are:
 - 1 data source outputs all axes per system - not multiple notes to merge.
 - there are 6 "axes" per Kinesys row/channel/motor.

 This is because a media server output item can affect 1 of 6 axes for other
 places to interpret. Similar to PSN.

"""

class KinesysAxis():
    def __init__(self):
        self.X = thisAxis[0]
        self.Y = thisAxis[1]
        self.Z = thisAxis[2]
        self.Pitch = thisAxis[3]
        self.Tilt = thisAxis[4]
        self.Rotate = thisAxis[5]

class KinesysAxisPart():
    def __init__(self, thisAxis):
        self.ID = thisAxis[0]
        self.Position = thisAxis[1]
        self.Speed = thisAxis[2]
        self.Error = thisAxis[3]


if _debug_:
    UDP_IP = "0.0.0.0"
    UDP_PORT = 6061
    LENGTH_HEADER = 10


Data_Table = {}

def KinesysPacketHeader(data):
    KNET = struct.unpack(">ssssssssssss",data[0:12])
    KNET_ID = "".join(str(KNET_part,'utf-8') for KNET_part in KNET)
    print(KNET_ID)
    opcode = struct.unpack(">h", data[12:14])[0]
    print(opcode)
    MinProtVer = struct.unpack(">h",data[16:18])[0]
    print(MinProtVer)
    FrameID = struct.unpack("<h", data[18:20])[0]
    print(FrameID)
    NumDataMsgs = struct.unpack(">b", data[20:21])[0]
    print(NumDataMsgs)
    PacketHeader = {
    "magicNumber" : KNET_ID,
    "packetID" : FrameID,
    "head1" : KNET_ID,
    "NumDataMsgs" : NumDataMsgs, #Skip head3 because NULL
    "axisData" : [], # Stores list of all axes data
    }
    return PacketHeader


def breakdownKinesysAxis(axisData):
    thisAxis = [] #Set up Blank List for this axis
    # Append Position, Speed, Time Left, Status to thisAxis (local)
    offset = 0
    for axis in axisData:
        thisAxis.append(struct.unpack(">H",axisData[offset+0:offset+2])[0]) # AxisID
        thisAxis.append(struct.unpack(">l",axisData[offset+2:offset+6])[0]) # Position signed
        thisAxis.append(struct.unpack(">H",axisData[offset+6:offset+8])[0]) # Speed
        thisAxis.append(struct.unpack(">H",axisData[offset+8:offset+10])[0]) # Errors
        offset += 10
    print(thisAxis)
    return thisAxis

def intoKinesysDataTable(addr,data):
# See below original code, but the IP doesn't actually matter as we're already passed PLC Node Number in each packet.
    PacketHeader = KinesysPacketHeader(data)
    print(PacketHeader)
#        print("packet header node no")
#        print(PacketHeader["head1"])
    #Break down the header information for each packet
    #dataTable = SimotionPacketHeader(data)
    dataTable = PacketHeader
    # Now only look at axisData section of the Packet
    axisData = data[LENGTH_HEADER:]
    axisCount = COM_CONFIG.FirstEChamAxis
    KSysClassStorage = []
    for axis in range(PacketHeader["NumDataMsgs"]): #Look up headData2 from the PacketHeader
        # Here you do the raw offset looping through the axes with the unpacking of the offset bits stuff.
        thisAxis = breakdownKinesysAxis(axisData)
        KSysClassStorage.append(KinesysAxis(thisAxis))
        axisData = axisData[10:]
        dataTable["axisData"].append(thisAxis)
        axisCount += 1
    return dataTable


def sortAxisData_Table(Data_Table):
    QuantifiedArray = []
    AxisMasterOrder = sorted(Data_Table, key = lambda x : int(x.split()[0]))
    for axis in AxisMasterOrder:
#        print("axis", axis)
#        print(Data_Table[axis])
        QuantifiedArray.append([axis,Data_Table[axis]])
    return QuantifiedArray


def convertAxisArraytoDictionary(AxisArray):
    AxDict = {}
    for item in AxisArray:
        AxDict[item[0]] = tuple(item[1])
    return AxDict


def read_main():
    # Set up UDP receiving ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    # This is the main polling loop of the program, to get each and every UDP data packet.
    Node1Get = False
    Node2Get = False
    # Output the raw UDP data and src addr.
    AllUpdated = False
    ExitCond = False
    while ExitCond == False:
        data, addr = sock.recvfrom(2048)  # data = UDP stuff, addr is tuple, addr[0] = IP as str, addr[1] = Port as int
        print(data)
        NodeOutput = intoKinesysDataTable(addr,data)
        AxisArray = sortAxisData_Table(Data_Table)
    AxisDict = convertAxisArraytoDictionary(AxisArray) # Now we can query an Axis Number and get info as tuple.
    return AxisDict


if __name__ == "__main__":
    print(read_main())
