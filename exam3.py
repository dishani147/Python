def distribute_apples(num_apples, min_weight, max_weight, target_weight):
    total_weight = num_apples * (min_weight + max_weight)
    return total_weight % 2 == 0 and min_weight <= target_weight <= max_weight

num_apples, min_weight, max_weight, target_weight = map(int, input("Enter the number of apples, minimum weight, maximum weight, and target weight: ").split())

if distribute_apples(num_apples, min_weight, max_weight, target_weight):
    print("Yes, it is possible to distribute the apples equally.")
else:
    print("No, it is not possible to distribute the apples equally.")
 
