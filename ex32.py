the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#go through a list
for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit
    
#go through mixed list
for i in change:
    print "I got %r" % i
    
#build a list
elements = []

for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)
    
#print the new list
for i in elements:
    print "element was: %d" % i