from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "if you don't want that, hit CTRL+C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'mgoing to ask you for hree lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close() 

print "This is how the file looks:"
target2 = open(filename)
print target2.read()
target2.close()

