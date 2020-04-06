
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

"Axis Node Channels"
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

"""AutoRead (Track) Settings"""



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
