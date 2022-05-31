from functions.significant import *
from functions.repeating_lines import *
import math

def triangle(whileLoopKiller):
    while whileLoopKiller:
        print()
        print("What kind of right triangle calculations would you like to perform?")
        print('''
        |1| Perimeter
        |2| Area
        |3| pythagora's calculations
        |4| Find angle via leg_a and leg_b
        |0| exit
                    ''')
        asker = input("which of these would you like to perform: ")
        match asker:
                #Perimeter
            case "1":
                while whileLoopKiller:
                    print('''
            |1| calculate with all Hypotenus and both legs
            |2| Calculate with only 2 legs
            |3| calculate with only a leg
            |4| calculate with hypotenus and a leg
            |5| calculate with only the hypotenus
            |0| go back
                                ''')
                    aski = input("pick from the following above: ")
                    match aski:
                        case "1":
                            hypo = float(input("input your hypotenus: "))
                            leg_a = float(input("input your a: "))
                            leg_b = float(input("input your b: "))
                            print(round(hypo + leg_a + leg_b, 2))

                            resultSaver("Right angle triangle", str(round(hypo + leg_a + leg_b, 2)), "Right angle triangle perimeter", "Hypotenus + leg_a + leg_b = p")
                            return endMessage(whileLoopKiller)
                        case "2":
                            leg_a = float(input("what's your a: "))
                            leg_b = float(input("what's your b: "))
                            pyth =  math.sqrt((leg_a ** 2) + (leg_b ** 2))
                            print("hypotenus =", pyth)
                            print(round(pyth + leg_a + leg_b,2))

                            resultSaver("Right angle triangle", str(round(pyth + leg_a + leg_b, 2)), "Right angle triangle perimeter without hypotenus", "sqrt(sqaure(leg_a) + square(leg_b)) = hypotenus + leg_a + leg_b = p")
                            return endMessage(whileLoopKiller)
                        case "3":
                            leg_a = float(input("what's your number: "))
                            pyth = math.sqrt((leg_a ** 2) + (leg_a ** 2))
                            print("hypotenus =", pyth)
                            print(round(pyth + leg_a + leg_a,2))

                            resultSaver("Right angle triangle", str(round(pyth + leg_a + leg_a, 2)), "Right angle triangle perimeter with only one leg", "sqrt(sqaure(leg_a) + square(leg_a)) = hypotenus + (leg_a * 2)")
                            return endMessage(whileLoopKiller)
                        case "4":
                            hypo = float(input("what's your hypotenus: "))
                            leg_a = float(input("what's your a: "))
                            c = math.sqrt(float((hypo ** 2) - (leg_a ** 2)))
                            print(round(leg_a + hypo + c,2))

                            resultSaver("Right angle triangle", str(round(pyth + leg_a + c, 2)), "Right angle triangle perimeter with hypotenus and one leg", "sqrt(sqaure(hypotenus) - square(leg_a)) = leg_b + leg_a + hypotenus")
                            return endMessage(whileLoopKiller)
                        case "5":
                            hypo = float(input("what's your hypo: "))
                            legs = math.sqrt((hypo ** 2) / 2)
                            print("a and b =", legs)
                            print(round(legs + legs + hypo,2))

                            resultSaver("Right angle triangle", str(round(pyth + legs + legs, 2)), "Right angle triangle perimeter with hypotenus and one leg", "sqrt(sqaure(hypotenus) - square(leg_a)) = leg_b + leg_a + hypotenus")
                            return endMessage(whileLoopKiller)

                        case "0":
                            break
                        case _:
                            print("that's not an option")
            case "2":
                while whileLoopKiller:
                    print('''
            |1| Calculate with only 2 legs
            |2| calculate with only a leg
            |3| calculate with hypotenus and a leg
            |4| calculate with only the hypotenus
            |0| go back
                                ''')
                    aski = input("pick from the following above: ")
                    match aski:
                        case "1":
                            leg_a = float(input("enter your a: "))
                            leg_b = float(input("enter your b: "))
                            area = (leg_a * leg_b) / 2
                            hypo = math.sqrt((leg_a ** 2) + (leg_b ** 2))
                            print("area =", round(area,2))
                            print("hypotenus =", round(hypo,2))
                            form = '''
   leg_a * leg_b
   _____________  = A
         2
         '''

                            resultSaver("Right angle triangle", str(round((leg_a * leg_b) / 2)), "Right angle triangle area", form)
                            return endMessage(whileLoopKiller)
                        case "2":
                            leg_a = float(input("what's your a: "))
                            area = (leg_a ** 2) / 2
                            hypo = math.sqrt((leg_a ** 2) + (leg_a ** 2))
                            print("area =", area)
                            print("hypotenus =", round(hypo,2))
                            form = '''
    leg_a²
   ________  = A
       2
       '''
                            resultSaver("Right angle triangle", str(round((leg_a ** 2) / 2)), "Right angle triangle area with only one leg", form)
                            return endMessage(whileLoopKiller)
                        case "3":
                            hypo = float(input("what's your hypotenus: "))
                            leg_a = float(input("what's your a: "))
                            leg_b = math.sqrt((hypo ** 2) - (leg_a ** 2))
                            area = (leg_a * leg_b) / 2
                            print("leg b =", round(leg_b, 2))
                            print("area =", round(area))
                            form = '''
    sqrt(hypo² - leg_a²) = leg_b

    leg_a * leg_b
   _______________  = A
          2
          '''
                            
                            resultSaver("Right angle triangle", str(round((leg_a * leg_b) / 2)), "Right angle triangle area with hypotenus and one leg", form)
                            return endMessage(whileLoopKiller)
                        case "4":
                            hypo = float(input("what's your input: "))
                            legs = math.sqrt((hypo ** 2) / 2)
                            area = (legs ** 2) / 2
                            print("a and b =", round(legs,2))
                            print("area =", round(area,2))
                            form = '''
          _                 _
         | square(hypotenus) |
    sqrt | _________________ | = leg_a
         |         2         |
         |_                 _|

    square(leg_a)
   ______________  = A
          2
          '''

                            resultSaver("Right angle triangle", str(round((legs ** 2) / 2)), "Right angle triangle area with hypotenus and one leg", form)
                            return endMessage(whileLoopKiller)
                        case "0":
                            break
                        case _:
                            print("that's not an option")
                        
            case "3":
                while whileLoopKiller:
                    print('''
            |1| Calculate with only 2 legs
            |2| calculate with only a leg
            |3| calculate with hypotenus and a leg
            |4| calculate with only the hypotenus
            |0| go back''')
                    aski = input("pcik from the following above: ")
                    match aski:
                        case "1":
                            leg_a = float(input("what's your a: "))
                            leg_b = float(input("what's your b: "))
                            hypo = math.sqrt((leg_a ** 2) + (leg_b ** 2))
                            print("hypotenus =", round(hypo,2))

                            resultSaver("Right angle triangle", str(round(math.sqrt((leg_a ** 2) + (leg_b ** 2)))), "Right angle triangle pythagora's", "sqrt(square(leg_a) + square(leg_b)) = hypotenus")
                            return endMessage(whileLoopKiller)
                        case "2":
                            leg_a = float(input("what's your a: "))
                            hypo = math.sqrt((leg_a ** 2) + (leg_a ** 2))
                            print("hypotenus =", round(hypo,2))

                            resultSaver("Right angle triangle", str(round( math.sqrt((leg_a ** 2) + (leg_a ** 2)))), "Right angle triangle pythagora's with one leg", "sqrt(square(leg_a) + square(leg_a)) = hypotenus")
                            return endMessage(whileLoopKiller)
                        case "3":
                            hypo = float(input("enter your hypotenus: "))
                            leg_a = float(input("enter your a: "))
                            leg_b = math.sqrt((hypo ** 2) - (leg_a ** 2))
                            print("leg b =", round(leg_b,2))

                            resultSaver("Right angle triangle", str(round(  math.sqrt((hypo ** 2) - (leg_a ** 2)))), "Right angle triangle pythagora's with hypotenus and only one leg", "sqrt(square(hypotenus) - square(leg_a)) = leg_b")
                            return endMessage(whileLoopKiller)
                        case "4":
                            hypo = float(input("what's your hypotenus: "))
                            legs = math.sqrt((hypo ** 2)/2)
                            print("legs =", round(legs,2))
                            form = '''
          _                 _
         | square(hypotenus) |
    sqrt | _________________ | = leg_a
         |         2         |
         |_                 _|
         '''

                            resultSaver("Right angle triangle", str(round(math.sqrt((hypo ** 2)/2))), "Right angle triangle pythagora's with only hypotenus", form)
                            return endMessage(whileLoopKiller)
                        case "0":
                            break
                        case _:
                            print("that's not a selections")
            case "4":
                while whileLoopKiller:
                    print('''
            |1| Calculate with only 2 legs
            |2| calculate with only a leg
            |3| calculate with hypotenus and a leg
            |4| calculate with only the hypotenus
            |0| go back''')
                    aski = input("pcik from the following above: ")
                    match aski:
                        case "1":
                            leg_a = float(input("enter your a: "))
                            leg_b = float(input("enter your b: "))
                            hypo = math.sqrt((leg_a ** 2) + (leg_b ** 2))
                            alphadee = math.acos(leg_a / hypo) * 180 / math.pi
                            betadee = math.acos(leg_b / hypo) * 180 / math.pi
                            print("angle alpha ", round(alphadee,2), " angle beta ", round(betadee,2))
                            dwayne = "angle alpha ", str(round(alphadee,2)), " angle beta ", str(round(betadee,2))

                            resultSaver("Right angle triangle", str(dwayne), "Right angle triangle angle finder", "[put later]")
                            return endMessage(whileLoopKiller)
                        case "2":
                            leg_a = float(input("enter your leg: "))
                            hypo = math.sqrt((leg_a ** 2) + (leg_a ** 2))
                            alphadee = math.acos(leg_a / hypo) * 180 / math.pi
                            betadee = math.acos(leg_a / hypo) * 180 / math.pi
                            print("hypotenus", hypo)
                            print("angle alpha ", round(alphadee,2), " angle beta ", round(betadee,2))
                            dwayne = "angle alpha " + str(round(alphadee,2)) + " angle beta " + str(round(betadee,2))

                            resultSaver("Right angle triangle", str(dwayne), "Right angle triangle angle finder without hypotenus", "[put later]")
                            return endMessage(whileLoopKiller)
                        case "3":
                            hypo = float(input("enter your hypotenus: "))
                            leg_a = float(input("enter your leg: "))
                            leg_b = math.sqrt((hypo ** 2) - (leg_a ** 2))
                            print("leg_b", leg_b)
                            alphadee = math.acos(leg_a / hypo) * 180 / math.pi
                            betadee = math.acos(leg_b / hypo) * 180 / math.pi
                            print("angle alpha ", round(alphadee,2), " angle beta ", round(betadee,2))
                            dwayne = "angle alpha ", str(round(alphadee,2)), " angle beta ", str(round(betadee,2))

                            resultSaver("Right angle triangle", str(dwayne), "Right angle triangle angle finder with hypotenus and one leg", "[put later]")
                            return endMessage(whileLoopKiller)
                        case"4":
                            hypo = float(input("enter your hypotenus: "))
                            legs = math.sqrt((hypo ** 2) / 2)
                            alphadee = math.acos(legs / hypo) * 180 / math.pi
                            betadee = math.acos(legs / hypo) * 180 / math.pi
                            print("legs: ", legs)
                            print("angle alpha ", round(alphadee,2), " angle beta ", round(betadee,2))
                            dwayne = "angle alpha ", str(round(alphadee,2)), " angle beta ", str(round(betadee,2))

                            resultSaver("Right angle triangle", dwayne, "Right angle triangle angle finder with only hypotenus", "[put later]")
                            return endMessage(whileLoopKiller) 
                        case"0":
                            break
                        case _:
                            print("not a valid option")

            case "0":
                return(whileLoopKiller)

            case _:
                print("that's not an option")