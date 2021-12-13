nums = [1,2,3,4,5]
nums2 = list((1,2,3,4,5))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pairs']

# Get oranges
print(fruits[1])

# Get length (4)
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Remove from position
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort alphabetically
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

# Change value
fruits[0] = 'Blueberries'