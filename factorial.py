def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n       #fact = fact * n
            n -= 1          #n = n - 1 
        return fact
 
# Driver Code
num = int(input("enter a number \n"))
print(f"Factorial of {num} is", factorial(num))