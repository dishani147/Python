# write a program to find out the maximum and minimum element of an list.
lst=[]
n=int(input("Enter how many numbers do you want to take"))
print(n)
for i in range (0,n):
    x=int(input("Enter the numbers"))
    lst.append(x)
print(lst)
maxx=lst[0]
for i in range(1,len(lst)):
    if (maxx<lst[i]):
        maxx=lst[i]
print("Tthe maximum number is:",maxx)
minn=lst[0]
for i in range (1,len(lst)):
    if (minn>lst[i]):
        minn=lst[i]
print("The minimum number is:"minn)
