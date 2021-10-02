def fibo(n):
   if n <= 1:                            # Base Case
       return n
   else:
       return(fibo(n-1) + fibo(n-2))     # Recursive Case

terms = int(input("Enter number of terms : "))
if terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(terms):
       print(fibo(i))
      
