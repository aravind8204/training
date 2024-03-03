n=input("Enter a sentence: ").lower()
arr=n.split(' ')
for word in arr:
    if word==word[::-1]:
        print(word)