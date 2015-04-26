"""
	Test suite runner for aztex.
"""
import os
from AztexRunner import run_test


def get_input(line_list):
	""" Returns the input that is being tested. """
	input_lines = line_list[1:line_list.index('Output:\n')]
	if len(input_lines) >= 1:
		if '\n' in input_lines[-1]:
			input_lines[-1] = input_lines[-1].replace('\n', '')
	return ''.join(input_lines)

def get_output(line_list):
	""" Returns what the output of the test should be. """
	output_lines = line_list[line_list.index('Output:\n')+1:]
	return ''.join(output_lines)

if __name__ == '__main__':
	cwd = os.getcwd()
	tests = cwd + '/test_suite'
	files = os.listdir(tests)
	if '.DS_Store' in files: files.remove('.DS_Store')
	test_result = True
	for f in files:
		with open(tests+'/'+f) as fp:
			line_list = fp.readlines()
			result = run_test(get_input(line_list))
			test_result = result == get_output(line_list)
			if not test_result:
				print f + ': FAILED'