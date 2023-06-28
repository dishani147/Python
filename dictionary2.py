dic={}
n=int(input("Enter how many elements do you want:\n"))
print(n)
for i in range(0,n):
    roll=int(input())
    nm=input()
    clas=input()
    marks=int(input())
    
    stream=input()
    dic[roll]=[nm,clas,marks,stream]
print(dic)
print("Enter any roll no of which do you want to see the record:\n")
rl=int(input())
for roll in dic:
     if(roll==rl):
        print(dic[roll][2])
        
          
