tracker = []
mixedFrac = []
topFrac = []
bottomFrac = []
operation = []
v = 1

#make a for loop that asks for an infinite amount of time until told to stop and then prints the steps on how it calculatoes, also use the tracker to know tf you're doing
while v <= 1:
    print('''
|1| mixed
|2| regular / irregular
|0| go back
    ''')
    aski = input()
    match aski:
        case "1":
            tracker.append(1)
            mix = float(input("enter your mix value: "))
            top = float(input("enter your top number: "))
            bot = float(input("enter your bottom number: "))
            mixedFrac.append(mix)
            topFrac.append(top)
            bottomFrac.append(bot)
            print(bottomFrac)
            while 1 == 1:
                print('''
        |1| plus
        |2| minus
        |3| times
        |4| Devide
        |5| nothing
                ''')
                asker = input("select from above: ")
                match asker:
                    case "1":
                        operation.append(1)
                        break
                    case "2":
                        operation.append(2)
                        break
                    case "3":
                        operation.append(3)
                        break
                    case "4":
                        operation.append(4)
                        break
                    case "5":
                        operation.append(5)
                        break
                    case _:
                        print("not an option")
            while 1 == 1:
                idno = input("would you like to continue? [y/n]").capitalize()
                if idno == "Y":
                    v -= 1
                    break
                    
                elif idno == "N":
                    v += 2
                    break
                else:
                    print("invalid answer")
        case "2":
            tracker.append(0)
            print()
        case "0":
            print()
            #return(whileLoopKiller)
        case _:
            print("not an option")
print("hello world!")
#extract the length of the fraction so it can check
if bottomFrac[0] == bottomFrac[1]:
    match operation[1]:
        case 1:
            if mixedFrac[0]:
                j = mixedFrac[0] * bottomFrac[0]
                topFrac = topFrac[0] + j
            elif mixedFrac[1]:
                k = mixedFrac[1] * bottomFrac[1]
                topFrac = topFrac[1] + k
            frac = topFrac[0] + topFrac[1]
            print(frac, "Over", bottomFrac)