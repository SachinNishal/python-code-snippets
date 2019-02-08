def add(a, b):
    return a+b


def sub(a,  b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


a = int(input("Enter first No:"))
c = input("Select operation (+,-,*,/) :")
b = int(input("Enter second No:"))


if(c == "+"):
    print(add(a, b))
if(c == "-"):
    print(sub(a, b))
if(c == "*"):
    print(mul(a, b))
if(c == "/"):
    print(div(a, b))
