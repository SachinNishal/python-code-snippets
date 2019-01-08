def collatz(number):
    if number % 2 == 0:                          #check even
        return (number // 2)
    elif number % 2 == 1:                        #check odd
        return (number * 3 + 1)
        
try:
    inputIn = int(input('Enter number: '))
except ValueError :
    print('Enter a valid integer !')
else:
    while collatz(inputIn) != 1:                 #calling collatz() until it returns 1
        print(collatz(inputIn))                  #print each value of collatz()
        inputIn = collatz(inputIn)               #assign new value of collatz() to inputIn

    print(collatz(inputIn))                      #print final value of collatz() ,this will be always equal to 1 