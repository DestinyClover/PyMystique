lst=eval(input("enter list"))
search= int(input("enter number to be searched"))
for i in range(len(lst)):
    if lst[i]==search:
        print("position of given number is",i+1)
        break
else:
    print("not found")
