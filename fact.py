n=int(input("Enter a number : "))
k=n
mul=1
while(n>0):
    mul*=n
    n=n-1
print("Factorial of",k," is",mul)