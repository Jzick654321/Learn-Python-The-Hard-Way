# The system imports arguments
from sys import argv
# The script and filename is imported into the arguments
script, filename = argv
# printing the lines and inside the curly brackets is putting the filename in the line
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# Targeting the file and opening it
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# targeting the truncate and erasing it
target.truncate()

print("Now i'm going to ask you for three lines.")
# the lines are needed in the text file
# I realized in the second file you need 3 lines open instead of only having 1 line.
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# Targeting each line and letting you write in the line and making a new line each.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# Targets the file and closes it.
target.close()