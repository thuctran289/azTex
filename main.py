import sys
from os import path
here = path.abspath(path.dirname(__file__))
sys.path.append(here + "/src/") 
from Element import Element
import sys
from Element import Element
from LatexOutput import *
from Tokenizer import Tokenizer
from Parser import Parser

def main():

	if len(sys.argv) > 1:
		args = sys.argv[1:]
		if '.txt' in args[0]:
			filename = args[0]
			w = open(filename[:-4:] + ".tex", 'w')
			f = open(filename, 'r')
			text = f.read()
		else:
			w = open('newfile.tex', 'w')
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
	#	print element
	#	print ""

	for element in  A.to_doc(elements):
		w.write(str(element))
		w.write('\n')

	print "==============================\n\n"


	print "==============="
	print "=== SUCCESS ==="
	print "==============="

if __name__ == "__main__":
	main()
