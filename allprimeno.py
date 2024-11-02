# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# List comprehension to find all prime numbers in the range
prime_numbers = [num for num in range(21) if is_prime(num)]
print("Prime numbers between 0 and 20:", prime_numbers)

