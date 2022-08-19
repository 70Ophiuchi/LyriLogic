def TT_maker(gate, case):

    TT = "\nTRUTH TABLE FOR {GATE} GATE: \n A B    OUTPUT \n 0 0    {a} \n 1 0    {b} \n 0 1    {c} \n 1 1    {d}\n"
    YI = "<---- YOUR INPUT AND OUTPUT"

    if gate == "AND" and case == "a":
        return TT.format(GATE="AND", a="0 " + YI, b="0 ", c="0 ", d="1 ")
    elif gate == "AND" and case == "b":
        return TT.format(GATE="AND", a="0 ", b="0 " + YI, c="0 ", d="1 ")
    elif gate == "AND" and case == "c":
        return TT.format(GATE="AND", a="0 ", b="0 ", c="0 " + YI, d="1 ")
    elif gate == "AND" and case == "d":
        return TT.format(GATE="AND", a="0 ", b="0 ", c="0 ", d="1 " + YI)

    if gate == "NAND" and case == "a":
        return TT.format(GATE="NAND", a="1 " + YI, b="1 ", c="1 ", d="0 ")
    elif gate == "NAND" and case == "b":
        return TT.format(GATE="NAND", a="1 ", b="1 " + YI, c="1 ", d="0 ")
    elif gate == "NAND" and case == "c":
        return TT.format(GATE="NAND", a="1 ", b="1 ", c="1 " + YI, d="0 ")
    elif gate == "NAND" and case == "d":
        return TT.format(GATE="NAND", a="1 ", b="1 ", c="1 ", d="0 " + YI)


    if gate == "NOT" and case == "a":
        return "\nTRUTH TABLE FOR {GATE} GATE: \n A    OUTPUT \n 0    {a} \n 1    {b}\n".format(GATE="NOT", a="1 " + YI, b="0 ")
    elif gate == "NOT" and case == "b":
        return "\nTRUTH TABLE FOR {GATE} GATE: \n A    OUTPUT \n 0    {a} \n 1    {b}\n".format(GATE="NOT", a="1 ", b="0 " + YI)

    if gate == "OR" and case == "a":
        return TT.format(GATE="OR", a="0 " + YI, b="1 ", c="1 ", d="1 ")
    elif gate == "OR" and case == "b":
        return TT.format(GATE="OR", a="0 ", b="1 " + YI, c="1 ", d="1 ")
    elif gate == "OR" and case == "c":
        return TT.format(GATE="OR", a="0 ", b="1 ", c="1 " + YI, d="1 ")
    elif gate == "OR" and case == "d":
        return TT.format(GATE="OR", a="0 ", b="1 ", c="1 ", d="1 " + YI)

    if gate == "XOR" and case == "a":
        return TT.format(GATE="XOR", a="0 " + YI, b="1 ", c="1 ", d="0 ")
    elif gate == "XOR" and case == "b":
        return TT.format(GATE="XOR", a="0 ", b="1 " + YI, c="1 ", d="0 ")
    elif gate == "XOR" and case == "c":
        return TT.format(GATE="XOR", a="0 ", b="1 ", c="1 " + YI, d="0 ")
    elif gate == "XOR" and case == "d":
        return TT.format(GATE="XOR", a="0 ", b="1 ", c="1 ", d="0 " + YI)


    if gate == "NOR" and case == "a":
        return TT.format(GATE="NOR", a="1 " + YI, b="0 ", c="0 ", d="0 ")
    elif gate == "NOR" and case == "b":
        return TT.format(GATE="NOR", a="1 ", b="0 " + YI, c="0 ", d="0 ")
    elif gate == "NOR" and case == "c":
        return TT.format(GATE="NOR", a="1 ", b="0 ", c="0 " + YI, d="0 ")
    elif gate == "NOR" and case == "d":
        return TT.format(GATE="NOR", a="1 ", b="0 ", c="0 ", d="0 " + YI)


class Gates():

    def __init__(self):
        self.AND_OUTPUT = 0
        self.NOT_OUTPUT = 0
        self.OR_OUTPUT = 0
        self.NOR_OUTPUT = 0
        self.NAND_OUTPUT = 0
        self.XOR_OUTPUT = 0

        self.TT = "TRUTH TABLE FOR {GATE} GATE: \n A B    OUTPUT \n 0 0    0 \n 1 0    1 \n 0 1    1 \n 1 1    1"



    def AND(self, input, RTT=False):
        
        a, b = input
        case = ""

        if a and b:
            self.AND_OUTPUT = 1
            case = "d"
        else:
            if a == 1 and b == 0:
                case = "b"
            elif a == 0 and b == 1:
                case = "c"
            elif a == 0 and b == 0:
                case = "a"
            self.AND_OUTPUT = 0

        if RTT:
            print(TT_maker("AND", case))

        return "OUTPUT: " + str(self.AND_OUTPUT)

    def NAND(self, input, RTT=False):
        
        a, b = input
        case = ""

        if a and b:
            self.NAND_OUTPUT = 0
            case = "d"
        else:
            if a == 1 and b == 0:
                case = "b"
            elif a == 0 and b == 1:
                case = "c"
            elif a == 0 and b == 0:
                case = "a"
            self.NAND_OUTPUT = 1

        if RTT:
            print(TT_maker("NAND", case))

        return "OUTPUT: " + str(self.NAND_OUTPUT)


    def NOT(self, input, RTT=False):

        a = input
        case = ""
        if a:
            self.NOT_OUTPUT = 0
            case = "b"
        else:
            self.NOT_OUTPUT = 1
            case = "a"
        
        if RTT:
            print(TT_maker("NOT", case))
        return "OUTPUT: " + str(self.NOT_OUTPUT)

    def OR(self, input, RTT=False):

        a, b = input
        case = ""

        if a == 1 and b == 0:
            self.OR_OUTPUT = 1
            case = "b"
        elif a == 0 and b == 1:
            self.OR_OUTPUT = 1
            case = "c"
        elif a == 1 and b == 1:
            self.OR_OUTPUT = 1
            case = "d"

        else:
            case = "a"
            self.OR_OUTPUT = 0

        if RTT:
            print(TT_maker("OR", case))

        return "OUTPUT: " + str(self.OR_OUTPUT)

    def XOR(self, input, RTT=False):

        a, b = input
        case = ""

        if a == 1 and b == 0:
            self.XOR_OUTPUT = 1
            case = "b"
        elif a == 0 and b == 1:
            self.XOR_OUTPUT = 1
            case = "c"
        elif a == 1 and b == 1:
            self.XOR_OUTPUT = 0
            case = "d"

        else:
            case = "a"
            self.XOR_OUTPUT = 0

        if RTT:
            print(TT_maker("XOR", case))

        return "OUTPUT: " + str(self.XOR_OUTPUT)

    def NOR(self, input, RTT=False):

        a, b = input
        case = ""

        if a == 1 and b == 0:
            self.NOR_OUTPUT = 0
            case = "b"
        elif a == 0 and b == 1:
            self.NOR_OUTPUT = 0
            case = "c"
        elif a == 1 and b == 1:
            self.NOR_OUTPUT = 0
            case = "d"

        else:
            case = "a"
            self.NOR_OUTPUT = 1

        if RTT:
            print(TT_maker("NOR", case))

        return "OUTPUT: " + str(self.NOR_OUTPUT)


# print(Gates().AND([0, 0], RTT=True)) # COMPLETE
# print(Gates().NOT(1, RTT=True)) # COMPLETE
# print(Gates().OR([0, 0], RTT=True)) # COMPLETE
# print(Gates().NOR([0, 0], RTT=True)) # COMPLETE

gate = ""
A = ""
B = ""

def getInfo():
    inpu = input("Which Logic Gate do you want to test?\n Input 1 for AND \n Input 2 for NOT \n Input 3 for OR \n Input 4 for NOR \n Input 5 for NAND \n Input 6 for XOR \n")
    if inpu == str("1"):
        gate = Gates().AND    
    elif inpu == str("2"):
        gate = Gates().NOT
    elif inpu == str("3"):
        gate = Gates().OR
    elif inpu == str("4"):
        gate = Gates().NOR
    elif inpu == str("5"):
        gate = Gates().NAND
    elif inpu == str("6"):
        gate = Gates().XOR

    else:
        while inpu != str("1") or inpu != str("2") or inpu != str("3") or inpu != str("4"):
            inpu = input("INVALID INPUT, ALLOWED INPUTS ARE: 1, 2, 3, 4 \n Which Logic Gate do you want to test?\n Input 1 for AND \n Input 2 for NOT \n Input 3 for OR \n Input 4 for NOR \n Input 5 for NAND \n Input 6 for XOR \n")
            if inpu == str("1"):
                gate = Gates().AND
                break
            elif inpu == str("2"):
                gate = Gates().NOT
                break
            elif inpu == str("3"):
                gate = Gates().OR
                break
            elif inpu == str("4"):
                gate = Gates().NOR
                break
            elif inpu == str("5"):
                gate = Gates().NAND
                break
            elif inpu == str("6"):
                gate = Gates().XOR
                break

    inpt = input("Enter A and B values for chosen Gate\n A: ")

    if inpt == "1" or inpt == "0":
        A = int(inpt)
    else:
        while inpt != "0" or inpt != "1":
            inpt = input("INVALID INPUT, ALLOWED INPUTS ARE: 0, 1 \n Enter A and B values for chosen Gate\n A: ")
            if inpt == "1" or inpt == "0":
                A = int(inpt)
                break

    if gate.__name__ != "NOT":
        inpt2 = input("Enter A and B values for chosen Gate\n B: ")

        if inpt2 == "1" or inpt2 == "0":
            B = int(inpt2)
        else:
            while inpt2 != "0" or inpt2 != "1":
                inpt2 = input("INVALID INPUT, ALLOWED INPUTS ARE: 0, 1 \n Enter A and B values for chosen Gate\n B: ")
                if inpt == "1" or inpt == "0":
                    B = int(inpt2)
                    break
    else:
        print(gate(int(A), RTT=True))
        return exit()
    return gate([A, B], RTT=True)

