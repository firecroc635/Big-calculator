import math
from functions.repeating_lines import *
from functions.rightAngleTriangle import *
from functions.Polygon import *
from functions.significant import *
from functions.standardform import *
from functions.Mactorials import *
from functions.circly import *
from functions.Ares import *

#variables
instructionRepeater = 1
whileLoopKiller = True

#the first selection
while whileLoopKiller:
    if instructionRepeater:
        print('''
|1| Right angle Traingle calculator
|2| Regular Polygon calculator
|3| Extra...
|0| Exit
        ''')
    Doi = input("pick from the options above: ")

    match Doi:

#triangles are pretty cool ngl
        case "1":
            whileLoopKiller = triangle(whileLoopKiller)


#Regular polygons
        case "2":
            whileLoopKiller = SidesnAngles(whileLoopKiller)

#The extras
        case "3":
            while whileLoopKiller:
                print('''
    |1| Significant figures
    |2| Standard form
    |3| Factorial
    |4| Circles calculations
    |5| Area and perimeter of all shapes(including the ones in the options above)
    |6| Fractions
    |0| Go back to the first page
                ''')
                extraAsker = input("pick from the options above: ")
                match extraAsker:
                    case "1":
                        whileLoopKiller = significant(whileLoopKiller)
                    case "2":
                        whileLoopKiller = standardForm(whileLoopKiller)
                    case "3":
                        whileLoopKiller = Factorials(whileLoopKiller)
                    case "4":
                        whileLoopKiller = circles(whileLoopKiller)
                    case "5":
                        whileLoopKiller = ArenPerimeter(whileLoopKiller)
                    case "0":
                        break
                    case _:
                        print("not an option")

        case "0":
            break

#Filter
        case _:
            print("wrong selection")
