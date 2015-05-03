"""
	Puts all the aztex classes together
"""	

from Element import Element
from LatexOutput import LatexOutput
from Tokenizer import Tokenizer
from Parser import Parser

def latex_text(md_text):
	elements = get_elements(md_text)

	latexOutput = LatexOutput()
	latex_str = latexOutput.to_str(elements)
	return latex_str

def get_elements(md_text):
	tokenizer = Tokenizer(md_text)
	parser = Parser()

	elements = []
	block = tokenizer.get_next_block()
	while block:
	    element = parser.parseBlock(block)
	    elements.append(element)
	    block = tokenizer.get_next_block()

	return elements
