# The end line is to print a line and to have the input go in there
print("How old are you?", end= ' ')
# the input is the thing that you type into the console
age = input()
print("How tall are you?", end= ' ')
height = input()
print("How much do you weigh?", end= ' ')
weight = input()
# The print inside the curly brackets is so python knows were to put the input
print(f"So, you're {age} old, {height} tall and {weight} heavy.")