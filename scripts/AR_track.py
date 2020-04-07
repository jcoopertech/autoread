# This file takes in input from AR_read, user input functions, etc.
# We do math based on the functions, and then send that to AR_control to output.

import math
import COM_CONFIG

_offline_test_ = True
if _offline_test_ == True:
    axisDict = {
    "8": (6750, 0, 0),
    }

class Axis():
    def __init__(self, AxisNumber, axisarray):
        self.AxisNumber = AxisNumber
        self.position = axisDict[str(AxisNumber)][0]
        self.Y_Coordinate = COM_CONFIG.AxisYValues[int(self.AxisNumber)-1]


class LightType:
    def __init__(self, type_name, total_pan, total_tilt, yoke_offset):
        self.type_name = type_name
        self.total_pan = total_pan
        self.total_tilt = total_tilt
        self.yoke_offset = yoke_offset


class Light():
    def __init__(self,axis,ThisLightType, (Base_X,Base_Y,Base_Z)):
        # Calculate maximum pan ranges in degrees.
        self.Axis = axis
        #Use LightType.type_name etc to access type variables
        self.LightType = ThisLightType
        self.unitID = None
        self.plus_pan = self.LightType.total_pan / 2
        self.neg_pan = - self.plus_pan
        self.plus_tilt = self.LightType.total_tilt / 2
        self.neg_tilt = - self.plus_tilt
        self.base_coord = {"X": Base_X, "Y": Base_Y, "Z": Base_Z}
        self.offset_coord = {"X": self.base_coord["X"],
                             "Y": self.base_coord["Y"],
                             "Z": self.Axis.position - self.LightType.yoke_offset}


LightTypeObjects = [LightType("TW1", 540, 242, 454), # YOKE OFFSET OF 454 does not account for clamps
                    LightType("ETC_REV", 540, 270, 713)] # 713 accounts to pipe - but measure it

# LightObjects = [Light(axis,LightTypeObjects[0])]

Lights = [["TW1", (-3500,2000,None), "8"],
          ["TW1", (-3500,2000,None), "8"]]


def setup_AxisObjects(axisDict):
    AxisObjects = []
    print(axisDict)
    for key, value in axisDict.items():
        AxisObjects.append(Axis(key, value[0]))
    return AxisObjects


def setup_LightObjects(Lights, AxisObjects, LightTypeObjects):
    LightObjects = []
    for Light in Lights:
        # Determine Axis to assign here
        LightObjects.append(Light(axis, LightTypeObjects[0], ))
    return LightObjects


def main_track(axisDict, Lights):
    AxisObjects = setup_AxisObjects(axisDict)
    LightObjects = setup_LightObjects(Lights, AxisObjects, LightTypeObjects)


if __name__ == "__main__":
    if _offline_test_ == True:
        pass
    main_track(axisDict, Lights)
