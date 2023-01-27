print("welcome to fabonachi series and factorial series")
input("please press enter to proceed")
series = input("type \"a\" for fabonachi and \"b\" for factorial: ")

def fabonachi(num):
    sum = 0
    for i in range(num):
        sum = sum + i
        print(sum)


def factorial(num):
    sum = 1
    for i in range(num):
        if i == 0:
            print("1")
        else:
            sum = sum* i
            print(sum)


limit = int(input("please enter a number limit: "))

if series=="a":
    fabonachi(limit)
elif series=="b":
    factorial(limit)
else:
    print("please type a valid value")