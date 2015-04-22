"""
	Test suite runner for aztex.
"""
import os

CWD = os.getcwd()
tests = CWD + '/test_suites'
# files = os.listdir(tests)

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
	with open(tests+'/'+files[2]) as fp:
		line_list = fp.readlines()
		inpt = get_input(line_list)
		print 'AztexRunner.py '+inpt
		print os.system('python AztexRunner.py '+inpt)
		print get_output(line_list)
	