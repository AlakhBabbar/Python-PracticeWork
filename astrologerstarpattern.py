print("welcome to astrologer stars pattern")
print("give a number so that we can calculate your stars")
rows = int(input("enter number here: "))
truefalse = input("choose 0 for true and 1 for false: ")
a = "*"
while True:
    if truefalse == "0" and len(a) <= rows:
        print(a)
        a = a + "*"
        continue
    elif truefalse == "1" and len(a) > 0:
        a = "*"
        a = rows*a
        print(a)
        rows = rows - 1
        continue

    break

print("thank you for using our service!")





