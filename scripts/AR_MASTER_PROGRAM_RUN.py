#!/usr/bin/python3

import COM_CONFIG
import AR_track
import AR_read
import AR_control


ContinuousLoop = True
if __name__=="__main__":
    while ContinuousLoop == True:
        try:
            AxisDict = AR_read.read_main()
        except OSError:
            print("""\n\nAutoRead Critical Warning: ---- No Automation network Input detected.
            Reverting to Offline Axis Positions\n\n""")
            AxisDict = COM_CONFIG.axisDict
        AR_track.main_track(AxisDict, COM_CONFIG.Lights)
        print("\n".join([str(item) for item in COM_CONFIG.LightObjects]))
        ContinuousLoop = False
