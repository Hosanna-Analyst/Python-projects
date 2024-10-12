# '1a.Create a List: Create a list of your five favorite movies. Print the list.
Meal_list=["american","korea","chinese","nigerian","german"]
print(Meal_list)

# 1b.Access Elements: Print the first and last movie from your list.
print(Meal_list[0])
print(Meal_list[4])

# 1c.Modify a List: Change the second movie in your list to a new favorite and print the updated list.
Meal_list[1]=['Bolly']
print(Meal_list)

# 1d. Add a Movie: Append another movie to your list and print the updated list.
Meal_list.append('Asia')
print(Meal_list)

# 1e.Remove a Movie: Remove the fourth movie from your list and print the updated list.
Meal_list.remove(['Bolly'])
print(Meal_list)

# 2a. Slice the List: Create a list of at least 10 integers. Print the first three numbers, the last three numbers, 
# and the middle five numbers.
Number_list=[25,30,40,50,60,70,80,90,95,10]
print(Number_list)
print(Number_list[0:3])
print(Number_list[7:10])
print(Number_list[3:8])

# 2b. Negative Indexing: Use negative indexing to print the last two numbers in your list.



# 3a Create a Nested List: Create a list that contains three other lists. Each of the inner lists should have three integers.
#  Print the nested list.

# Access Nested Elements: Retrieve and print the second element of the first inner list.

# extra:
# Create a Tuple: Create a tuple containing the names of five animals. Print the tuple.
Animal_Tuple=("lion","tiger","Ape","monkey","goat")
print(Animal_Tuple)

# Access Elements: Print the first and last animal from your tuple.
print(Animal_Tuple[0])
print(Animal_Tuple[4])

# extra extra:
# Create a Dictionary: Create a dictionary to store the names and ages of five people. Print the dictionary.
NameandAge_Dictionary={"Hosanna":"30","stella":'40',"Iyke":'50',"Theo":'60',"Busayo":'70'}
print(NameandAge_Dictionary)

# Access Values: Access and print the age of one of the people in your dictionary.
print(NameandAge_Dictionary["Hosanna"])

# Modify Values: Change the age of one of the people in your dictionary and print the updated dictionary.'
NameandAge_Dictionary["Busayo"]='25'
print(NameandAge_Dictionary)