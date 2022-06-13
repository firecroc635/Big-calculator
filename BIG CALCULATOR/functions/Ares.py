from functions.repeating_lines import *
from functions.rightAngleTriangle import *
from functions.circly import *
import math

def ArenPerimeter(whileLoopKiller):
    while whileLoopKiller:
        print('''
|1| Perimeter
|2| Area
|3| 3d objects      
|0| Go back
        ''')
        ap = input("Pick from above yet again: ")
        match ap:
            case "1":
                print('''
        |1| Squares/rectangles
        |2| Right angle triangles
        |3| Other triangles
        |4| Rhombus
        |5| Kite
        |6| Trapezoid / Trapezium
        |7| circle
        |0| Go back           
                ''')
                asker = input("Pick from above: ")
                match asker:
                    case "1":
                        side = float(input("Enter the length of your side: "))
                        side2 = float(input("Enter the length of your side: "))
                        if side == side2:
                            side = round(side * 4, 2)
                            resultSaver("areas_and_perimeters", str(side), "perimeter for square", "a * 4")
                        else:
                            side = round(2*(side + side2), 2)
                            resultSaver("areas_and_perimeters", str(side), "perimeter for rectangle", "2(a + b)")
                            print(side)
                            resultSaver("areas_and_perimeters", str(side), "perimeter for square", "2(a + b)")
                        return endMessage(whileLoopKiller)
                    case "2":
                        whileLoopKiller = perimetertriangle(whileLoopKiller)
                    case "3":
                        a = float(input("Enter your a: "))
                        b = float(input("Enter your B: "))
                        c = float(input("Enter your C: "))
                        if a == b == c:
                            side = round(a * 3, 2)
                            resultSaver("areas_and_perimeters", str(side), "perimeter for equilateral triangle", "a * 3")
                        else:
                            side = round(a + b + c, 2)
                            resultSaver("areas_and_perimeters", str(side), "perimeter for some triangle", "a + b + c")
                        print("Perimeter", side)
                        return endMessage(whileLoopKiller)
                    case "4":
                        a = float(input("enter your side: "))
                        side = round(4 * a, 2)
                        print("perimeter: ", side)
                        resultSaver("areas_and_perimeters", str(side), "perimeter for Rhombus", "4a")
                        return endMessage(whileLoopKiller)
                    case "5":
                        a = float(input("enter your first side: "))
                        b = float(input("enter your second side: "))
                        side = round(2 *(a + b))
                        print("perimeter: ", side)
                        resultSaver("areas_and_perimeters", str(side), "perimeter for Kite", "2(a + b)")
                        return endMessage(whileLoopKiller)
                    case "6":
                        print("one by one enter your sides")
                        arry = []
                        for x in range(4):
                            x = float(input("enter your side: "))
                            arry.append(x)
                        side = round(arry[0] + arry[1] + arry[2] + arry[3], 2)
                        print("perimeter: ", side)
                        resultSaver("areas_and_perimeters", str(side), "perimeter for Trapezium", "a + b + c + d")
                        return endMessage(whileLoopKiller)
                    case "7":
                        c = circlesPeri(whileLoopKiller)
                    case "0":
                        return(whileLoopKiller)
                    case _:
                        print("not a valid option")


            case "2":
                print('''
        |1| Squares/rectangles
        |2| Right angle triangles
        |3| Other triangles
        |4| Rhombus / kite
        |5| Trapezoid / Trapezium
        |6| Parallelogram
        |7| circle
        |0| Go back           
                ''')
                asker = input("Pick from above: ")
                match asker:
                    case "1":
                        side = float(input("Enter your length of one side: "))
                        side2 = float(input("Enter your length of the 2nd side: "))
                        if side == side2:
                            side = round(side ** 2, 2)
                            resultSaver("areas_and_perimeters", str(side), "area for square", "a^2")
                        else:
                            side = round(side * side2, 2)
                            resultSaver("areas_and_perimeters", str(side), "area for rectangle", "a * b")
                        print("Area =", side)
                            
                        return endMessage(whileLoopKiller)


                    case "2":
                        b = areatriangle(whileLoopKiller)


                    case "3":
                        while 1 == 1:
                            print('''
                |1| Equilateral with side
                |2| Equilateral with height
                |3| some other
                            
                            ''')
                            aski = input("select from above: ")
                            match aski:
                                case "1":
                                    a = float(input("enter your side: "))
                                    side = round((math.sqrt(3) * a) / 2, 2)
                                    print("area: ", side)
                                    resultSaver("areas_and_perimeters", str(side), "area for equilateral triangle", "sqrt(3) * a/2")
                                    return endMessage(whileLoopKiller)

                                case "2":
                                    height = float(input("enter your height: "))
                                    side = round((2 * height) / math.sqrt(3), 2)
                                    print("area: ", side)
                                    resultSaver("areas_and_perimeters", str(side), "area for equilateral triangle", "2 * a/sqrt(3)")
                                    return endMessage(whileLoopKiller)

                                case "3":
                                    base = float(input("enter your base: "))
                                    height = float(input("enter your height: "))
                                    side = round((base * height) / 2, 2)
                                    print("area: ", side)
                                    resultSaver("areas_and_perimeters", str(side), "area for triangle", "base * height * 1/2")
                                    return endMessage(whileLoopKiller)
                                case "0":
                                    break
                                case _:
                                    print("not a valid option")
                    case "4":
                        p = float(input("enter your horizontal side: "))
                        q = float(input("enter your vertical side: "))
                        side = round((p * q)/ 2, 2)
                        print("area: ", side)
                        resultSaver("areas_and_perimeters", str(side), "area for Rhobus", "pq / 2")
                        return endMessage(whileLoopKiller)
                    case "5":
                        b1 = float(input("enter your top horizontal value: "))
                        b2 = float(input("enter your bottom horizontal value: "))
                        h = float(input("enter your height: "))
                        side = round(((b1 + b2) / 2) * h, 2)
                        resultSaver("areas_and_perimeters", str(side), "area for Trapezium", "((b1 + b2) / 2) * h")
                        return endMessage(whileLoopKiller)
                    case "6":
                        b = float(input("enter your base: "))
                        h = float(input("enter your height: "))
                        side = round(b * h, 2)
                        resultSaver("areas_and_perimeters", str(side), "area for Parallelogram", "bh")
                        return endMessage(whileLoopKiller)
                    case "7":
                        a = circlesArea(whileLoopKiller)

            case "3":
                print("didn't make it yet wait!!")

            case "0":
                return(whileLoopKiller)
            case _:
                print("not an option")