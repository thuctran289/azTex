"""
	Test suite runner for aztex.
"""
import os
from AztexRunner import run_test


def get_input(line_list):
	input_lines = line_list[1:line_list.index('Output:\n')]
	if '\n' in input_lines[-1]:
		input_lines[-1] = input_lines[-1].replace('\n', '')
	return ''.join(input_lines)
	# for line in fp:
	# 	if line.startswith('Input:'):
	# 		break
	# input_str = ''
	# for line in fp:
	# 	if line.startswith('Output:'):
	# 		break
	# 	input_str += line
	# return input_str

def get_output(line_list):
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
			if test_result == False:
				print f + ': FAILED'
				break

	with open(tests+'/'+files[1]) as fp:
		line_list = fp.readlines()
		inpt = get_input(line_list)
		# print 'AztexRunner.py '+inpt
		result = run_test(inpt)
		print result == get_output(line_list)