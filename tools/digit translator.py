# James Cooper 2019
# Base 2, 10 and 16 converter.
#
#
#


class Error(Exception):
    """Base class for exceptions"""
    def __init__(self):
        pass


class InputError(Error):
    """Exception raised for errors in the input dummy.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


bit = "\#DEFAULT\#"
err_msg = [
"Unexpected length of item.",
"This value isn't in the list. Left is correct options:",
"{0} isn't in the list. Here are the accepted options.".format(bit),]


def getValue(checks=None, acceptedOpt=None, msg=None):
    # Sanitise input here
    if acceptedOpt != None:
        acceptedOpt = [str(x) for x in acceptedOpt]
        print("Accepted Options: \"{0}\"".format(", ".join(acceptedOpt)))
    if msg != None:
        usr_val = input("User Input - {0}\n".format(msg))
    else:
        usr_val = input("User Input:\n")

    if checks == "showMenu":
        # Sanitise input for showMenu func.
        if len(usr_val) != 1:
            raise InputError(usr_val, err_msg[0])
        elif usr_val not in acceptedOpt:
            raise InputError(acceptedOpt, err_msg[1])

    elif checks != None:
        # Sanitise input for ist options input
        for bit in usr_val:
            if not bit in acceptedOpt:
                raise InputError(acceptedOpt, err_msg[2])
    return str(usr_val)


def showMenu():
    # acceptedOpt should be changed here, based on what options are available.
    acceptedOpt = ["B","H","D","b","h","d"]
    print("""
Select input type here.

B\t- Entering a (positive) Binary value.
H\t- Entering a Hex value.
D\t- Entering a Decimal value.
""")
    return acceptedOpt


def initialise():
    # Set up anything for the program here, welcome msg etc.
    print("""
Welcome to my little binary, hex and decimal conversor tool.

Select what sort of number you're inputting, let us do the rest!""")
    acceptedOpt = showMenu()
    return acceptedOpt


def convertFromBinary():
    usr_val = getValue("binary", ["0","1"], "Enter binary (Base 2)")
    denary = int(usr_val, 2)
    hexadecimal = format(denary,"X")
    print("""
You entered: {0}

In \tDecimal\t{1},
\tHex\t{2}
""".format(usr_val, denary, hexadecimal))


def convertFromHex():
    def makeHexLetterList():
        # This function is only used here - so it can be child of convertFromHex
        # Generates a list of the hex digits... stoically returns ["A", .. "F"]
        # Make to test my python
        ord_start = 65
        hex_letters = [chr(x) for x in range(65, 65+6)]
        return hex_letters
    acceptedOpt = [x for x in range(0,10)] + [y for y in makeHexLetterList()]
    usr_val = getValue("hex", acceptedOpt, "Enter hexadecimal (Base 16))")
    denary = int(usr_val, 16)
    binary = format(denary,"b")
    print("""
You entered: {0}

In \tDecimal\t{1},
\tBinary\t{2}
""".format(usr_val, denary, binary))


def convertFromDenary():
    acceptedOpt = range(0,10)
    usr_val = getValue("denary", acceptedOpt, "Enter decimal (Base 10)")
    binary = format(int(usr_val), "b")
    hexadecimal = format(int(usr_val),"X")
    print("""
You entered: {0}

In \tBinary\t{1},
\tHex\t{2}
""".format(usr_val, binary, hexadecimal))


def doDebugFunctions(is_debug):
    def printRestartLine():
        """This is literally just a line. It should only run at top of run.
        Which is why it's nested."""
        line = "=" * 40
        msg = " RESTART "
        print(line+msg+line ,end="")
    # If you need to test a function, just pop it here I guess.
    printRestartLine()
    # Include a pass just in case you forget... just save the headache.
    pass

if __name__ == "__main__":
    is_debug = False
    if is_debug == True:
        doDebugFunctions(is_debug)
    acceptedOpt = initialise()
    menuOpt = getValue("showMenu", acceptedOpt).upper()
    if menuOpt == acceptedOpt[0]:
        convertFromBinary()
    elif menuOpt == acceptedOpt[1]:
        convertFromHex()
    elif menuOpt == acceptedOpt[2]:
        convertFromDenary()
