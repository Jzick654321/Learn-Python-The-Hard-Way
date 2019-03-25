# system is importing into arguments
from sys import argv
from os.path import exists
# transfering one file to another
script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# opening one file to another file
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready hit RETURN to continue, CTRL-C to abort.")
input()
# opening to a new file
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
# closing the first file and then the second file
out_file.close()
in_file.close()