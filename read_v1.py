#!/usr/bin/env python3
# - Run in a py3 environment.
# No additional packages required, only using py standard lib.

__doc__ = """
This software takes UDP readouts from TAIT Stage Tech's eChameleon software, and translates it into useful things.
Originally written for the Guildhall School of Music and Drama by James Cooper, whilst studying on the BA Hons Technical Theatre Arts course.
"""


__author__ = "James Cooper"
__copyright__ = "Copyright 2019, James Cooper"
__credits__ = ["James Cooper"]
__license__ = "GNU GPLv3"
__version__ = "1"
__maintainer__ = "James Cooper"
__email__ = "james.cooper@stu.gsmd.ac.uk"
__status__ = "Development"


import socket
import struct

_debug_ = False


# These may be TAIT specific. But they're a good point to start from, use Wireshark to find out what settings you need here.
if not _debug_:
    UDP_IP = "172.16.1.255"
    UDP_PORT = 30501
    print(_debug_)
    print("hi")

if _debug_:
    UDP_IP = "172.16.1.255"
    UDP_PORT = 50365
    UDP_PORT = 50741
    print(_debug_)

# Generally, leave these, unless TAIT has changed their packet structure.
LENGTH_HEADER = 24 # How long is the header of each packet?
ATTR_PER_AXIS = 5 # How many attributes per axis?


## Class definitions
class Axis():
    def __init__(self, PLC, position, speed, timeleft, status):
        self.PLC = PLC
        self._position = position
        self._speed = speed
        self._timeleft = timeleft
        self.status = status
        

## Function definitions
def doAxisDataParsing(axisData):
    # Convert all axis attributes into one big array,
    # Come up with solution to mixing len(4) and len(8) attributes in struct
    return axisDataList


def parseAxisData(axisDataList, axis):
    # Use this function to create class objects. Then store classes in an array.
    # Make this similar to parsePacketHeaderData, tip. Use ">B", for interpreting the BYTE length values.
    # Feed this the axisDataList from doAxisDataParsing, so you specify which axis you want, then it will tell you it's data.
    # Make this go the other way in another function, to grab every fifth attribute from axisDataList, starting from StatusCode, to get each status, and search by status for each bar. Potentially look into making each Axis an Axis() object, make custom class.
    returnArray = []
    for attr in range(ATTR_PER_AXIS):
        returnArray.append(axisDataList[axis*ATTR_PER_AXIS+attr])
    return axis, returnArray


def parsePacketHeaderData(data):
    magicNumber = struct.unpack(">I",data[0:4])[0]
    packetID = struct.unpack(">I",data[4:8])[0]
    head1 = struct.unpack(">I",data[8:12])[0] # PLC Node Number
    head2 = struct.unpack(">I",data[12:16])[0] # Number of Axes driven from this PLC/ALM
    head3 = struct.unpack(">I",data[16:20])[0] # Null (these bytes return the value int(0))
    head4 = struct.unpack(">I",data[20:24])[0] # First axis on this PLC (this returns value '1' as integer)
    PacketHeader = {
    "magicNumber" : magicNumber,
    "packetID" : packetID,
    "head1" : head1,
    "head2" : head2, #Skip head3 because NULL
    "head4" : head4,    
    "axisData" : [], # Set up AxisData to allow us to iterate through and offset through all the attributes for the axes
    }
    return PacketHeader


def joinDataTables(TableList):
    MasterArray = []
    for DataTable in TableList:
        MasterArray.append(DataTable)
        

def breakdownThisAxis(axisData):
    thisAxis = [] #Set up Blank List for this axis
    thisAxis.append(struct.unpack(">I",axisData[0:4])[0]) #Append the first 4 bytes (Position to list)
    thisAxis.append(struct.unpack(">I",axisData[4:8])[0]) #Append speed to the second bit of thisAxis
    thisAxis.append(struct.unpack(">I",axisData[8:12])[0]) #Append Seconds Left
    thisAxis.append(struct.unpack(">b",axisData[12:13])[0]) #Append Status Code
    thisAxis.append(struct.unpack(">b",axisData[13:14])[0])
    return thisAxis
    

def inDataTable(AxisClassArray, addr, data):
    packet = {}
    packet["Packet Header"] = parsePacketHeader(data)
    NodeNo = Packet["Packet Header"]["head1"]
    Packet["axisData"] = data[24:]
    iteration = 0
    for axis in range(packet["PacketHeader"]["head2"]):
        AxisClassArray.append(Axis(breakdownThisAxis(Packet["AxisData"]), iteration))
        iteration += 1
    return AxisClassArray

def intoDataTable(addr,data):
# See below original code, but the IPI doesn't actually matter as we're already passed PLC Node Number in each packet.
   PacketHeader = parsePacketHeaderData(data)
   for axis in range(PacketHeader["head2"]):
    # If data is on Node 1
    if addr[0] == "172.16.1.51":
        pass
    if True: 
        print(addr[0])
        #Break down the header information for each packet
        dataTablePLC1 = parsePacketHeaderData(data)
        # Now only look at axisData section of the Packet
        axisData = data[24:]
        for axis in range(dataTablePLC1["head2"]): #Look up headData2 from the PacketHeader
            # Here you do the raw offset looping through the axes with the unpacking of the offset bits stuff.
            thisAxis = breakdownThisAxis(axisData)
            #dataTablePLC1["axisData"].append(thisAxis)
            axisData = axisData[14:]
            dataTablePLC1["axisData"].append(thisAxis)
        return "NODE1", dataTablePLC1
    # if on Node 2
    elif addr[0] == "172.16.1.52":
        print(addr[0])
        dataTablePLC2 = parsePacketHeaderData(data)
        axisData = data[24:]
        for axis in range(dataTablePLC2["head2"]):
            thisAxis = breakdownThisAxis(axisData)
            axisData = axisData[14:]
            dataTablePLC2["axisData"].append(thisAxis)
        return "NODE2", dataTablePLC2


def main():
    # Set up UDP receiving ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    # This is the main polling loop of the program, to get each and every UDP data packet.
    AxisClassArray=[]
    while 1:
        # Output the raw UDP data and src addr.
        data, addr = sock.recvfrom(2048)  # data = UDP stuff, addr is tuple, addr[0] = IP as str, addr[1] = Port as int

        # Call intoDataTable above
        NodeNo, NodeOutput = intoDataTable(addr,data)
        print("_______________________________",NodeOutput["head1"], NodeOutput["head2"], NodeOutput["head4"], NodeOutput["packetID"])
        for line in NodeOutput["axisData"]:
              print(line)

 #       if NodeNo == "NODE1" and NodeOutput["axisData"][0] == "14100":
  #          print("hi")
#            print(NodeNo, NodeOutput["axisData"])
#            print("\n".join(NodeOutput["axisData"]))

if __name__ == "__main__":
    main()

# EOF