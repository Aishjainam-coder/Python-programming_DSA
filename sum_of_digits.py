def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # Add the last digit
        n //= 10         # Remove the last digit
    return total

# Example
number = 1234
print(sum_of_digits(number))  # Output: 10
