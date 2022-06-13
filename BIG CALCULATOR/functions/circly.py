import math
from functions.repeating_lines import *

def circles(whileLoopKiller):
    while whileLoopKiller:
        print('''
        |1| Area calculator
        |2| Circumfrence calculator
        |3| Arc area calculator
        |4| Arc calculator
        |5| Radius finder with area
        |6| Radius finder with circumfrence
        |0| Go back
        ''')
        asker = input("pick from above: ")
        match asker:
            case "1":
                radius = float(input("enter your radius: "))
                area = round(math.pi * (radius ** 2), 2)
                print("Area: ", area)
                resultSaver("Circles", str(area), "Area of circle", "pi * squared(r)")
                return endMessage(whileLoopKiller)
            case "2":
                diameter = float(input("enter your diameter: "))
                circumfrence = round(math.pi * diameter, 2)
                print("circumfrence: ", circumfrence)
                resultSaver("Circles", str(circumfrence), "Circumfrence of circle", "pi * D")
                return endMessage(whileLoopKiller)
            case "3":
                radius = float(input("enter your radius: "))
                angle = float(input("enter your angle: "))
                area = round((angle / 360) * math.pi * (radius ** 2), 2)
                print("Area of arc:", area)
                resultSaver("Circles", str(area), "Area of arc", "a/360 * pi * squared(r)")
                return endMessage(whileLoopKiller)
            case "4":
                diameter = float(input("enter diameter: " ))
                angle = float(input("enter your angle: "))
                arc = round((angle / 360) * math.pi * diameter, 2)
                perimeter = arc + (diameter / 2) + (diameter / 2)
                print("arc: ", arc, "Perimeter: ", perimeter)
                ski = "arc: " + str(arc) + "Perimeter: " + str(perimeter)
                form = '''
    arc = a/360 * pi * r
    perimeter = arc + radius + radius'''
                resultSaver("Circles", ski, "Finding arc", form)
                return endMessage(whileLoopKiller)
            case "5":
                area = float(input("enter your area: "))
                radius = round(math.sqrt(area / math.pi), 2)
                diameter = round(math.sqrt(area / math.pi) * 2, 2)
                ski = "radius: " + str(radius) + " diameter: " + str(diameter)
                print(ski)
                form = '''
    radius = sqrt(area / pi)
    perimeter = sqrt(area / pi) * 2'''
                resultSaver("Circles", ski, "radius finder via area", form)
                return endMessage(whileLoopKiller)
            case "6":
                circumfrence = float(input("enter your circumfrence: "))
                radius = round(circumfrence / math.pi, 2)
                diameter = round(circumfrence / math.pi * 2, 2)
                ski = "radius: " + str(radius) + " diameter: " + str(diameter)
                form = '''
    radius = sqrt(area / pi)
    perimeter = sqrt(area / pi) * 2'''
                print(ski)
                resultSaver("Circles", ski, "radius finder via circumfrence", form)
                return endMessage(whileLoopKiller)
            case "0":
                return(whileLoopKiller)
            case _:
                print("not a valid option")
def circlesArea(whileLoopKiller):
    while whileLoopKiller:
        print('''
        |1| Circle area
        |2| Arc area
        |0| Go back
        ''')
        aski = input("select from above")
        match aski:
            case "1":
                radius = float(input("enter your radius: "))
                area = round(math.pi * (radius ** 2), 2)
                print("Area: ", area)
                resultSaver("Circles", str(area), "Area of circle", "pi * squared(r)")
                return endMessage(whileLoopKiller)
            case "2":
                diameter = float(input("enter diameter: " ))
                angle = float(input("enter your angle: "))
                arc = round((angle / 360) * math.pi * diameter, 2)
                perimeter = arc + (diameter / 2) + (diameter / 2)
                print("arc: ", arc, "Perimeter: ", perimeter)
                ski = "arc: " + str(arc) + "Perimeter: " + str(perimeter)
                form = '''
    arc = a/360 * pi * r
    perimeter = arc + radius + radius'''
                resultSaver("Circles", ski, "Finding arc", form)
                return endMessage(whileLoopKiller)
            case "0":
                return(whileLoopKiller)
            case _:
                print("not a valid option")
def circlesPeri(whileLoopKiller):
    while whileLoopKiller:
        print('''
    |1| Circumfrence calculator
    |2| Arc circumfrence 
    |0| Go back   
        ''')
        aski = input("select from above: ")
        match aski:
            case "1":
                diameter = float(input("enter your diameter: "))
                circumfrence = round(math.pi * diameter, 2)
                print("circumfrence: ", circumfrence)
                resultSaver("Circles", str(circumfrence), "Circumfrence of circle", "pi * D")
                return endMessage(whileLoopKiller)
            case "2":
                diameter = float(input("enter diameter: " ))
                angle = float(input("enter your angle: "))
                arc = round((angle / 360) * math.pi * diameter, 2)
                perimeter = arc + (diameter / 2) + (diameter / 2)
                print("arc: ", arc, "Perimeter: ", perimeter)
                ski = "arc: " + str(arc) + "Perimeter: " + str(perimeter)
                form = '''
    arc = a/360 * pi * r
    perimeter = arc + radius + radius'''
                resultSaver("Circles", ski, "Finding arc", form)
                return endMessage(whileLoopKiller)
            case "0":
                return(whileLoopKiller)
            case _:
                print("not a valid option")