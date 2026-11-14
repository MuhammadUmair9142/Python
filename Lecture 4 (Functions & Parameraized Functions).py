# Functions
#default function

# def text():
#     print("text function")

#call function
# text()

#parameraized function

# n=input("Enter Name: ")
# a=input("Enter Age: ")

# def intro(n,a):
#     # print("hello My name is ",n,"and i'm",a,"years old")
#     print(f"hello My name is {n} and i'm {a} years old")

# intro(n,a)


# a = int(input("Enter first Number: "))
# b = int(input("Enter second Number: "))
# opr = input("Enter your operator")

# def add(a,b):


#     return f"Result: {a+b}"

  
# print(add(a,b))


a = int(input("Enter first Number: "))
opr = input("Enter your operator ")
b = int(input("Enter second Number: "))

def calculate(a,b,opr):
    if opr == "+":
       print(a+b)
    elif opr == "-":
       print(a-b)
    elif opr == "*":
       print(a*b)
    elif opr == "/":
       print(a/b)
    else:
        print("unknown operator")

calculate(a,b,opr)


