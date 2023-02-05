# Python has functions for creating, reading, updating, and deleting files.
# Open a file
myFile_fd = open('myfile.txt', 'w')
# Get some info
print('Name: ', myFile_fd.name)
print('Is Closed :', myFile_fd.closed)
print('Opening Mode:', myFile_fd.mode)
# Write to file
myFile_fd.write('I love Python')
myFile_fd.write(' and JavaScript')
myFile_fd.close()
# Append to file
myFile_fd = open('myfile.txt', 'a')
myFile_fd.write(' I also like PHP')
myFile_fd.close()
# Read from file
myFile_fd = open('myfile.txt', 'r+')
text = myFile_fd.read(100)
print(text)
