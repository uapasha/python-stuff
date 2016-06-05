
def create_list(length, incr):
	#i = 0
	numbers = []
	for i in range(0, length, incr):
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + incr
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "

	for num in numbers:
		print num
create_list(10, 3)