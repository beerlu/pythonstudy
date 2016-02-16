from nose.tools import *
from ex48 import parser

def test_peek():
    assert_equal(parser.peek([('direction', 'north'),('noun','bear')]),'direction')
    
							
def test_match():
    assert_equal(parser.match([('direction', 'north'),('noun','bear')], 'direction'), ('direction', 'north'))
    assert_equal(parser.match([('direction', 'north'),('noun','bear')], 'noun'), None)	
    assert_equal(parser.match([],'noun'), None)

def test_skip():
	x = [('stop', 'to'),('verb', 'run'), ('direction', 'north')]
	parser.skip(x,'stop')
	assert_equal(x, [('verb', 'run'), ('direction', 'north')])
	
	x = [('stop', 'at'), ('stop', 'to'),('verb', 'run'), ('stop', 'to'), ('direction', 'north')]
	parser.skip(x,'stop')
	assert_equal(x, [('verb', 'run'), ('stop', 'to'), ('direction', 'north')])
	
def test_parse_subject():
	assert_raises(Exception, parser.parse_subject,[('direction','north'), ('noun','fox')])
	assert_equal(parser.parse_subject([('noun', 'fox'), ('verb', 'says'), ('object', 'pawpawpawpawpawpaw')]), ('noun', 'fox'))
	assert_equal(parser.parse_subject([('verb', 'kick'), ('what', 'pawpawpawpawpawpaw')]), ('noun', 'player'))
	

	