aa = open("alakh exercise.txt")
bb = open("alakh food.txt")
cc = open("mouj exercise.txt")
dd = open("mouj food.txt")
ee = open("arsh exercise.txt")
ff = open("arsh food.txt")

line1= aa.readline()
line2=bb.readline()
line3=cc.readline()
line4=dd.readline()
line5=ee.readline()
line6=ff.readline()
while(True):
    print("welcome to health management system of alakh babbar...".upper())
    lock_and_retrieve = input("choose one of the options\nlock\nretrieve\nchoose: ")
    choose_the_person = input("enter your name: ")
    ex_or_food = input("enter what you want to check\nexercise\nfood\nchoose: ")
    if lock_and_retrieve=="retrieve":
        if choose_the_person=="alakh" and ex_or_food=="exercise":
            line1= line1 + aa.readline()
        elif choose_the_person=="alakh" and ex_or_food=="food":
            line2= line2 + bb.readline()
        elif choose_the_person=="mouj" and ex_or_food=="exercise":
            line3= line3 + cc.readline()
        elif choose_the_person=="mouj" and ex_or_food=="food":
            line4= line4 + dd.readline()
        elif choose_the_person=="arsh" and ex_or_food=="exercise":
            line5= line5 + ee.readline()
        elif choose_the_person=="arsh" and ex_or_food=="food":
            line6= line6 + ff.readline()
        else:
            print("something went wrong...")
    else:
        pass
# making functions

    def lock(a, b):
        """function for getting complete content of the person"""
        if a=="alakh" and b=="exercise":
            x = open("alakh exercise.txt", "a")
            x.write("\n")
            x.write(input("add here: "))
        elif a=="alakh" and b=="food":
            x = open("alakh food.txt", "a")
            x.write("\n")
            x.write(input("add here: "))
        elif a=="mouj" and b=="exercise":
            x = open("mouj exercise.txt", "a")
            x.write("\n")
            x.write(input("add here: "))
        elif a=="mouj" and b=="food":
            x = open("mouj food.txt", "a")
            x.write("\n")
            x.write(input("add here: "))
        elif a=="arsh" and b=="exercise":
            x = open("arsh exercise.txt", "a")
            x.write("\n")
            x.write(input("add here: "))
        elif a=="arsh" and b=="food":
            x = open("arsh food.txt", "a")
            x.write("\n")
            x.write(input("add here: "))
        else:
            print("something went wrong please try again...")
        return lock

    def retrieve(a, b):
        """function for retrieve"""
        if choose_the_person=="alakh" and ex_or_food=="exercise":
            aab=[line1]
            for line in aab:
                print(line)
        elif choose_the_person=="alakh" and ex_or_food=="food":
            bbb=[line2]
            for line in bbb:
                print(line)
        elif choose_the_person=="mouj" and ex_or_food=="exercise":
            ccb=[line3]
            for line in ccb:
                print(line)
        elif choose_the_person=="mouj" and ex_or_food=="food":
            ddb=[line4]
            for line in ddb:
                print(line)
        elif choose_the_person=="arsh" and ex_or_food=="exercise":
            eeb=[line5]
            for line in eeb:
                print(line)
        elif choose_the_person=="arsh" and ex_or_food=="food":
            ffb=[line6]
            for line in ffb:
                print(line)
        else:
            print("something went wrong...")


    def getdate():
        """function for get time and date"""
        import datetime
        return datetime.datetime.now()

# main program starts

    if lock_and_retrieve=="lock":
        print(getdate(), lock(choose_the_person, ex_or_food))
        foragain = input("do you want to try again or quit\nif yes type \"y\" and if no type \"n\"")
        if foragain=="y":
            continue
        else:
            print("thanks for using our service")
            break
    elif lock_and_retrieve=="retrieve":
        print(getdate(), retrieve(choose_the_person, ex_or_food))
        foragain = input("do you want to try again or quit\nif yes type \"y\" and if no type \"n\"")
        if foragain == "y":
            continue
        else:
            print("thanks for using our service")
            break
    else:
        print("something went wrong, try again..")
        foragain = input("do you want to try again or quit\nif yes type \"y\" and if no type \"n\"")
        if foragain == "y":
            continue
        else:
            print("thanks for using our service")
            break

aa.close()
bb.close()
cc.close()
dd.close()
ee.close()
ff.close()

