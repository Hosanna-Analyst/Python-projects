# 1. Predefined value for length,width,threshold
length=20
width=10
threshold=50

# The area of a rectangle, using predefined values for Length and Width.
area=length*width
print(f"Area of a rectangle:{area}cm")
print(length//width) #using floor division
print(length**width) #using exponention

# The perimeter of the rectangle using the same predefined Length and Width.
perimeter=2*(length+width)
print(f"The perimeter of the rectangle:{perimeter}cm")

# Check if the area is greater than a predefined threshold value.
Check_area=area>threshold #comparison operator
print(f"Is area greater than threshold:{Check_area}")

# Ensure to utilize multiple operators throughout the calculations
#Assignment operator
length+=2
width+=2
new_area=length*width #newarea after modifying
print(f"new area after modifying:{new_area}cm")

#Conditional xpression to check new area
result= "Exceeds threshold" if new_area> threshold else "within threshold"
print(f"new area check:{result}")

# ' 2. Check for Vowel or Consonant
# # a.Write a Python program that checks if a given letter is a vowel or a consonant.
# # • Vowels: 'a', 'e', 'i', 'o', 'u' (consider both uppercase and lowercase letters)
# def check_vowels_or_consonant(letter):
#     vowels='aeiouAEIOU' #(it defines vowels with both lower and uppercase)
#     if len(letter)==1 and letter.isalpha(): #(check if input is single alphabet)
#         if letter in vowels:
#             return f"'{letter}' is a vowel."
#         else:
#             return f"'{letter}' is a consonant."
#     else:
#         return "please enter a single valid alphabet letter."

    
# # 3. Divisibility Check
# # Write a Python program that checks if a number is divisible by 3 and 5.
# # • If divisible by both, print "Divisible by both"
# # • If divisible by only 3, print "Divisible by 3"
# # • If divisible by only 5, print "Divisible by 5"
# # • Otherwise, print "Not divisible by 3 or 5"
# def check_divisibility(number):
#     if number %3==0 and number %5==0:
#         print("divisibility by both")
#     elif number %3==0:
#         print("divisible by 3")
#     elif number %5==0:
#         print("divisible by 5")
#     else:
#         print("not divisible by 3 or 5")
       
# check_divisibility(2)

# # 4. write a Python program to check the type of triangle (equilateral, isosceles, or scalene) based on the lengths of its sides.
# # • Equilateral: All sides are equal
# # • Isosceles: Two sides are equal
# # • Scalene: All sides are different
# ''

# CORRECTION
# 2.
vowel_sound="aeiouAEIOU"
user_input=input('enter an alphabet')
if user_input in vowel_sound:
    print('alphabet is a vowel sound')
else:
    print('alphabet is a consonant')

# 3.
