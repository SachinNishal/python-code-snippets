def factorial(inputValue):
    if(inputValue==1):
        return 1
    else:
        return inputValue*factorial(inputValue-1)    

_input=int(input("Enter a number : "))
print(factorial(_input))
