"""
	@author: jovanduy
	Test suite runner for aztex.
"""
import os
from AztexCompiler import AztexCompiler


def get_input(line_list):
	""" Returns the input that is being tested. """
	output_index = line_list.index('Output:\n')
	input_lines = line_list[1:output_index]

	#blankdoc.txt test has no input lines
	return ''.join(input_lines).rstrip('\n')

def get_output(line_list):
	""" Returns what the output of the test should be. """
	output_index = line_list.index('Output:\n')
	output_lines = line_list[output_index+1:]
	return ''.join(output_lines).rstrip('\n')

def run_test(filename, line_list):
	md_text = get_input(line_list)

	actual = compiler.compile(md_text) 
	expected = get_output(line_list)

	test_result = (actual == expected)
	if not test_result:
		print filename + '\n'
		print 'expected:\n' + expected
		print 'got:\n' + actual
		print '----------------------\n'

if __name__ == '__main__':
	cwd = os.getcwd()
	tests = cwd + '/test_suite'
	files = os.listdir(tests)
	files = filter(lambda x: x.endswith('.txt'), files)

	# OSX creates a .DS_Store in directories, this is 
	# not part of the test suite
	if '.DS_Store' in files: files.remove('.DS_Store')

	# run through all the files, printing the names of
	# the ones that failed the test
	compiler = AztexCompiler()
	for f in files:
		with open(tests+'/'+f) as fp:
			line_list = fp.readlines()
			run_test(f, line_list)
