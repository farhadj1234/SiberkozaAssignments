# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people_fd = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person_fd in people_fd:
  print(f'Current Person_fd: {person_fd}')

# Break
for person_fd in people_fd:
  if person_fd == 'Sara':
    break
  print(f'Current Person_fd: {person_fd}')

# Continue
for person_fd in people_fd:
  if person_fd == 'Sara':
    continue
  print(f'Current Person_fd: {person_fd}')

# range
for i in range(len(people_fd)):
  print(people_fd[i])
for i in range(0, 11):
  print(f'Number_fd: {i}')

# While loops execute a set of statements as long as a condition is true.
count_fd = 0
while count_fd < 10:
  print(f'Count_fd: {count_fd}')
  count_fd += 1
