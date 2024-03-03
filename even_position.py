n=int(input("Enter the size of the array: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a number: ")))
for i in range(0,n,2):
    print(arr[i])
