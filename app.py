from os import stat
from GateClass import *

statement = ""
GU = []


for x in range(len(statement)):
    
    if statement.find("∧") != -1:
        GU.append("AND")
    elif statement.find("∨") != -1:
        GU.append

WHOLE = statement.split("(")[1].split(")")[0]

