"""
	Test suite runner for aztex.
"""
import os

CWD = os.getcwd()
tests = CWD + '/test_suites'
# files = os.listdir(tests)

def get_input(fp):
	for line in fp:
		if line.startswith('Input:'):
			break
	input_str = ''
	for line in fp:
		if line.startswith('Output:'):
			break
		input_str += line
	return input_str

def get_output(fp):
	pass

if __name__ == '__main__':
	cwd = os.getcwd()
	tests = cwd 
	files = os.listdir(tests)
	
	with open(files[1]) as fp:
		print get_input(fp)
	