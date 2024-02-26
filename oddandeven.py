n=int(input("Enter a number : "))
odd=0
o_a=[]
even=0
e_a=[]
while(n>0):
    rem=n%10
    if rem%2==0:
        e_a.append(rem)
        even+=1
    else:
        o_a.append(rem)
        odd+=1
    n=n//10
print("Odd Numbers : ")
for x in o_a:
    print(x,end=" ")
print("\ncount of odd numbers :",odd)
print("Even Numbers : ")
for x in e_a:
    print(x,end=" ")
print("\ncount of even numbers :",even)
