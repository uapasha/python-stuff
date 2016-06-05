categories = {"direction" : ["north", "south", "east", "west", "up", "down",
			"left", "rigth", "back"],
			"verb": ["do", "stop", "kill", "eat", "go"],
			"stop": ["the", "in", "of", "from", "at", "it", "if", "to"],
			"noun": ["door", "bear", "princess", "cabinet"]
			}
def convert_input(s):
	try:
		s = int(s)
		return s
	except ValueError:
		return None
			
def scan(user_input):
	result = []
	input = user_input
	input = input.split()
	for word in input:
		w_flag = False
		
		if convert_input(word) != None:
			result.append(('number', convert_input(word)))
			w_flag = True
		else:
			for cat in categories:
			
				if word.lower() in categories[cat]:
					result.append((cat, word))
					w_flag = True
			
		if not w_flag:			
			result.append(('error', word))
	
	return result