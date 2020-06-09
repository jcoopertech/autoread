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
    pass
    UDP_IP = "0.0.0.0"
    UDP_PORT = 6061
    LENGTH_HEADER = 10
    axNoCh = \
    [[1, 1, 1],[1, 2, 22],[1, 3, 24],[1, 4, 26],
    [1, 5, 28],[1, 6, 30],[1, 7, 32],[1, 8, 35],
    [1, 9, 41],[1, 10, 42],[1, 11, 43],[1, 12, 44],
    [1, 13, 45],[1, 14, 46],[1, 15, 91],[1, 16, 92],
    [1, 17, 93],[2, 1, 1],[2, 2, 2],[2, 3, 5],
    [2, 4, 7],[2, 5, 9],[2, 6, 11],[2, 7, 13],
    [2, 8, 15],[2, 9, 17],[2, 10, 19],[2, 11, 21],
    [2, 12, 23],[2, 13, 25],[2, 14, 27],[2, 15, 29],
    [2, 16, 31],[2, 17, 33],[2, 18, 34],[2, 19, 3],
    [2, 20, 4],[2, 21, 6],[2, 22, 8],[2, 23, 10],
    [2, 24, 12],[2, 25, 14],[2, 26, 16],[2, 27, 18],
    [3, 1, 81],[3, 2, 82]]

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



def SimotionPacketHeader(data):
    magicNumber = struct.unpack(">I",data[0:4])[0]
    packetID = struct.unpack(">I",data[4:8])[0]
    head1 = struct.unpack(">I",data[8:12])[0] # Simotion
    head2 = struct.unpack(">I",data[12:16])[0] # Number of Axes driven from this Simotion CU
    head3 = struct.unpack(">I",data[16:20])[0] # Null (these bytes return the value int(0))
    head4 = struct.unpack(">I",data[20:24])[0] # First axis on this PLC (always 1)
    PacketHeader = {
    "magicNumber" : magicNumber,
    "packetID" : packetID,
    "head1" : head1,
    "head2" : head2, #Skip head3 because NULL
    "head4" : head4,
    "axisData" : [], # Stores list of all axes data
    }
    return PacketHeader


def breakdownSimotionAxis(axisData):
    thisAxis = [] #Set up Blank List for this axis
    # Append Position, Speed, Time Left, Status to thisAxis (local)
    thisAxis.append(struct.unpack(">I",axisData[0:4])[0]) # Position
    thisAxis.append(struct.unpack(">I",axisData[4:8])[0]) # Speed
    thisAxis.append(struct.unpack(">I",axisData[8:12])[0]) # Time Left
    thisAxis.append(struct.unpack(">b",axisData[12:13])[0]) # Status
    thisAxis.append(struct.unpack(">b",axisData[13:14])[0])
    return thisAxis

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
    """When using Tkinter, this code should be called by the
    'after' method. Our system sends packets every 50ms per node."""
    # Output the raw UDP data and src addr.
    AllUpdated = False
    ExitCond = False
    while ExitCond == False:
        data, addr = sock.recvfrom(2048)  # data = UDP stuff, addr is tuple, addr[0] = IP as str, addr[1] = Port as int
        print(data)
        NodeOutput = intoKinesysDataTable(addr,data)
        AxisArray = sortAxisData_Table(Data_Table)
        if NodeOutput["head1"] == 1:
            Node1Get = True
            COM_CONFIG.Nodes[0]["recv"] = True
        if NodeOutput["head1"] == 2:
            Node2Get = True
            COM_CONFIG.Nodes[1]["recv"] = True
#        if Node1Get == True and Node2Get == True:
#            AllUpdated = True
        for Node in COM_CONFIG.Nodes:
            if Node["recv"] == True:
                NodesHeardFrom.append(Node)
    AxisDict = convertAxisArraytoDictionary(AxisArray) # Now we can query an Axis Number and get info as tuple.
    return AxisDict


if __name__ == "__main__":
    print(read_main())
