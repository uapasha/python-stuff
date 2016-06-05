from lexicon import scan

input = "princess run to the door"

class ParserError(Exception):
	pass
	
class Sentence (object):
	def __init__(self, subject, verb, object):
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = object[1]
	
class Parse(object):
	def __init__(self, word_list):
		self.word_list = word_list
		
	def peek(self):

		if self.word_list:
			word = self.word_list[0]
			return word[0]
		else:
			return None
			
	def match(self, expected):
			if self.word_list:
				word=self.word_list.pop(0)
				print word
			
				if word[0] == expected:
					return word
				else:
					return None
			else:
				return None
			
	def skip (self, word_type):
		while self.peek() == word_type:
			self.match(word_type)
		
	def parse_verb(self):
		self.skip('stop')
		if self.peek() == 'verb':
			return (self.match('verb'))
		else:
			return ParserError('Expected a verb text')

	def parse_object(self):
		self.skip('stop')
		next_word = self.peek()
		if next_word == 'noun':
			return (self.match('noun'))
		elif next_word == 'direction':
			return (self.match('direction'))
		else:
			return ParserError('Expected a noun or a direction')

	def parse_subject(self):
		skip('stop')
		next_word = peek()
		
		if next_word == 'noun':
			return match('noun')
		elif next_word == 'verb':
			return ('noun', 'player')
		else:
			ParserError('Expected a verb text')

	def parse_sentence(self):
		verb = self.parse_verb()
		object = self.parse_object()
		subject = self.parse_subject()
		return Sentence(subject, verb, object)
		