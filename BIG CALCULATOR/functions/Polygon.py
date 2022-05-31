from functions.repeating_lines import *

def SidesnAngles(whileLoopKiller):
    while whileLoopKiller:
        print('''
    |1| sum of angles
    |2| interior angles
    |3| exterior angles
    |0| Exit
        ''')
        aski = input("pick from the following above: ")
        match aski:
            case "1":
                n = float(input("enter your amount of sides: "))
                sumAngl = (n - 2)* 180
                interAngle = sumAngl / n
                exterAngle = 360 - interAngle
                print("sum of all angles ", round(sumAngl, 2))
                print("interior angle ", round(interAngle, 2))
                print("exterior angle ", round(exterAngle, 2))
                formul = '''
    n = sides
    j = sum of angles
    u = interior angle
    sum of angles: (n-2) * 180 = j
    interior angle: j / n = u
    exterior angle: 360 - u'''
                resultSaverPolygon("polygon",  str(round(sumAngl, 2)), str(round(interAngle, 2)), str(round(exterAngle, 2)), str(n), "sum of angles", formul)
                return endMessage(whileLoopKiller)
            case "2":
                while whileLoopKiller:
                    n = float(input("enter your interior angle: "))
                    if n > 180:
                        print("value too big")
                    else:
                        Sid = 360 / (180 - n)
                        exterAngle = 360 - n
                        sumAngl = (Sid - 2) * 180
                        print("side: ", round(Sid, 2))
                        print("sum of all angles: ", round(sumAngl, 2))
                        print("exterior angle: ", round(exterAngle, 2))
                        formul = '''
    n = sides
    j = sum of angles
    a = interior angle
    Sides: 360 / (180 - a): n
    sum of angles: (n-2) * 180 = j
    exterior angle: 360 - a'''
                        resultSaverPolygon("polygon",  str(round(sumAngl, 2)), str(round(n, 2)), str(round(exterAngle, 2)), str(int((Sid))), "Interior angles", formul)
                        return endMessage(whileLoopKiller)
            case "3":
                while whileLoopKiller:
                    n = float(input("enter your exterior angle: "))
                    if n > 360:
                        print("value too big")
                    else:
                        interAngle = 360 - n
                        Sid = 360 / (180 - interAngle)
                        sumAngl = (Sid - 2) * 180
                        print("side: ", round(Sid, 2))
                        print("sum of all angles: ", round(sumAngl, 2))
                        print("interior angle: ", round(interAngle, 2))
                        formul = '''
    n = sides
    j = sum of angles
    a = exterior angle
    Sides: 360 / (180 - a): n
    sum of angles: (n-2) * 180 = j
    Interior angle: 360 - a'''
                        resultSaverPolygon("polygon",  str(round(sumAngl, 2)), str(round(interAngle, 2)), str(round(n, 2)), str(int((Sid))), "Exterior angles", formul)
                        return endMessage(whileLoopKiller)
            case "0":
                return(whileLoopKiller)
            case _:
                print("not a valid option")