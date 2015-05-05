"""
	@author: jovanduy
	Test suite runner for aztex.
"""
import os
from AztexCompiler import AztexCompiler


def get_input(line_list):
	""" Returns the input that is being tested. """
	input_lines = line_list[1:line_list.index('Output:\n')]
	#blankdoc.txt test has no input lines
	if len(input_lines) >= 1:
		if '\n' in input_lines[-1]:
			input_lines[-1] = input_lines[-1].replace('\n', '')
	return ''.join(input_lines) 

def get_output(line_list):
	""" Returns what the output of the test should be. """
	output_lines = line_list[line_list.index('Output:\n')+1:]
	return ''.join(output_lines)

def run_test(line_list):
	md_text = get_input(line_list)

	actual = compiler.compile(md_text) 
	expected = get_output(line_list)

	test_result = (actual == expected)
	if not test_result:
		print f + ':\n'
		print 'expected:\n' + expected
		print 'got:\n' + actual
		print '----------------------\n'

if __name__ == '__main__':
	cwd = os.getcwd()
	tests = cwd + '/test_suite'
	files = os.listdir(tests)

	# OSX creates a .DS_Store in directories, this is 
	# not part of the test suite
	if '.DS_Store' in files: files.remove('.DS_Store')

	# run through all the files, printing the names of
	# the ones that failed the test
	compiler = AztexCompiler()
	for f in files:
		with open(tests+'/'+f) as fp:
			line_list = fp.readlines()
			run_test(line_list)
