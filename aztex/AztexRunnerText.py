""" 
	Prints the internal representation of a document as a string
"""
import sys
from Element import Element
from AztexCompiler import AztexCompiler

def is_text_file(filename):
	return filename.endswith('.txt')

def input_text(argv):
	""" gets input text from command line args """
	inputf = input_file(argv)

	if inputf:
		f = open(inputf, 'r')
		return f.read()
	else:
		text = ''.join(argv[1:])
		return text

def input_file(argv):
	""" gets the input file from command line args """
	# no input given
	if len(argv) == 1:
		return "input.txt"

	# input file given
	elif is_text_file(argv[1]):
		return argv[1]

def main():
	""" prints the internal representation """
	md_text = input_text(sys.argv)
	compiler = AztexCompiler()
	print '\n'.join(map(lambda x: str(x), compiler.get_representation(md_text)))

if __name__ == "__main__":
	main()
