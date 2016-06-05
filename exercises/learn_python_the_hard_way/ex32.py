the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this is first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go throught mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
# we can also build lists, first start with an empty one
elements = range(0, 6)

# then use the range function to do 0 to 5 counts
#for i in range(0, 6):
#	print "Adding %d to the list." % i 
#	elements.append(i)

#elements.append(range(6, 8))
	
# now we can print them out too
for i in elements: 
		print "Element was: %r" % i