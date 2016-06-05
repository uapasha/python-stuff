VOWELS = 'уеаоіиюяєї'

ans = {'vowels':0, 'consonants': 0, 'punctuations': 0, 'spaces':0}
top_five = []

f = open('taras.txt', 'r', encoding='utf8')
poem = f.read().lower()

poem = poem.split()

## go through each word
for w in poem:
	ans['spaces'] +=1
	word = ''

	## go inside each word
	for c in w:

		if not c.isalpha():
			ans['punctuations'] += 1
		
		elif c in VOWELS:
			ans['vowels'] +=1
			word += c
		
		else:
			ans['consonants'] += 1
			word +=c

	## check whether word is top 5
	if len(top_five) < 5:
		top_five.append(word)
	
	elif word in top_five:
		pass
	
	else:
		shortest_word = min(top_five, key=len)
		
		if len(shortest_word) < len(word):
			top_five.remove(shortest_word)
			top_five.append(word)


## result

print ('amount of vowels: %s \n \ramount of consonants: %s \n \
		\ramount of punctuations: %s \n \ramount of spaces: %s \n \
		\rtop five words: ' % (ans['vowels'], ans['consonants'], ans['punctuations'], 
								ans['spaces']))
for i in top_five:
	print(repr(i.encode('utf-8').decode('UTF-8').replace(u'\u0456', u'i')))