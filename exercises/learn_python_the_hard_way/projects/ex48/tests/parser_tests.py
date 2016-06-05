from nose.tools import *
from ex48 import parser
from ex48 import lexicon


input = lexicon.scan("princess go to the door")

def test_peek():
	assert_equal(parser.peek([]), None)
	assert_equal(parser.peek([('verb', 'run')]), 'verb')
	assert_equal(parser.peek(input), 'noun')
	assert_equal(parser.peek(input[1:2]), 'verb')
	assert_equal(parser.peek(input[2:3]), 'stop')
	

def test_verb():
	assert_equal(parser.parse_verb([('verb', 'run')]), ('verb', 'run'))

	assert_raises("ParserError", parser.parse_verb, input)