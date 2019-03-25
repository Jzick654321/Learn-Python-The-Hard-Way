# the system is importing argv.
from sys import argv
# The next two lines are to use argv to get a filename.
script, filename = argv

txt = open(filename)
# printing and giving yo u the file.
print(f"Here's your file {filename}:")
print(txt.read())
# printing the file name and giving you an input.
print("Type the filename again:")
file_again = input("> ")
# opening the file
txt_again = open(file_again)
# printing the text file.
print(txt_again.read())