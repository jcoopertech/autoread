#!/usr/bin/python3

import sacn
import COM_CONFIG
import socket
# AR_control.py
"""
This file takes each light's degree values from AR_track, and converts them into something that sACN can output.

Process: Get 16 bit number, perform logical bitwise shift on it, to take it down to coarse value.
Then take literal remainder, of number of values coarse provides, then return as fine.
"""

source_name = "AutoRead_"+socket.gethostname()
Universe = 1

def test_output(sender,dmxData):
    sender[1].dmx_data = tuple(dmxData)


def setupSACNoutput(StartCode = "0"):
    sender = sacn.sACNsender(fps=int(40), StartCode = StartCode)
    sender.source_name = source_name
    sender.activate_output(Universe)
    sender[1].priority = COM_CONFIG.sACNPriority
    sender[1].multicast = True
    sender.start()
    return sender


def mergeSACNdata(dmxData, alteredOutputData=None):
    dmxData = list(dmxData)
    #Take the addresses, assign their values.
    dmxData[45:46] = (128,129)
    return dmxData


def setupSACNreceiver():
    receiver = sacn.sACNreceiver()
    receiver.start()
    receiver.join_multicast(1)
    @receiver.listen_on('universe', universe=Universe)
    def callback(packet):
        receivedData = packet.dmxData
    return receivedData

if __name__=="__main__":
    sender = setupSACNoutput()
    priority = setupSACNoutput("DD")
    dmxData = setupSACNreceiver()
    alteredOutputData = mergeSACNdata(dmxData)
    test_output(sender, alteredOutputData)
