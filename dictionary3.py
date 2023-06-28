dic = {}
n = int(input("Enter how many elements do you want:\n"))
print("Enter the elements:\n")
for i in range(0, n):
    roll = int(input())
    nm = input()
    cls = input()
    marks = input()
    stream = input()
    dic[roll] = [nm, cls, marks, stream]
    print(dic)
print("Enter any roll no. of which do you want to see the record:\n")
roll = int(input())
for r1 in dic:
    if (roll == r1):
        print(dic[roll])

