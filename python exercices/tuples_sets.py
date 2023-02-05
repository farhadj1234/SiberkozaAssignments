# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Create tuple
fruits_fd = ('Apples', 'Oranges', 'Grapes')
# fruits_fd2 = tuple(('Apples', 'Oranges', 'Grapes'))
#single value needs trailing coma
fruits_fd2 = ('Apples',)
# Get value 
print(fruits_fd[1])
#Can't change value
#fruits_fd[0] = 'Pears'
#Delete tuple
del fruits_fd2
#Get length
print(len(fruits_fd))
# A Set is a collection which is unordered and unindexed. No duplicate members.
# Create set
fruits_fd_set = {'Apples', 'Oranges', 'Mango'}
# Check if in set 
print ('Apples' in fruits_fd_set)
# Add to set
fruits_fd_set.add('Grape')
# Remove from set 
fruits_fd_set.remove('Grape')
# clear set 
#fruits_fd_set.clear()
# Delete
#del fruits_fd_set
print(fruits_fd_set)

