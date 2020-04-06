import json

AxisList = []

for axis in range(40):
    AxisName = "Axis {0}".format(axis+1)
    eChamNo = axis + 1
    AxisLine = [axis,eChamNo,AxisName]
    AxisList.append(AxisLine)

with open("axis_list.txt", "w") as axis_list:
    json.dump(AxisList,axis_list)
