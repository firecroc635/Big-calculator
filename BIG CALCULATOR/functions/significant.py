from functions.repeating_lines import *

from math import log10, floor
def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)

def significant(whileLoopKiller):
    while whileLoopKiller:
        print('''
|1| Continue with calculation
|0| Go back
        ''')
        asker = input("pcik an option from above: ")
        match asker:
            case "1":
                number = float(input("enter your digit: "))
                x = int(input("enter the significant figure: "))
                roundedDigit = round_sig(number, x)
                print("rounded digit: ", roundedDigit)
                Formul = "rounded to SF " + str(x)

                resultSaver("significant", str(roundedDigit), "significant figure", Formul)
                return endMessage(whileLoopKiller)
            case "0":
                return(whileLoopKiller)
            case _:
                print("that ain't an option")


def significantAlways(a, b):
    while 1 == 1:
        roundedDigit = round_sig(a, b)
        print("rounded digit: ", roundedDigit)
        break