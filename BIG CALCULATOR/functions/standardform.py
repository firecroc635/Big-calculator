from functions.repeating_lines import *

def standardForm(whileLoopKiller):
    while whileLoopKiller:
        print('''
|1| Generate standard form
|2| original number of standard form
|0| Go back
        ''')
        asker = input("pick from above: ")
        match asker:
            case "1":
                number = float(input("enter your number: "))
                number2 = number - int(number)
                yo = 0
                if number2 == 0:
                    while number > 10:
                        number = number / 10
                        yo += 1
                    result = str(number) + "* 10 power (" + str(yo) + ")"
                    print(number, "* 10power(", yo , ")")
                    resultSaver("Standard form", result, "standard form", "x * 10 power(n)")
                    return endMessage(whileLoopKiller)
                else:
                    while number - int(number) != 0:
                        number = number * 10
                        yo += 1
                    yo = yo - (yo * 2)
                    result = str(number) + "* 10 power (" + str(yo) + ")"
                    print(number, "* 10power(", yo, ")")
                    resultSaver("Standard form", str(result), "standard form", "x * 10 power(-n)")
                    return endMessage(whileLoopKiller)
            case "2":
                number = float(input("enter your number: "))
                powah = int(input("enter your power: "))
                number2 = number - int(number)
                if number2 == 0:
                    number = number / (10 ** powah)
                    print(number)
                    resultSaver("Standard form", str(number), "standard form", "x * 10 power(n)")
                    return endMessage(whileLoopKiller)
                else:
                    number = number * (10 ** powah)
                    print(number)
                    resultSaver("Standard form", str(number), "standard form", "x * 10 power(-n)")
                    return endMessage(whileLoopKiller)
            case "0":
                return(whileLoopKiller)
            case _:
                print("option not valid")