def binarySearch(inList,value): 
    try:
        low=0
        high=len(inList)-1
        while inList[(low+high)//2] != value :
            if inList[(low+high)//2]>value:
                high=high-1
            if inList[(low+high)//2]<value: 
                low=low+1
        return((low+high)//2)
    except IndexError:
        return("Not Found !")        

a=list(map(str,input("Enter the list : ").split()))    #inList should be a sorted list.
b=input("Enter the value to search : ")
print(binarySearch(a,b))