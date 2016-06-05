from nose.tools import *
from ex48 import lexicon
from ex48 import parserClass

INPUT = lexicon.scan("princess go to the door")
parsed_input = parserClass.Parse(INPUT)


def test_peek_class():
	assert_equal(parsed_input.peek(), 'noun')
	
def test_verb():
	assert_equal(parsed_input.match('verb'), None)
	assert_equal(parsed_input.match('noun'), ('princess', 'noun'))