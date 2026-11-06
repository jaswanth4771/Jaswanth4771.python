numbers = [2, 4, 6, 8, 10, 12]

# Extract even numbers
even_numbers = [n for n in numbers if n % 2 == 0]

# Calculate squares
squares = [n ** 2 for n in even_numbers]

# Extract squares greater than 100
result = [n for n in squares if n > 100]

print("Even numbers:", even_numbers)
print("Squares:", squares)
print("Squares greater than 100:", result)