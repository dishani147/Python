tup = (10, 21, 4, 45, 66, 93, 1)
tup1=()
tup2=()
even_count, odd_count = 0, 0
for num in tup:
    if num % 2 == 0:
        list(tup1).append(num)
        even_count += 1       
    else:
        list(tup2).append(num)
        odd_count += 1
print("Even numbers in the list: ",even_count)
print("Odd numbers in the list: ",odd_count)
print(tup1)
print(tup2)
