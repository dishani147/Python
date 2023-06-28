def gcd(a,b):
    i=min(a,b)
    while i>0:
        if(a%i==0 & b%i==0):
            result = i
            break
        i-=1
    return result
a=int(input("Enter the number"))
b=int(input("Enter the number"))
print(f"GCD of {a} and {b} is {gcd(a,b)}")
