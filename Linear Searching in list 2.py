
def search(Temp, n):
    for i in range(len(Temp)):
        if Temp[i] == n:
            return True
    return False
Temp = (1, 2, 'A', 4, 'b', 6)
n = "b"
if search(Temp, n):
    print("Found")
else:
    print("Not Found")
