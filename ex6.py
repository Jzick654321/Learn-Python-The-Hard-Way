# The variable is showing the number of people
types_of_people = 10
x = f"There are {types_of_people} types of people."
# The variables are being put into a text for the output
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
# There are 2 lines being printed for line x and y above
print(x)
print(y)
# x and y are being put into the text so they
# don't have to retype the print
print(f"I said: {x}")
# I noticed that the y is inputing the y = above and in those curly brackets
# the variables that were printed like binary = "binary" are being put into
# the curly brackets.
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# This print is to have the variable False print after
# the question "Isn't that joke so funny"
print(joke_evaluation.format(hilarious))
# The variable w and e are a sentence to put into a print faster
w = "This is the left side of..."
e = "a string with a right side."
# The print w and e are are a faster way of retying the
# sentence over again
# the reason why adding two strings w and e with + makes a longer string is that
# w + e prints the variables above of w = and e = so the strings form longer.
print(w + e)