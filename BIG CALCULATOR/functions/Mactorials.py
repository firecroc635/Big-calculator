from functions.repeating_lines import *
def Factorials(whileLoopKiller):
    while whileLoopKiller:
        print('''
|1| Regular factorial
|2| Find source of factorial
|0| go back
''')
        asker = input("Select an option from above: ")
        match asker:
            case "1":
                factori = float(input("enter facotrial amount: "))
                y = 1
                x = 1
                while x <= factori:
                    y = y * x
                    x = x + 1
                print(y)
                resultSaver("Factorial", str(y), "factorial", "find factorial")
                return endMessage(whileLoopKiller)
            case "2":
                number = float(input("enter your factorial'd number: "))
                y = 1
                x = 1
                while y != number:
                    y = y * x
                    x = x + 1
                print("the factorial amount was: ", x - 1)
                resultSaver("Factorial", str(x), "source of factorial", "do a factorial until the source is found")
                return endMessage(whileLoopKiller)

            case "0":
                return(whileLoopKiller)
            case _:
                print("not a valid option")