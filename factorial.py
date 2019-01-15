def factorial(inputValue):
    if(inputValue==0):
        return 1                                        #base case
    else:
        return inputValue*factorial(inputValue-1)       #recursive case

try:
    inputNumber=int(input("Enter a number : "))
    print(factorial(inputNumber))
except ValueError:
    print("Enter a integer !")