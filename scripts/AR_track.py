# This file takes in input from AR_read, user input functions, etc.
# We do math based on the functions, and then send that to AR_control to output.

import math
import COM_CONFIG

LightTypeObjects = [LightType("TW1", 540, 242, 454), # YOKE OFFSET OF 454 does not account for clamps
                    LightType("ETC_REV", 540, 270, 713)] # 713 accounts to pipe - but measure it

Lights = [["TW1", (-3500,2000,None), 8],
          ["TW1", (-3500,2000,None), 8]]


class Axis():
    def __init__(self, AxisNumber, axisarray):
        self.AxisNumber = AxisNumber
        self.position = axisDict[AxisNumber][0]
        self.Y_Coordinate = COM_CONFIG.AxisYValues[self.AxisNumber-1]


class LightType:
    def __init__(self, type_name, total_pan, total_tilt, yoke_offset)
        self.type_name = type_name
        self.total_pan = total_pan
        self.total_tilt = total_tilt
        self.yoke_offset = yoke_offset



class Light():
    def __init__(self,axis,ThisLightType):
        # Calculate maximum pan ranges in degrees.
        self.Axis = axis
        #Use LightType.type_name etc to access type variables
        self.LightType = ThisLightType
        self.unitID = None
        self.plus_pan = self.LightType.total_pan / 2
        self.neg_pan = - self.plus_pan
        self.plus_tilt = self.LightType.total_tilt / 2
        self.neg_tilt = - self.plus_tilt
        self.base_coord = {"X": None, "Y": None, "Z": None}
        self.offset_coord = {"X": self.base_coord["X"],
                             "Y": self.base_coord["Y"],
                             "Z": self.Axis.position - }


def setup_AxisObjects(axisDict):
    AxisObjects = []
    for key, value in axisDict:
        AxisObjects.append(Axis(key, value[0]))
    return AxisObjects


def setup_LightObjects(AxisObjects, LightTypeObjects):
    LightObjects = []
    for LightObject in LightObjects:
        LightObjects.append(Light(AxisObjects[],LightTypeObjects[0]))
    return LightObjects


def main_track(axisDict, Lights):
    AxisObjects = setup_AxisObjects(axisDict)
    LightObjects = setup_LightObjects(Lights, AxisObjects, LightTypeObjects)
