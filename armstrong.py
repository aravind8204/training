n=int(input("Enter a number "))
k=n
sum=0
while(n>0):
    digit=n%10
    sum+=digit**3
    n//=10
if(k==sum):
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")
