
# AutoRead Configuration File default

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
"IP": "172.16.1.52"
"recv": False,
}

Nodes = [Node1,Node2]
NumberOfNodes = len(Nodes)


"""AutoRead (Track) Settings"""
# Define AxisYValues based on CAD plan
AxisYValues = [200,500,800,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,
3200,3400,3600,3800,4000,4200,4400,4600,4800,5000,5200,5400,5600,5800,6000,6200,
6400,6600,6800,7000]


"""AutoRead (Control) Settings"""




"""
# Axis Definitions
- Describe Node per Axis definitions here, retrofit into AR_read file
"""

def main():
    print("""Sorry chief. This file is just common constant variables.
    You'll want to edit this file though!""")

if __name__ is "__main__":
    main()
