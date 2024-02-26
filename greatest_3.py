a=int(input("Enter Value of A : "))
b=int(input("Enter Value of B : "))
c=int(input("Enter Value of C : "))
if a>b:
    if a>c:
        print(a,"is greater")
    else:
        print(c,"is greater")
else:
    if b>c:
        print(b,"is greater")
    else:
        print(c,"is greater")