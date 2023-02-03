import random

def generate_lottery_numbers(num_numbers, lower_bound, upper_bound):
  # Initialize an empty list to store the numbers
  numbers = []

  # Generate the desired number of numbers
  for i in range(num_numbers):
    # Generate a random number
    number = random.randint(lower_bound, upper_bound)

    # Make sure the number has not already been chosen
    while number in numbers:
      number = random.randint(lower_bound, upper_bound)

    # Add the unique number to the list
    numbers.append(number)

  return numbers

# Example usage: generate 7 lottery numbers between 1 and 49
lottery_numbers = generate_lottery_numbers(5, 1, 49)
starts = generate_lottery_numbers (2,1,10)
print(lottery_numbers,  starts)
