lst=[]
n= int(input("Enter the number:"))
for i in range (0,n):
    print("Value is in index",i)
    x=int(input("Enter the number"))
    lst.append(x)
print(lst)
print("Sum of a list", sum(lst))