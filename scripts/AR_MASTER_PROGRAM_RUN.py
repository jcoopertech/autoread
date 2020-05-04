#!/usr/bin/python3

import COM_CONFIG
import AR_track
import AR_read
import AR_control


ContinuousLoop = True
if __name__=="__main__":
    while ContinuousLoop == True:
        runtime_err = []
        try:
            AxisDict = AR_read.read_main()
        except OSError as fubar:
            runtime_err.append(fubar)
            ContinuousLoop = False
            print("""AutoRead Critical Warning: ---- No Automation network Input detected.
Reverting to Offline Axis Positions""")
            AxisDict = COM_CONFIG.axisDict

        # Check we have all the info we need.
        try:
            COM_CONFIG.Lights
            AR_track.main_track(AxisDict, COM_CONFIG.Lights)
        except AttributeError:
            print("\"Lights\" list could not be found in COM_CONFIG.py.")
    if len(runtime_err) > 0:
        print("The following errors happened:")
        for err in runtime_err:
            print(err)
