# The system is importing argv.
from sys import argv
# There are 2 values to unpack into argv.
script, user_name = argv
# changing the prompt variable doesn't affect the code.
prompt = '* '
# The lines are printing and at the end the prompt is being inputted.
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)
# This line is printing lines but the lines are the input to the answers.
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")