n1=0
n2=1
n=int(input("Enter number of series : "))
print(n1)
print(n2)
for i in range(n-2):
    s=n1+n2
    n1=n2
    n2=s
    print(s)