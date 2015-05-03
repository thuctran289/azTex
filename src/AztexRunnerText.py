import sys
from Element import Element
import Aztex

def is_text_file(filename):
	return filename.endswith('.txt')

def input_text(argv):
	inputf = input_file(argv)

	if inputf:
		f = open(inputf, 'r')
		return f.read()
	else:
		text = ''.join(argv[1:])
		return text

def input_file(argv):
	# no input given
	if len(argv) == 1:
		return "input.txt"

	# input file given
	elif is_text_file(argv[1]):
		return argv[1]

def main():
	md_text = input_text(sys.argv)
	print '\n'.join(map(lambda x: str(x), Aztex.get_elements(md_text)))

if __name__ == "__main__":
	main()
