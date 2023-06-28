dic={}
n=int(input("Enter how many number of employee do you want:"))
print("Enter the elements:")
for i in range (0,n):
    emp_id=int(input())
    name=input()
    dept=input()
    salary=int(input())
    dic[emp_id]=[name,dept,salary]
print(dic)
print("Enter the emp_id of which do you want to see the record:")
idd=int(input())
for emp_id in dic:
    if(idd==emp_id):
        print(dic[emp_id])
else:
    print("Employee not found")
