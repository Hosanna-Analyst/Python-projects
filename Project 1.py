# 1. A. Create a string variable greeting with the value "Hello, World!" and perform the following operations:
Greeting="Hello, World"
print(Greeting)

# B. Print the string in all uppercase.
print(Greeting.upper())

# C. Print the string in all lowercase.
print(Greeting.lower())

# D. Replace "World" with your name.
Greeting_with_name=Greeting.replace("World","Hosanna")
print(Greeting_with_name)

# 2. Given the string quote = "The only limit to our realization of tomorrow is our doubts of today.", perform the following:
# A. Find the index of the word "doubts."
quote="The only limit to our realization of tomorrow is our doubts of today."
index_of_doubt=quote.find("doubt")
print(f"index of the word 'doubt':{index_of_doubt}")

# B. Count how many times the letter "o" appears.
count_of_o=quote.count("o")
print(f"number of times the letter'o' appears:{count_of_o}")

# C. Check if the string starts with "The" and ends with "today."
starts_with_the=quote.startswith("The")
ends_with_today=quote.endswith("today.")
print(f"starts with 'The':{starts_with_the}")
print(f"ends with 'today':{ends_with_today}")

# 3. Given the string text = "Data Science", write a program to:
# A. Count how many times the letter "a" appears in the string.
text="Data Science"
count_of_a=text.count("a")
print(f"number of times the letter 'a' appears:{count_of_a}")

# B. Count the total number of characters in the string, excluding spaces.'
total_chars_excluding_spaces = len(text.replace(" ", ""))
print(f"Total number of characters excluding spaces: {total_chars_excluding_spaces}")

# edited_text=text.strip()
# print(len(edited_text))
