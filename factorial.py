def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
x=int(input("Enter the number"))
print("The result of factorial is:",fact(x))
