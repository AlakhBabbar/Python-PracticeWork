print("welcome to fabonachi series and factorial series")
input("please press enter to proceed")
series = input("type \"a\" for fibonacci and \"b\" for factorial: ")

def fibonacci(num):
    sum = 0
    for i in range(num+1):
        sum = sum + i
        print(sum)


def factorial(num):
    product = 1
    for i in range(num+1):
        if i == 0:
            print("1")
        else:
            product = product* i
            print(product)


limit = int(input("Please enter a number limit: "))

if series=="a":
    fibonacci(limit)
elif series=="b":
    factorial(limit)
else:
    print("Please type a valid value")
