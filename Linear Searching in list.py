def search(Temp, n):
    for i in range(0,len(Temp)):
        if Temp[i] == n:
            return True
    return False
Temp=[]
n=int(input("Enter how many numbers do you want to input:\n"))
for i in range(0,n):
    x = int(input())
    Temp.append(x)
    print(Temp)
m = int(input("Ente the value :\t"))
if search(0,n):
    print("Found")
else:
    print("Not Found")
    
