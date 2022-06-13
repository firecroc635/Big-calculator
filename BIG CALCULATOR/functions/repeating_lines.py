import os

def endMessage(whileLoopKiller):
    while whileLoopKiller:
        lo = input("would you like to calculate something else? [y/n]: ").capitalize()
        if not lo in ("Y", "N"):
            print("not a valid response")
        elif lo == "N":
            print("goobye")
            whileLoopKiller = False
            return whileLoopKiller
        else:
            return whileLoopKiller

def resultSaver(fileName, result, Operation, Formula):
    fileName = "BIG CALCULATOR\\functions\\Results\\" + fileName + ".txt"
    openFile = open(fileName, "a")
    openFile.writelines("[" + '\n')
    openFile.writelines("   Operation: " + Operation + '\n')
    openFile.writelines("   Formula used: " + Formula + '\n')
    openFile.writelines("   Result: " + result + '\n')
    openFile.writelines("]" + '\n')
    openFile.writelines('\n')
    openFile.writelines('\n')
    openFile.close()
    cwd = os.getcwd()
    print(format(cwd))

def resultSaverPolygon(fileName, sumAngl, interAngle, exterAngle, sid,  Operation, Formula):
    fileName = "BIG CALCULATOR\\functions\\Results\\" + fileName + ".txt"
    openFile = open(fileName, "a")
    openFile.write("[" + '\n')
    openFile.writelines("   Operation: " + Operation + '\n')
    openFile.writelines("   Formula used: " + Formula + '\n')
    openFile.writelines("   sum of Angles: " + sumAngl + '\n')
    openFile.writelines("   Interior Angle: " + interAngle + '\n')
    openFile.writelines("   Exterior Angle: " + exterAngle + '\n')
    openFile.writelines("   All sides: " + sid + '\n')
    openFile.write("]")
    openFile.writelines('\n')
    openFile.writelines('\n')
    openFile.close()
