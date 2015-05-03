import re
from Regex import *

class Matcher(object):
	""" determines what element an input block is """

	def match(self, block, pattern):
		return pattern.match(block)

	def matchHeading(self, block):
		""" determines if a block is a header
		ie: 
				aztex
				=====
		>>> m = Matcher()
		>>> bool(m.matchHeading("aztex\\n=====")) 
		True
		>>> bool(m.matchHeading('Harry Potter\\n===='))
		True
		>>> bool(m.matchHeading('Voldemort\\n='))
		False
		"""
		return self.match(block, HEADING_PATTERN)

	def matchSubHeading(self, block):
		""" determines if a block is a subheader
		ie: 
				aztex
				-----
		>>> m = Matcher()
		>>> bool(m.matchSubHeading("aztex\\n=====")) 
		False
		>>> bool(m.matchSubHeading("aztex\\n-----")) 
		True
		>>> bool(m.matchSubHeading("Harry Potter\\n-----"))
		True
		>>> bool(m.matchSubHeading('Voldemort\\n-'))
		False
		"""
		return self.match(block, SUB_HEADING_PATTERN)

	def matchSubSubHeading(self, block):
		""" determines if a block is a subsubheader
		ie: 
				#### aztex ####
		>>> m = Matcher()
		>>> bool(m.matchSubSubHeading("## aztex ##")) 
		True
		>>> bool(m.matchSubSubHeading("#### aztex ####")) 
		True
		>>> bool(m.matchSubSubHeading("# Harry Potter #"))
		True
		>>> bool(m.matchSubSubHeading('### Voldemort #'))
		False
		>>> bool(m.matchSubSubHeading('## Ron'))
		False
		"""
		return self.match(block, SUB_SUB_HEADING_PATTERN)

	def tableString(self):
		return "| id | name |     email    |\n\
				|----|------|--------------|\n\
				| 1  | bob  | bob@mail.com |\n\
				| 2  | tom  | tom@mail.com |\n\
				| 3  | ron  | ron@mail.com |"

	def matchTable(self, block):
		""" determines if the block is a table
		>>> m = Matcher()
		>>> bool(m.matchTable("| cat |"))
		False
		>>> bool(m.matchTable(m.tableString()))
		True
		"""
		return self.match(block, TABLE_PATTERN)

	def matchOrderedList(self, block):
		""" determines if the block is an ordered list
		>>> m = Matcher()
		>>> bool(m.matchOrderedList("1. eggs\\n2. bread\\n3. rice"))
		True
		"""
		return self.match(block, ORDERED_LIST_PATTERN)

	def matchUnorderedList(self, block):
		""" determines if the block is an ordered list
		>>> m = Matcher()
		>>> bool(m.matchUnorderedList("* eggs\\n* bread\\n* rice"))
		True
		>>> bool(m.matchUnorderedList("- eggs\\n- bread\\n- rice"))
		True
		"""
		return self.match(block, UNORDERED_LIST_PATTERN)

	def matchBlockEquation(self, block):
		""" determines if the block is a block equation
		>>> m = Matcher()
		>>> bool(m.matchBlockEquation("y = 3 * x"))
		True
		>>> bool(m.matchBlockEquation("Einstein: e = m * c ^ 2"))
		False
		"""
		return self.match(block, EQUATION_BLOCK_PATTERN)

	def matchBoldText(self, block):
		""" determines if a block starts with bold text
		>>> m = Matcher()
		>>> bool(m.matchBoldText("**yup, it does**"))
		True
		>>> bool(m.matchBoldText("*nope, this is italic*"))
		False
		"""
		return self.match(block, START_BOLD_TEXT_PATTERN)

	def matchBoldItalicText(self, block):
		""" determines if a block starts with bold text
		>>> m = Matcher()
		>>> bool(m.matchBoldItalicText("***yup, it does***"))
		True
		>>> bool(m.matchBoldItalicText("*nope, this is italic*"))
		False
		"""
		return self.match(block, START_BOLD_ITALIC_TEXT_PATTERN)

	def matchItalicText(self, block):
		""" determines if a block starts with italic text
		>>> m = Matcher()
		>>> bool(m.matchItalicText("*yup, it does*"))
		True
		>>> bool(m.matchItalicText("**nope, this is bold**"))
		False
		"""
		return self.match(block, START_ITALIC_TEXT_PATTERN)

	def matchStrikethroughText(self, block):
		""" determines if a block starts with strike through text
		>>> m = Matcher()
		>>> bool(m.matchStrikethroughText("~~yup, it does~~"))
		True
		>>> bool(m.matchStrikethroughText("**nope, this is bold**"))
		False
		"""
		return self.match(block, START_STRIKETHROUGH_TEXT_PATTERN)

	def matchUnderlineText(self, block):
		""" determines if a block starts with underlined text
		>>> m = Matcher()
		>>> bool(m.matchUnderlineText("_yup, it does_"))
		True
		>>> bool(m.matchUnderlineText("**nope, this is bold**"))
		False
		"""
		return self.match(block, START_UNDERLINE_TEXT_PATTERN)

	def matchQuoteText(self, block):
		""" determines if a block starts with quoted text
		>>> m = Matcher()
		>>> bool(m.matchQuoteText("``yup, it does\'\'"))
		True
		>>> bool(m.matchQuoteText("**nope, this is bold**"))
		False
		"""
		return self.match(block, START_QUOTE_TEXT_PATTERN)

	def matchLinkText(self, block):
		""" determines if a block starts with linked text
		>>> m = Matcher()
		>>> bool(m.matchLinkText("[yup](http://example.com)"))
		True
		>>> bool(m.matchLinkText("**nope, this is bold**"))
		False
		"""
		return self.match(block, START_LINK_TEXT_PATTERN)

	def matchPlainText(self, block):
		""" !!! can't determine if matches, but 
		    gets the matching plaintext !!!  """
		return self.match(block, START_PLAIN_TEXT_PATTERN)

	def matchImage(self, block):
		""" determines if a block starts with an image
		>>> m = Matcher()
		>>> bool(m.matchImage("![cats](http://imgur.com/cat.jpg)"))
		True
		>>> bool(m.matchImage("**nope, this is bold**"))
		False
		"""
		return self.match(block, START_IMAGE_PATTERN)

	def matchInlineEquation(self, block):
		""" determines if a block starts with an equation
		>>> m = Matcher()
		>>> bool(m.matchInlineEquation("y = m * x + b"))
		True
		>>> bool(m.matchInlineEquation("It's as simple as 2 + 2 = 4"))
		False
		"""
		return self.match(block, START_EQUATION_PATTERN)

class Match(object):

	def __init__(self, match):
		self.match = match

class BoldItalicTextMatch(Match):

	def text(self):
		return self.match.groups()[0]
		
	def end(self):
		return self.match.end()

class BoldTextMatch(Match):

	def text(self):
		return self.match.groups()[0]
		
	def end(self):
		return self.match.end()

class ItalicTextMatch(Match):

	def text(self):
		return self.match.groups()[0]
		
	def end(self):
		return self.match.end()

class StrikethroughTextMatch(Match):

	def text(self):
		return self.match.groups()[0]
		
	def end(self):
		return self.match.end()

class UnderlineTextMatch(Match):

	def text(self):
		return self.match.groups()[0]
		
	def end(self):
		return self.match.end()

class QuoteTextMatch(Match):

	def text(self):
		return self.match.groups()[0]
		
	def end(self):
		return self.match.end()

class LinkTextMatch(Match):

	def text(self):
		return self.match.groups()[0]

	def url(self):
		return self.match.groups()[1]
		
	def end(self):
		return self.match.end()

class ImageMatch(Match):

	def text(self):
		return self.match.groups()[0]

	def path(self):
		return self.match.groups()[1]
		
	def end(self):
		return self.match.end()

class InlineEquationMatch(Match):

	def equation(self):
		""" gets the equation string """
		block = self.match.string
		equationStart = self.match.start()
		equationEnd = self.match.end()
		return block[equationStart:equationEnd]

	def end(self):
		return self.match.end()

class PlainTextMatch(Match):

	def text(self):
		return self.match.groups()[0]
		
	def end(self):
		return len(self.text())

class HeadingMatch(Match):

	def text(self):
		block = self.match.string
		return str.split(block, "\n")[0]

class SubHeadingMatch(Match):

	def text(self):
		block = self.match.string
		return str.split(block, "\n")[0]

class SubSubHeadingMatch(Match):

	def text(self):
		block = self.match.string
		pat = re.compile(r"^(\#+) (.+) \1")
		match = pat.search(block)
		return match.groups()[1]

	def level(self):
		block = self.match.string
		match = re.match(r"^#+", block)
		return len(match.group())
		
class TableMatch(Match):

	def tableRowItems(self, row):
		items = row.split("|")
		items = filter(lambda x: x.strip(), items)
		return map(lambda x: x.strip(), items)

	def tableHeaders(self):
		""" gets a list of heading elements """
		block = self.match.string
		firstLine = block.split("\n")[0]	
		return self.tableRowItems(firstLine)

	def tableItems(self):
		""" get a 2D list of items """
		block = self.match.string
		lines = block.split("\n")
		lines = lines[2:] # remove first two rows (header and separator)
		return map(self.tableRowItems, lines)

class OrderedListMatch(Match):

	def listItems(self):
		""" gets the list of items """
		block = self.match.string
		itemRegex = r"(?<=\d\. )(.+)(?=(?:\n|$))"
		return re.findall(itemRegex, block)

class UnorderedListMatch(Match):

	def listItems(self):
		""" gets the list of items """
		block = self.match.string
		itemRegex = r"(?<=(?:\*|\-) )(.+)(?=(?:\n|$))"
		return re.findall(itemRegex, block)

class BlockEquationMatch(Match):

	def equation(self):
		block = self.match.string
		equationStart = self.match.start()
		equationEnd = self.match.end()
		return block[equationStart:equationEnd]

if __name__ == "__main__":
	import doctest
	doctest.testmod()
