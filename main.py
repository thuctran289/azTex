"""
	@authors: idgetto, jovanduy, thuctran289

	Main aztex program. Run this program to get the LaTeX 
	output of given aztex code. Creates a .tex file with the
	same name as the input file (if input is text rather than 
	a file, creates a file named newfile.tex) with the analogous
	LaTeX code.

	To run:
		with a certain file filename: python main.py filename.txt
		with a file input.txt: python main.py
		with "just a few words": python main.py "just a few words"
"""

import sys
from os import path

here = path.abspath(path.dirname(__file__))
sys.path.append(here + "/src") 

from Element import Element
from LatexOutput import LatexOutput
from Tokenizer import Tokenizer
from Parser import Parser
from AztexCompiler import AztexCompiler

def is_text_file(filename):
	return filename.endswith('.txt')

def tex_file_name(txt_file):
	name = txt_file.split('.')[0]
	tex_file = name + '.tex'
	return tex_file

def input_text(argv):
	inputf = input_file(argv)

	if inputf:
		f = open(inputf, 'r')
		return f.read()
	else:
		text = ' '.join(argv[1:])
		return text

def input_file(argv):
	# no input given
	if len(argv) == 1:
		return "input.txt"

	# input file given
	elif is_text_file(argv[1]):
		return argv[1]

def output_file(argv):
	inputf = input_file(argv)

	if inputf:
		return tex_file_name(inputf)
	else:
		return 'out.tex'

def main():
	md_text = input_text(sys.argv)
	compiler = AztexCompiler()
	latex_str = compiler.compile(md_text)

	out_file = output_file(sys.argv)
	w = open(out_file, 'w')

	w.write(latex_str)

if __name__ == "__main__":
	main()
