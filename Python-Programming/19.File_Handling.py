"""
File Handling in Python:
Create a file
Open a file
Work on file
Close on file

Creating/opening a file in different Modes:
r = read mode
w = write mode
a = append mode
x = create the file
"""
import os          # Will use this module only to delete the file

file1=open("C:/Users/pra44/Desktop/f_handle/text1.txt",'x')  # Creating a file---Produces Error if file already created
# Closing the file
file1.close()

# **********************************************************************************************************************
# Opening a file in write mode and adding some content
file1=open("C:/Users/pra44/Desktop/f_handle/text1.txt",'w')
file1.write("This is file Handling in Python\nThis is second line\nThis is third line\nThis is fourth Line")
file1.close()

# **********************************************************************************************************************
# Opening a file in read mode and reading the content
file1=open("C:/Users/pra44/Desktop/f_handle/text1.txt",'r')
# print(file1.read())        # Reads the entire file
# print(file1.readline())    # Reads the First Line
# print(file1.readline(14))  # Reads the line up top 14 characters
# print(file1.readline(5))   # Reads 5 characters starting from 14 because the pointer will be at 14th character
file1.seek(0)
list1 = file1.readlines()    # Read lines separately and assign them into list
print(list1[0])            # returns the first line
print(list1[1])            # returns the second line
print(list1[2])            # returns the third line
file1.close()

# **********************************************************************************************************************
# Deleting a file

os.remove("C:/Users/pra44/Desktop/f_handle/text1.txt")





