# James Cooper 2019
# Base 2, 10 and 16 converter.
#
#
#


class Error(Exception):
    """Base class for exceptions"""
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


class MalformedNumberError(Error):
    def __init__(self, message):
        self.message = message
        

def getValue(checks=None, acceptedOpt=None, msg=None):
    # Sanitise input here.
    if acceptedOpt != None:
        print("Accepted Options: \"{0}\"".format(", ".join(acceptedOpt)))
    usr_val = input("User Input:\n")
    if checks == "showMenu":
        # Sanitise input for showMenu func.
        if len(usr_val) != 1:
            raise InputError(usr_val, "This value is too long. Max: 1")
        elif usr_val not in acceptedOpt:
            raise InputError(acceptedOpt, "This value isn't in the list. Left is correct options:")
    elif checks == "binary":
        if not len(usr_val) % 2 == 0:
            raise MalformedNumberError("Binary integers must have an even number of bits. This one has {}".format(len(usr_val)))
        for bit in usr_val:
            if not bit in acceptedOpt:
                raise InputError(acceptedOpt, "{0} isn't in the list. Left is correct options:".format(bit))
    return str(usr_val)


def guessBase():
    # Let the software guess the user input - vanity feature, unreliable.
    pass


def showMenu():
    # I wonder what this could be...
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
    exitState = False
    print("""
Welcome to my little binary, hex and decimal conversor tool.

Select what sort of number you're inputting, let us do the rest!""")
    acceptedOpt = showMenu()
    return exitState, acceptedOpt


def convertFromBinary():
    usr_val = getValue("binary", ["0","1"], "Enter binary digits")
    denary = int(usr_val, 2)
    hexadecimal = format(denary,"X")
    print("""
You entered: {0}

In \tDecimal\t{1},
\tHex\t{2}
""".format(usr_val, denary, hexadecimal))


def convertFromHex():
    usr_val = getValue("decimal", [range(0,10)], "Enter binary digits")
    denary = int(usr_val, 2)
    hexadecimal = format(denary,"X")
    print("""
You entered: {0}

In \tDecimal\t{1},
\tHex\t{2}
""".format(usr_val, denary, hexadecimal))


def convertFromDenary():
    usr_val = getValue("binary", ["0","1"], "Enter binary digits")
    denary = int(usr_val, 2)
    hexadecimal = format(denary,"X")
    print("""
You entered: {0}

In \tDecimal\t{1},
\tHex\t{2}
""".format(usr_val, denary, hexadecimal))


if __name__ == "__main__":
    exitState, acceptedOpt = initialise()
    menuOpt = getValue("showMenu", acceptedOpt)
        
    if menuOpt.upper() == acceptedOpt[0]:
        convertFromBinary()
    elif menuOpt.upper() == acceptedOpt[1]:
        # Do Hex Input
        pass
    elif menuOpt.upper() == acceptedOpt[2]:
        # Do Denary Input
        pass
    
    else:
        # Do exit state/error condition.
        pass
