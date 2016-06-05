people = 50
cars = 40
trucks = 15

def check_num (people, cars, trucks):
	if cars > people:
		print "We should take the cars."
	elif cars < people:
		print "We should not take the cars."
	else:
		print "We can't decide."
	
	if trucks > cars: 
		print "Thats too many trucks."
	elif trucks < cars:
		print "Maybe we could take the trucks."
	else:
		print "We still can't decide."
	
	if people > trucks:
		print "Alright, lets just take the trucks."
	else:
		print "Finem lets stay home than."

check_num(people, cars, trucks)		