# This file takes in input from AR_read, user input functions, etc.
# We do math based on the functions, and then send that to AR_control to output.

import math
import COM_CONFIG


class Coordinate():
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z
    def print_me(self):
        print("\tX:\t", self.X)
        print("\tY:\t", self.Y)
        print("\tZ:\t", self.Z)


class TrackingPoint():
    def __init__(self, CoordTuple, Name, ID):
        self.Coordinate = Coordinate(CoordTuple[0], CoordTuple[1], CoordTuple[2])
        self.Name = Name
        self.ID = ID
        self.TrackedBy = []
    def print_me(self):
        print("TrackingPoint")
        print("Name:\t\t", self.Name)
        print("ID:\t\t", self.ID)
        self.Coordinate.print_me()


class Axis():
    def __init__(self, AxisNumber, position, WinchCalibration = 0,):
        self.AxisNumber = AxisNumber
        self.Coordinate = Coordinate(None, COM_CONFIG.AxisYValues[int(self.AxisNumber)-1], position)
        self.WinchCalibration = WinchCalibration
        self.CalibratedCoordinate = Coordinate(None, COM_CONFIG.AxisYValues[int(self.AxisNumber)-1], position + self.WinchCalibration)
    def print_me(self):
        #print("--")
        #print("Axis object print_me")
        print("AxisNumber:\t\t", self.AxisNumber)
        print("WinchCalibration:\t", self.WinchCalibration)
        print("Coordinate:")
        self.Coordinate.print_me()
        print("CalibratedCoordinate:")
        self.CalibratedCoordinate.print_me()
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
        print("type_name:\t\t", self.type_name)
        print("total_pan:\t\t", self.total_pan)
        print("total_tilt:\t\t", self.total_tilt)
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
        self.BaseCoord = Coordinate(CoordTuple[0], self.Axis.CalibratedCoordinate.Y, self.Axis.CalibratedCoordinate.Z)
        self.OffsetCoord = Coordinate(  self.BaseCoord.X, self.BaseCoord.Y, self.BaseCoord.Z - self.LightType.yoke_offset)
        self.TrackingPoint = None
        self.PanDeg = None
        self.TiltDeg = None
    def print_me(self):
        print("Unit ID:", self.unitID)
        print(".LightType attributes")
        self.LightType.print_me()
        print(".Axis attributes")
        self.Axis.print_me()
        print(".BaseCoord attributes")
        self.BaseCoord.print_me()
        print(".OffsetCoord attributes")
        self.OffsetCoord.print_me()
        print("plus_pan:\t\t", self.plus_pan)
        print("neg_pan\t\t\t", self.neg_pan)
        print("plus_tilt\t\t", self.plus_tilt)
        print("neg_tilt\t\t", self.neg_tilt)
        print("PanDeg\t\t", self.PanDeg)
        print("TiltDeg\t\t", self.TiltDeg)
        if self.TrackingPoint != None:
            self.TrackingPoint.print_me()
        else:
            print("TrackingPoint\t\t", self.TrackingPoint)


LightTypeObjects = [LightType("TW1", 540, 242, 454), # YOKE OFFSET OF 454 does not account for clamps
                    LightType("ETC_REV", 540, 270, 713)] # 713 accounts to pipe - but measure it


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
        Axis = [Axis for Axis in AxisObjects if Axis.AxisNumber == LightItem[2]][0]
        unitID  = LightItem[3]
        CurrentLightType = [LightType for LightType in LightTypeObjects if LightType.type_name == LightItem[0]][0]
        LightObjects.append(Light(CurrentLightType, LightItem[1], Axis, unitID))
    return LightObjects


def setup_TrackingPoints(TrackingPoints):
    TrackingObjects = []
    for Point in TrackingPoints:
        TrackingObjects.append(TrackingPoint(Point[0], Point[1], Point[2]))
    return TrackingObjects


def printAllLightDetails(LightObjects):
    for Light in LightObjects:
        Light.print_me()
        print("\n")


def printAllTrackingPointDetails(TrackingObjects):
    for Point in TrackingObjects:
        Point.print_me()
        print("\n")


def GiveLightTrackingPoint(LightObjects, TrackingObjects):
    for Light in LightObjects:
        try:
            WhichPointID = int(input("Which point should Light:{0} track?\n\t-\tType 0 for no Point".format(Light.unitID)))
        except ValueError:
            print("ValueError raised. Telling to track no point.")
            WhichPointID = 0
        if WhichPointID != 0:
            Light.TrackingPoint = [Point for Point in TrackingObjects if WhichPointID == Point.ID][0]
        else:
            Light.TrackingPoint = None


def CalculateLightAngles(LightsTracking, Light, TrackingObjects):
    """We need to use the following, based on the calculators found at:
    https://planetcalc.com/7952/"""
    LightX = Light.OffsetCoord.X
    LightY = Light.OffsetCoord.Y
    LightZ = Light.OffsetCoord.Z
    PointX = Light.TrackingPoint.Coordinate.X
    PointY = Light.TrackingPoint.Coordinate.Z
    PointZ = Light.TrackingPoint.Coordinate.Y
    if LightZ > PointZ:
        Z_Difference = LightZ - PointZ
        X_Difference = LightX - PointX
        Y_Difference = LightY - PointY
        PolarDeg = math.degrees(math.atan(math.sqrt(X_Difference**2+Y_Difference**2)/Z_Difference))
        print(X_Difference, Y_Difference, Z_Difference)
        print(PolarDeg)
    PanDeg = math.degrees(math.atan2(Y_Difference, X_Difference))
    Light.TiltDeg = PolarDeg
    Light.PanDeg = PanDeg


def updateTrackingPointsAssociation(LightsTracking, LightObjects, TrackingObjects):
    for Light in LightObjects:
            association = [Assignment for Assignment in LightsTracking if Assignment[0] == Light.unitID][0]
            print(association)
            Light.TrackingPoint = [Point for Point in TrackingObjects if association[1] == Point.ID][0]


def main_track(axisDict, Lights):
    #Lights = GenerateNewLightList()
    AxisObjects = setup_AxisObjects(axisDict)
    LightObjects = setup_LightObjects(Lights, AxisObjects, LightTypeObjects)
    TrackingObjects = setup_TrackingPoints(COM_CONFIG.TrackingPoints)
#    GiveLightTrackingPoint(LightObjects, TrackingObjects)
    updateTrackingPointsAssociation(COM_CONFIG.LightsTracking, LightObjects, TrackingObjects)
    for Light in LightObjects:
        if Light.TrackingPoint != None:
            CalculateLightAngles(COM_CONFIG.LightsTracking, Light, TrackingObjects)
    printAllLightDetails(LightObjects)



if __name__ == "__main__":
    if COM_CONFIG._offline_test_ == True:
        pass
    #COM_CONFIG.GenerateNewLightList()
    main_track(COM_CONFIG.axisDict,COM_CONFIG.Lights)
