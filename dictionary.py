
#Tupple looks like a list but there are some difference see [pdf] 
T1=()
T2=()
T3=()
n=int(input("Enter how many numbers do you want :\n"))
print("Enter the elements :\n")
for i in range(0,n):
    x=int(input())
    T1=T1+(x,)
print(T1)
n=int(input("Enter how many numbers do you want :\n"))
print("Enter the elements :\n")
for i in range(0,n):
    y=int(input())
    T2=T2+(y,)
print(T2)
T3=(T1+T2)
print(T3)
    
