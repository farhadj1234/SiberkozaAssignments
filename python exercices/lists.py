# A List is a collection which is ordered and changeable. Allows duplicate members.
# Create list
numbers = [1, 2, 3, 4, 5]
fruits_fd = ['Apples', 'Oranges', 'Grapes', 'Pears']
# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))
# Get a value
print(fruits_fd[1])
# Get length
print(len(fruits_fd))
# Append to list
fruits_fd.append('Mangos')
# Remove from list
fruits_fd.remove('Grapes')
# Insert into position
fruits_fd.insert(2, 'Strawberries')
# Change value
fruits_fd[0] = 'Blueberries'
# Remove with pop
fruits_fd.pop(2)
# Reverse list
fruits_fd.reverse()
# Sort list
fruits_fd.sort()
# Reverse sort
fruits_fd.sort(reverse=True)
print(fruits_fd)

