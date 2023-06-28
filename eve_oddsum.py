maximum = int (input("Please enter the maximum value:\n"))
s1=0
s2=0
for number in range(1, maximum+1):
    if(number % 2 == 0):
        s1 = s1+number
    else:
        s2 = s2+number

print("The sum of even numbers from 1 to {0} = {1}".format(number,s1))
print("the sum of odd numbers from 1 to {0} = {1}".format(number,s2))
