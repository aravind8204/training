n=int(input("Enter the size of the array: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a number: ")))
k=set(arr)
for l in k:
    print("count of",k,"is",arr.count(l))