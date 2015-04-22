import sys
from Element import Element
from LatexOutput import *

if len(sys.argv) > 1:
	args = sys.argv[1:]
	if '.txt' in args:
		filename = args
		f = open(filename, 'r')
		text = f.read()
	else:
		text = ' '.join(args)
else:
	filename = "input.txt"
	f = open(filename, 'r')
	text = f.read()

from Tokenizer import Tokenizer
from Parser import Parser

tokenizer = Tokenizer(text)
parser = Parser()

elements = []
block = tokenizer.get_next_block()
while block:
    element = parser.parseBlock(block)
    elements.append(element)
    block = tokenizer.get_next_block()

A = LatexOutput()

#for element in elements:
#	print A.to_code(element)
#	print ""
# for element in  A.to_doc( elements):
# 	print element
print '\n'.join(A.to_doc(elements)) + "HELLO WORLD"

def run_test(text):
	tokenizer = Tokenizer(text)
	parser = Parser()

	elements = []
	block = tokenizer.get_next_block()
	while block:
    	element = parser.parseBlock(block)
    	elements.append(element)
    	block = tokenizer.get_next_block()

	A = LatexOutput()
	return '\n'.join(A.to_doc(elements))