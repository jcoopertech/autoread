# This file takes in input from AR_read, user input functions, etc.
# We do math based on the functions, and then send that to AR_control to output.

import math
import COM_CONFIG

_offline_test_ = True
if _offline_test_ == True:
    # Update Axis status and Z value here - this is because we're not connected to Auto Network.
    axisDict = {
    9: (6750, 0, 0),
    31: (7000, 0, 0),
    6: (1100,0,0),
    }

class Axis():
    def __init__(self, AxisNumber, axisarray):
        self.AxisNumber = AxisNumber
        self.position = axisDict[AxisNumber][0]
        self.Y_Coordinate = COM_CONFIG.AxisYValues[int(self.AxisNumber)-1]
    def print_me(self):
        #print("--")
        #print("Axis object print_me")
        print("AxisNumber\t\t", self.AxisNumber)
        print("position\t\t", self.position)
        print("Y_Coordinate\t\t", self.Y_Coordinate)
        #print("--")


class LightType:
    def __init__(self, type_name, total_pan, total_tilt, yoke_offset):
        self.type_name = type_name
        self.total_pan = total_pan
        self.total_tilt = total_tilt
        self.yoke_offset = yoke_offset
    def print_me(self):
        #print("--")
        #print("LightType object print_me")
        print("type_name\t\t", self.type_name)
        print("total_pan\t\t", self.total_pan)
        print("total_tilt\t\t", self.total_tilt)
        print("yoke_offset\t\t", self.yoke_offset)
        #print("--")


class Light():
    def __init__(self,ThisLightType,CoordTuple,AxisClass,unitID):
        # Calculate maximum pan ranges in degrees.
        self.Axis = AxisClass
        #Use LightType.type_name etc to access type variables
        self.LightType = ThisLightType
        self.unitID = unitID
        self.plus_pan = self.LightType.total_pan / 2
        self.neg_pan = - self.plus_pan
        self.plus_tilt = self.LightType.total_tilt / 2
        self.neg_tilt = - self.plus_tilt
        self.base_coord = {"X": CoordTuple[0], "Y": self.Axis.Y_Coordinate, "Z": self.Axis.position}
        self.offset_coord = {"X": self.base_coord["X"],
                             "Y": self.Axis.Y_Coordinate,
                             "Z": self.Axis.position - self.LightType.yoke_offset}

    def print_me(self):
        print("Unit ID:", self.unitID)
        self.LightType.print_me()
        self.Axis.print_me()
        print("plus_pan\t\t", self.plus_pan)
        print("neg_pan\t\t\t", self.neg_pan)
        print("plus_tilt\t\t", self.plus_tilt)
        print("neg_tilt\t\t", self.neg_tilt)
        print("base_coord\t\t", self.base_coord)
        print("yoke_offset_coord\t", self.offset_coord)
        print("=====")

LightTypeObjects = [LightType("TW1", 540, 242, 454), # YOKE OFFSET OF 454 does not account for clamps
                    LightType("ETC_REV", 540, 270, 713)] # 713 accounts to pipe - but measure it

# LightObjects = [Light(axis,LightTypeObjects[0])]

# Format: Type, Coordinate,
Lights = [["TW1", (-3500,2000,None), 9, 1],
          ["TW1", (-3500,2000,None), 31, 2],
          ["ETC_REV", (0,None,None), 6, 3]]


def setup_AxisObjects(axisDict):
    AxisObjects = []
    for key, value in axisDict.items():
        AxisObjects.append(Axis(key, value[0]))
    return AxisObjects


def assignAxisToLight(Axis, Light):
    Light.Axis = Axis
    return Light


def getLightTypeFromObject(LightTypeObjects):
    LightTypes_type_name = []
    for LightType in LightTypeObjects:
        LightTypes_type_name.append(LightType.type_name)
    return LightTypes_type_name


def getAxisNumberFromObject(AxisObjects):
    AxisNumbers = []
    for Axis in AxisObjects:
        AxisNumbers.append(Axis.AxisNumber)
    return AxisNumbers


def setup_LightObjects(Lights, AxisObjects, LightTypeObjects):
    LightObjects = []
    #Get Axis Object to be written to Light object
    AxisNumbers = getAxisNumberFromObject(AxisObjects)
    #print([LightType for LightType in LightTypeObjects if LightType.type_name == "TW1"])
    LightTypes_type_name = getLightTypeFromObject(LightTypeObjects)
    for LightItem in Lights:
        print(LightItem)
        Axis = [Axis for Axis in AxisObjects if Axis.AxisNumber == LightItem[2]][0]
        unitID  = LightItem[3]
        CurrentLightType = [LightType for LightType in LightTypeObjects if LightType.type_name == LightItem[0]][0]
        LightObjects.append(Light(CurrentLightType, LightItem[1], Axis, unitID))
    return LightObjects


def printAllLightDetails(LightObjects):
    for Light in LightObjects:
        Light.print_me()
        print("\n")


def main_track(axisDict, Lights):
    AxisObjects = setup_AxisObjects(axisDict)
    LightObjects = setup_LightObjects(Lights, AxisObjects, LightTypeObjects)
    printAllLightDetails(LightObjects)


if __name__ == "__main__":
    if _offline_test_ == True:
        pass
    main_track(axisDict, Lights)
