# 1.Fibonacci Sequence: Write a program that generates the Fibonacci sequence up to the nth term 
# (where n is a positive integer input by the user) using a loop.
# Function to generate Fibonacci sequence up to nth term
def fibonacci_sequence(n):
    # Starting values for the first two terms
     fib_sequence = [0, 1]
    
     # Generate the Fibonacci sequence up to n terms
     for i in range(2, n):
         next_term = fib_sequence[i-1] + fib_sequence[i-2]
         fib_sequence.append(next_term)
    
     return fib_sequence[:n]  # Slice the list to return only the first n terms

 # Input from the user
n = int(input("Enter the number of terms for the Fibonacci sequence: "))

 # Check if the input is a positive integer
if n <= 0:
     print("Please enter a positive integer.")
else:
     # Generate and print the Fibonacci sequence
     result = fibonacci_sequence(n)
     print("Fibonacci sequence up to", n, "terms:", result)

# 2. Prime Numbers: Create a function that prints all prime numbers between 1 and 100 using a loop. 
# A prime number is a number that is only divisible by 1 and itself. 
# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # Only check up to the square root of the number
        if num % i == 0:
            return False
    return True

# Function to print all prime numbers between 1 and 100
def print_primes():
    print("Prime numbers between 1 and 100 are:")
    for num in range(1, 101):
        if is_prime(num):
            print(num, end=" ")  # Print prime numbers on the same line

# Call the function
print_primes()


# 3.Character Count: Create a program that counts the occurrences of each character in a given string using a loop and
#  prints the results in a dictionary format.
# Function to count occurrences of each character in a string
def character_count(input_string):
    char_count = {}  # Dictionary to store character counts
    
    # Loop through each character in the string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        else:
            # If it's not in the dictionary, add it with a count of 1
            char_count[char] = 1
    
    return char_count

# Input from the user
input_string = input("Enter a string: ")

# Call the function and print the result
result = character_count(input_string)

# Print the character counts in dictionary format
print("Character counts:", result)


# 4. Reverse a String: Using a loop, write a program that takes a user-input string and returns the string reversed 
# (without using any built-in methods).
# Function to reverse a string using a loop
def reverse_string(input_string):
    reversed_string = ""  # Initialize an empty string to store the reversed string
    
    # Loop through the original string backwards
    for char in input_string:
        reversed_string = char + reversed_string  # Add each character to the beginning of the new string
    
    return reversed_string

# Input from the user
input_string = input("Enter a string to reverse: ")

# Call the function and print the reversed string
reversed_result = reverse_string(input_string)
print("Reversed string:", reversed_result)

# 5. Count Vowels and Consonants: Create a program that takes a string as input and counts the number of vowels and consonants
#  using a loop.
# Function to count vowels and consonants
def count_vowels_consonants(input_string):
    # Define vowels (both uppercase and lowercase)
    vowels = "aeiouAEIOU"
    
    # Initialize counters for vowels and consonants
    vowel_count = 0
    consonant_count = 0
    
    # Loop through each character in the input string
    for char in input_string:
        # Check if the character is an alphabetic letter
        if char.isalpha():
            if char in vowels:
                vowel_count += 1  # Increment vowel counter
            else:
                consonant_count += 1  # Increment consonant counter
    
    return vowel_count, consonant_count

# Input from the user
input_string = input("Enter a string: ")

# Call the function and get the vowel and consonant counts
vowels, consonants = count_vowels_consonants(input_string)

# Print the results
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
