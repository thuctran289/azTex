"""
	@authors: idgetto, 
"""

import sys
from Element import Element
from LatexOutput import *
from Tokenizer import Tokenizer
from Parser import Parser

def run_test(text):
	""" Function to run AztexRunner on some given text input 
		text: string of input text that should be aztex code
		returns: the analogous LaTeX output to text
	"""
	tokenizer = Tokenizer(text)
	parser = Parser()

	elements = []
	block = tokenizer.get_next_block()
	while block:
		element = parser.parseBlock(block)
		elements.append(element)
		block = tokenizer.get_next_block()

	A = LatexOutput()
	return ''.join(A.to_doc(elements))

if __name__ == "__main__":
	if len(sys.argv) > 1:
		args = sys.argv[1:]
		if '.txt' in args:
			filename = args
			w = open(filename[:-4:] + ".tex", 'w')
			f = open(filename, 'r')
			text = f.read()
		else:
			text = ' '.join(args)
	else:
		filename = "input.txt"
		w = open(filename[:-4:] + ".tex", 'w')
		f = open(filename, 'r')
		text = f.read()

		print "===== ORIGINAL FILE =====\n"
		print text
		print "=========================\n\n"

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

		print "===== DOCUMENT ELEMENTS ====="
		A = LatexOutput()

	#for element in elements:
	#	print A.to_code(element)
	#	print ""

	for element in  A.to_doc(elements):
		w.write(str(element))

	print "==============================\n\n"


	print "==============="
	print "=== SUCCESS ==="
	print "==============="




