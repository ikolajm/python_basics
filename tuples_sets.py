fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

# Tuples are UNCHANGEABLE

# Sets are unordered and unindexed - no duplicates
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

# Add duplicate (Will not be added)
fruits.set('Apples')

# Delete set
del fruits_set