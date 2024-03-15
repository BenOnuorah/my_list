# Create an empty list called my_list
my_list = []

# Append the elements 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position
my_list.insert(1, 15)

# Extend my_list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print (f'Index of value 30 is {index_of_30 }')

# Print the final list
for val in my_list:
	print (val)

