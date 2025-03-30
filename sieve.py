from math import sqrt

# Keep asking for input until a valid integer is provided
while True:
    try:
        n = int(input("Enter a number: "))
        if n < 2:
            print("Please enter a number greater than or equal to 2.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

# Create a list of numbers from 2 to n (potential prime candidates)
sieve_numbers = [i for i in range(2, n + 1)]

# Determine the range of numbers to check for multiples (up to sqrt(n))
sieve_basis = [j for j in range(2, int(sqrt(n)) + 1)]

# Filter out non-prime numbers by eliminating multiples of known primes
for p in sieve_basis:
    sieve_numbers = [x for x in sieve_numbers if x == p or x % p != 0]

# Print the numbers used for filtering (sieve basis)
print("Sieve Basis:", sieve_basis)

# Print the remaining prime numbers
print("Final Prime Numbers:", sieve_numbers)

            




