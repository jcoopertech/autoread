#!/usr/bin/env python3
# - Run in a py3 environment.
# No additional packages required, only using py standard lib.

__doc__ = """
This software demo's the desired output of the read.py script.
Used for promotional purposes.
"""


__author__ = "James Cooper"
__copyright__ = "Copyright 2019, James Cooper"
__credits__ = ["James Cooper"]
__license__ = "GNU AGPLv3"
__version__ = "0.0.1"
__maintainer__ = "James Cooper"
__email__ = "james@jcooper.tech"
__status__ = "Development"


import random
import json
import time


class Node():
    """
    This Node class also stores Axis objects in self.Axes
    """
    def __init__(self,NodeID,NoAxes):
        self.NodeID = NodeID
        self.NoAxes = NoAxes
        self.Axes = [] # Store Axes objects here.


class Axis():
    def __init__(self,NodeNo,AxNo,Position):
        self.NodeNo = (NodeNo)
        self.AxNo = AxNo
        self.Position = Position


def createSpoofAxes(NodeNo, NoAxes):
    # Create Axes to go in each node, with random Positions.
    ClassArray = []
    for AxNo in range(NoAxes):
        Position = random.randint(900,14100)
        ClassArray.append(Axis(NodeNo,AxNo,Position))
    return ClassArray


def displayInfo(Node):
    # Get all Axes per Node, display here.
    for Axis in Node.Axes:
        print(("""{2}\t- Simotion Node: {0}\tChannel: {1}.\t@ {3}mm""".format( \
        Node.NodeID, Axis.AxNo, Axis.AxisName, Axis.Position)))


def GeneraliseIntoECham(MasterNodes):
    # Look up the Axis names from the list, as well as echam number.
    with open("axis_list.txt","r") as axis_list_file:
        axis_list = json.load(axis_list_file)
    line_axis_count = 0
    for Node in MasterNodes:
        for Axis in Node.Axes:
            Axis.AxisName = axis_list[line_axis_count][2]
            line_axis_count += 1
    return MasterNodes


def setUpNodes():
    # Set up Node objects, with number of Axes associated to it.
    NodeClassArray = []
    Nodes = [[1,24],[2,16]]
    for NodeItem in Nodes:
        NodeClassArray.append(Node(NodeItem[0],NodeItem[1]))
    return NodeClassArray


# Main storage for all Nodes in the system.
def main():
    MasterNodes = setUpNodes()
    for NodeObject in MasterNodes:
        NodeObject.Axes = createSpoofAxes(NodeObject.NodeID, NodeObject.NoAxes)
    MasterNodes = GeneraliseIntoECham(MasterNodes)
    for NodeObject in MasterNodes:
        displayInfo(NodeObject)


if __name__ == "__main__":
    live = False
    if live == True:
        while True:
            main()
    else:
        main()
    if live == True:
        print("*"*50)
        time.sleep(0.50)
