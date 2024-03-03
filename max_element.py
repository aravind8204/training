n=int(input("Enter the size of the array: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a number: ")))
arr.sort()
print("Biggest element in array is",arr[n-1])