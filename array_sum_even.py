n=int(input("Enter the size of the array: "))
arr=[]
sum=0
for i in range(n):
    arr.append(int(input("Enter a number: ")))
for num in arr:
    if num%2==0:
        sum+=num
print("The sum of the array is",sum)