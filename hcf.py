def find_hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
input_data = input("Enter the two numbers (format: 'a b'): ").split()
num1 = int(input_data[0])
num2 = int(input_data[1])

hcf = find_hcf(num1, num2)
print(hcf)
