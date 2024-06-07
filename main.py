import random


def is_armstrong(n):
    """
    Returns True if n is an Armstrong number, False otherwise
    """
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(d) ** num_digits for d in num_str)
    return sum_of_powers == n

# Test the function
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is not an Armstrong number.")

 #Example usage:
# Enter a number: 370
 #370 is an Armstrong number!
