from sys import argv

script, input_file = argv
# printing everything from the text file.
def print_all(f):
    print(f.read())
# rewinding the file.
def rewind(f):
    f.seek(0)
# printing each line from text file.
def print_a_line(line_count, f):
    print(line_count, f.readline())
# opening an input file.
current_file = open(input_file)
# printing
print("First let's print the whole file:\n")
# printing all.
print_all(current_file)
# printing
print("Now Let's rewind, kind of like a tape.")
# rewinding the current file.
rewind(current_file)
# printing
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)