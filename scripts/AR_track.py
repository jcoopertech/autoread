# This file takes in input from AR_read, user input functions, etc.
# We do math based on the functions, and then send that to AR_control to output.

import math
import COM_CONFIG
import sys, getopt

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
    def print_me(self):
        print("TrackingPoint")
        print("Name:\t\t", self.Name)
        print("ID:\t\t", self.ID)
        self.Coordinate.print_me()
    def print_simple(self):
        print("Tracking Point:\t\t", self.Name)


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


class Light():
    def __init__(self,ThisLightType,CoordTuple,AxisClass,unitID):
        # Calculate maximum pan ranges in degrees.
        if isinstance(AxisClass, Axis):
            self.Axis = AxisClass
        else:
            self.Axis = None
        #Use LightType.type_name etc to access type variables
        self.LightType = ThisLightType
        self.unitID = unitID
        self.plus_pan = self.LightType.total_pan / 2
        self.neg_pan = - self.plus_pan
        self.plus_tilt = self.LightType.total_tilt / 2
        self.neg_tilt = - self.plus_tilt
        if self.Axis == None:
            self.BaseCoord = AxisClass
            print(self.BaseCoord)
        if self.Axis != None:
            self.BaseCoord = Coordinate(CoordTuple[0], self.Axis.CalibratedCoordinate.Y, self.Axis.CalibratedCoordinate.Z)
        self.OffsetCoord = Coordinate(  self.BaseCoord.X, self.BaseCoord.Y, self.BaseCoord.Z - self.LightType.yoke_offset)
        self.TrackingPoint = None
        self.PanDeg = None
        self.TiltDeg = None
        self.Pan = None
        self.Tilt = None
        self.Addresses = []
        self.Universe = None
    def print_me(self):
        print("Unit ID:", self.unitID)
        print(".LightType attributes")
        self.LightType.print_me()
        print(".Axis attributes")
        if self.Axis != None:
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
        print("Pan:\t\t", self.Pan)
        print("Tilt:\t\t", self.Tilt)
        print("Universe:\t\t", self.Universe)
        print("Addresses:\t\t", self.Addresses)
        if self.TrackingPoint != None:
            self.TrackingPoint.print_me()
        else:
            print("TrackingPoint\t\t", self.TrackingPoint)
    def print_simple(self):
        print("Unit ID:", self.unitID)
        print("PanDeg\t\t", self.PanDeg)
        print("TiltDeg\t\t", self.TiltDeg)
        self.TrackingPoint.print_simple()



LightTypeObjects = COM_CONFIG.LightTypeObjects

def setup_AxisObjects(axisDict):
    AxisObjects = []
    for key, value in axisDict.items():
        AxisObjects.append(Axis(key, value[0]))
    return AxisObjects


def setup_LightObjects(Lights, AxisObjects, LightTypeObjects):
    LightObjects = []
    #Get Axis Object to be written to Light object
    #print([LightType for LightType in LightTypeObjects if LightType.type_name == "TW1"])
    for LightItem in Lights:
        unitID  = LightItem[3]
        CurrentLightType = [LightType for LightType in LightTypeObjects if LightType.type_name == LightItem[0]][0]
        #print(LightItem[2])
        if LightItem[2] == None:
            #If there is no Axis assigned
            BaseCoord = Coordinate(LightItem[1][0], LightItem[1][1], LightItem[1][2])
            LightObjects.append(Light(CurrentLightType, LightItem[1], BaseCoord, unitID))
        else:
            Axis = [Axis for Axis in AxisObjects if Axis.AxisNumber == LightItem[2]][0]
            LightObjects.append(Light(CurrentLightType, LightItem[1], Axis, unitID))
    return LightObjects


def setup_TrackingPoints(TrackingPoints):
    TrackingObjects = []
    for Point in TrackingPoints:
        TrackingObjects.append(TrackingPoint(Point[0], Point[1], Point[2]))
    return TrackingObjects


def printAllLightDetails(LightObjects, argv, opts):
    for opt, arg in opts:
        if opt == "-v":
            verbose = arg
        else:
            verbose = 0
    for Light in LightObjects:
        if int(verbose) == 2:
            Light.print_me()
        elif int(verbose) == 1:
            Light.print_simple()
        else:
            ""
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
    """Calculate Azimuth and Elevation (Pan/Tilt) for all the
    lights defined in the AutoRead system."""

    LightX = Light.OffsetCoord.X
    LightY = Light.OffsetCoord.Y
    LightZ = Light.OffsetCoord.Z
    PointX = Light.TrackingPoint.Coordinate.X
    PointY = Light.TrackingPoint.Coordinate.Z
    PointZ = Light.TrackingPoint.Coordinate.Y
    Z_Difference = LightZ - PointZ
    X_Difference = LightX - PointX
    Y_Difference = LightY - PointY
#    print("Light ", Light.unitID, "X",X_Difference, "Y",Y_Difference, "Z",Z_Difference)
    TiltAngle = math.degrees(math.atan(math.sqrt(X_Difference**2+Y_Difference**2)/Z_Difference))
#    print("Tilt", TiltAngle)
    PanDeg = -(math.degrees(math.atan2(Y_Difference, X_Difference)))+90
#    print("Pan", PanDeg)
    Light.TiltDeg = TiltAngle
    Light.PanDeg = PanDeg
    #https://planetcalc.com/7952/"""

def updateTrackingPointsAssociation(LightsTracking, LightObjects, TrackingObjects):
    for Light in LightObjects:
            association = [Assignment for Assignment in LightsTracking if Assignment[0] == Light.unitID][0]
#            print(association)
            Light.TrackingPoint = [Point for Point in TrackingObjects if association[1] == Point.ID][0]


def remap(degreeinput,degreemin,degreemax,dmxmin=0,dmxmax=65536):
    """
    Convert the degree value to a 16 bit dmx number.
    """
    DMXvalue = ((degreeinput - degreemin) * (dmxmax-dmxmin) / (degreemax - degreemin) + dmxmin)
    return DMXvalue


def resplitfinecontrol(DMXvalue):
    DMXvalue = round(int(DMXvalue))
    coarse = DMXvalue >> 8
    fine = DMXvalue % 256
    return coarse,fine


def AssignAddressesToLights(LightsUniverseAddr, Light):
    try:
        Light.Addresses = [LightAsAddresses[1:6] for LightAsAddresses in LightsUniverseAddr if LightAsAddresses[0] == Light.unitID][0]
        Light.Universe = Light.Addresses[0]
        Light.Addresses.remove(Light.Addresses[0])
    except IndexError:
        print("Light {0}'s address could not be found!' ".format(Light.unitID))

def main_track(axisDict, Lights, argv=None, opts=None):
    #Lights = GenerateNewLightList()
    AxisObjects = setup_AxisObjects(axisDict)
    LightObjects = setup_LightObjects(Lights, AxisObjects, LightTypeObjects)
    TrackingObjects = setup_TrackingPoints(COM_CONFIG.TrackingPoints)
#    GiveLightTrackingPoint(LightObjects, TrackingObjects)
    updateTrackingPointsAssociation(COM_CONFIG.LightsTracking, LightObjects, TrackingObjects)
    for Light in LightObjects:
        if Light.TrackingPoint != None:
            CalculateLightAngles(COM_CONFIG.LightsTracking, Light, TrackingObjects)
            """Calculate Pan sACN 16 bit"""
            Light.Pan = resplitfinecontrol(remap(Light.PanDeg,Light.neg_pan,Light.plus_pan))
            Light.Tilt = resplitfinecontrol(remap(Light.TiltDeg,Light.neg_tilt,Light.plus_tilt))
            AssignAddressesToLights(COM_CONFIG.LightsUniverseAddr, Light)
            #CalculatesACNforLights(COM_CONFIG.LightsUniverseAddr)
    COM_CONFIG.LightObjects = LightObjects
    printAllLightDetails(LightObjects, argv, opts)



if __name__ == "__main__":
    if COM_CONFIG._offline_test_ == True:
        pass
    #COM_CONFIG.GenerateNewLightList()
    argv = sys.argv[1:]
    try:
       opts, args = getopt.getopt(argv,"v:")
       main_track(COM_CONFIG.axisDict,COM_CONFIG.Lights, args, opts)
    except getopt.GetoptError:
        print('AR_track.py -v [0-2]')
        sys.exit(2)
