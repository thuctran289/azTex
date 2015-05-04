import re

class Tokenizer(object):
	""" breaks input up into tokens """

	BLOCK_REGEX = "([^\n]+(?:\n[^\n]+)*(?=\n|$))"
	BLOCK_PATTERN = re.compile(BLOCK_REGEX)
	
	def __init__(self, text):
		self.text = text
		self.text_index = 0

	def get_next_block(self):
		""" finds the next token 
		>>> t = Tokenizer('first block\\n\\nsecond block')
		>>> t.get_next_block()
		'first block'
		>>> t.get_next_block()
		'second block'
		>>> str(t.get_next_block())
		'None'
		"""
		match = self.BLOCK_PATTERN.search(self.text, self.text_index)	 

		if match == None:
			return None

		self.text_index = match.end()
		block = match.group()
		return block

if __name__ == "__main__":
	import doctest
	doctest.testmod()
