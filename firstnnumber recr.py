def calc_num(num):
    if num == 0:
        return 0  # Base case should return 0
    return calc_num(num - 1) + 1  # Recursive case

# Example usage:
print(calc_num(5))  # Output: 5

