tup=()
s=0
n= int(input("Enter how many numbers do you want to take"))
print("Enter the number",n)
for i in range(0,n):
    x=int(input())
    tup=tup+(x,)
print(tup)
for i in range(0,n):
    if(tup[i]%2==0):
        s=s+tup[i]
print(s)
