import sys
from Element import Element

def main():

	filename = "input.txt"
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

	for element in elements:
		print element

	print "==============================\n\n"


	print "==============="
	print "=== SUCCESS ==="
	print "==============="

