a=int(input("Enter Value of A : "))
b=int(input("Enter Value of B : "))
c=int(input("Enter Value of C : "))
if a<b:
    if a<c:
        print(a,"is smaller")
    else:
        print(c,"is smaller")
else:
    if b<c:
        print(b,"is smaller")
    else:
        print(c,"is smaller")