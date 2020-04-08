# axisDict Updater
# Mainly used for online testing

from random import randint


def GenerateNewAxisDict():
    axisDict = {}
    NumberOfAxes = 33
    output = "axisDict = {\n"
    for i in range(NumberOfAxes):
        output += "{0}: ({1},0,0), \n".format(i+1, randint(1100,14100))
    output += "}"
    return output


if __name__ == "__main__":
    print(GenerateNewAxisDict())
