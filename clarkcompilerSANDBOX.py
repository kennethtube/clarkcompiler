import re
from collections import Counter
# CLARK COMPILER by kenneth

def initialize():
    print("\n+-------------------------------------------------+\n|                  CLARK COMPILER                 |\n+-------------------------------------------------+")
    raw()

def raw():
    global rData
    print("\n> Please input your raw data")
    rData=input(">>> ")
    rData=str(rData)
    print("\n> Raw data saved")
    main()

def main():
    req=input(">>> ")
    req=req.lower()
    if req=="item":print("blub")
###
    elif req=="findowner":findowner()
###
    elif req=="raw":raw()
    else:
        print("Invalid input.")
        main()

def findowner():
    print("test")

initialize()