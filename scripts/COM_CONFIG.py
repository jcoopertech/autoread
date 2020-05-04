
# AutoRead Configuration File default
"""
AUTOREAD CONFIG File

Author:     James Cooper
Contact:    james@jcooper.tech
Description:    Shared code for many parts of AutoRead.

This project was made for the Guildhall School of Music and Drama.
Developed with the Milton Court TAIT eChameleon Automation installation in mind.

"""


"""Leave these first sections alone :)"""
class LightType:
    def __init__(self, type_name, total_pan, total_tilt, yoke_offset):
        self.type_name = type_name
        self.total_pan = total_pan
        self.total_tilt = total_tilt
        self.yoke_offset = yoke_offset
    def print_me(self):
        print("type_name:\t\t", self.type_name)
        print("total_pan:\t\t", self.total_pan)
        print("total_tilt:\t\t", self.total_tilt)
        print("yoke_offset\t\t", self.yoke_offset)


def GenerateNewLightList():
    """You should use this function to generate a new light configuration.
    Note, adaptations will need to be made if you want to add more LightTypes."""
    Lights = []
    NumberToMake = int(input("How many lights would you like to have in the system?"))
    for UnitID in range(NumberToMake):
        ThisLightType = str(input("What type of light is this? (\"TW1\" or \"ETC_REV\")"))
        CentreOffset = int(input("What is it's X value, based on your origin?\n\t-\tNote: Anything Stage Right of 0 should be negative."))
        ThisItemAxis = int(input("What axis is the light on? Enter a number only."))
        Lights.append([ThisLightType,(CentreOffset, None, None), ThisItemAxis, UnitID+1])
    print("Lights = [{0}]".format(",\n".join([str(x) for x in Lights])))
    return Lights

"""AUTO READ CONFIG FILE - READ FROM HERE DOWN"""
"""
          _    _ _______ ____  _____  ______          _____
     /\  | |  | |__   __/ __ \|  __ \|  ____|   /\   |  __ \
    /  \ | |  | |  | | | |  | | |__) | |__     /  \  | |  | |
   / /\ \| |  | |  | | | |  | |  _  /|  __|   / /\ \ | |  | |
  / ____ \ |__| |  | | | |__| | | \ \| |____ / ____ \| |__| |
 /_/    \_\____/   |_|  \____/|_|  \_\______/_/    \_\_____/


"""
"""If this system is installed, with an automation network, set this to False"""
_offline_test_ = True
#_offline_test_ = False



"""AutoRead Track functions"""


"""Set Up GPIO LED Pins"""
LED_def = {"led1":16,"led2":18}


""" AutoRead (Read) Settings """
# The broadcast IP for your Simotion Automation input
UDP_IP = "172.16.1.255"
# Port being used for Simotion output
UDP_PORT = 30501
LENGTH_HEADER = 24 # How many bytes long is the head1..head4 section of the simotion packet.
ATTR_PER_AXIS = 5 # How many data points are being sent per axis? Important because of how we interpret the packet.

# Map your eCham Axis to the Node/Channel format.
# Format: Node,Channel,Axis
axisNodeChannels = [
[1, 1, 20],[1, 2, 22],[1, 3, 24],[1, 4, 26],
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

# This saves on computing time - if the starting axis in eCham is nowhere near 1
FirstEChamAxis = 1 #Default should be 1 though.

# Copy and paste this to make sure you have the right number of nodes in the system.
Node1 = {
"Name": "1A0",
"IP": "172.16.1.51",
"recv": False,
}

Node2 = {
"Name": "2A0",
"IP": "172.16.1.52",
"recv": False,
}

Nodes = [Node1,Node2]
NumberOfNodes = len(Nodes)


"""AutoRead (Track) Settings"""
# Define AxisYValues based on CAD plan
AxisYValues = [200,500,800,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,
3200,3400,3600,3800,4000,4200,4400,4600,4800,5000,5200,5400,5600,5800,6000,6200,
6400,6600,6800,7000]




# Update Axis status and Z value here - this is because we're not connected to Auto Network.
axisDict = {
1: (3871,0,0),
2: (10709,0,0),
3: (2550,0,0),
4: (5811,0,0),
5: (4108,0,0),
6: (3701,0,0),
7: (1549,0,0),
8: (6750,0,0),
9: (4127,0,0),
10: (6479,0,0),
11: (6214,0,0),
12: (7136,0,0),
13: (12364,0,0),
14: (3541,0,0),
15: (12606,0,0),
16: (3872,0,0),
17: (4360,0,0),
18: (12200,0,0),
19: (12768,0,0),
20: (2815,0,0),
21: (9137,0,0),
22: (10100,0,0),
23: (9172,0,0),
24: (7573,0,0),
25: (5697,0,0),
26: (13667,0,0),
27: (6386,0,0),
28: (5740,0,0),
29: (7080,0,0),
30: (13992,0,0),
31: (6000,0,0),
32: (3248,0,0),
33: (3869,0,0),
}

LightTypeObjects = [LightType("TW1", 540, 242, 454), # YOKE OFFSET OF 454 does not account for clamps
                    LightType("ETC_REV", 540, 270, 713)] # 713 accounts to pipe - but measure it

## Format: [ [LightType Name, (X coordinate, None, None), AxisNumber, unitID], ]
Lights = [['ETC_REV', (0, None, None), 8, 1],
['TW1', (-3628, None, None), 8, 2],
['TW1', (-4342, None, None), 22, 3],
['TW1', (-3000, None, None), 31, 4],
['TW1', (145, None, None), 22, 5],
['TW1', (3000, None, None), 31, 6],
['TW1', (3288, None, None), 22, 7],
['TW1', (4328, None, None), 8, 8],
#['TW1', (-4320, 6000, 10000), None, 9],
]

#Lights = [['TW1', (3000, None, None), 10, 1],
#['TW1', (-3000, None, None), 24, 2],]

#Format:
#   [ [ UnitID, Univ, AddrPanCoarse, AddrPanFine,AddrTiltCoarse,AddrTiltFine] ]
LightsUniverseAddr=[
[1, 1, 2,3,4,5],
[2, 1, 45,46,47,48],
[3, 1, 65,66,67,68],
[4, 1, 85,86,87,88],
[5, 1, 105,106,107,108],
[6, 1, 125,126,127,128],
[7, 1, 145,146,147,148],
[8, 1, 165,166,167,168],]

# Format per point:
#   [ ((X,Y,Z), "Name", ID - should be unique), ... ]
TrackingPoints = [((0,0,0),"Tracking Point 1", 1),
                  ((-2500,1500,0), "Mid Stage Centre Track", 2),
                  ((300,6742,100), "Upstage Left Tracking Point", 3),
                  ((0,4000,3000), "Above CS", 4),
                  ((1521,1400,2000), "Man DSR", 5),
		  ((3000,3000,3000), "3m Square", 6),
          ((-1569,3313,1000), "Table", 7),
]

# Format: [[Light.unitID, TrackingPoint.ID],...]
LightsTracking = [[1,1],[2,1],[3,7],[4,5],[5,5],[6,7],[7,5],[8,5], [9,5]]

#LightsTracking = [[1,6],[2,6]]

"""AutoRead (Control) Settings"""

sACNPriority = 150


"""
# Axis Definitions
- Describe Node per Axis definitions here, retrofit into AR_read file
"""

def main():
    print("""
COM_CONFIG.py - AUTOREAD CONFIG FILE

Sorry chief. This file is just common constant variables.
You'll want to edit this file though:\nuse a text editor, or \"nano\" on the command line
JRC 27APR2020

Support at james@jcooper.tech if you're stuck.

Uncomment the last line in this file to help you generate a new "Lights" list,
which you can use to replace the one in this file.
""")

if __name__ == "__main__":
    main()
    GenerateNewLightList()
