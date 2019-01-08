inList = list(map(str, input("Enter String : ").split()))  #get input and map space seperated values into a list of string type
for item in inList:
    print(item.capitalize(), end=" ")