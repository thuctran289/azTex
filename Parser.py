import re
from Element import *
from Regex import *

class Parser(object):

	def parse(self, block):
		if self.isHeading(block):
			return HeadingElement(self.headingText(block), 1)
		elif self.isSubHeading(block):
			return HeadingElement(self.subHeadingText(block), 2) 
		elif self.isSubSubHeading(block):
			return HeadingElement(self.subSubHeadingText(block), self.subSubHeadingLevel(block)) 
		elif self.isTable(block):
			return TableElement(self.tableHeaders(block), self.tableItems(block))
		elif self.isOrderedList(block):
			return OrderedListElement(self.orderedListItems(block))
		elif self.isUnorderedList(block):
			return UnorderedListElement(self.unorderedListItems(block))
		else:
			return ParagraphElement(self.paragraphComponents(block))

	def isHeading(self, block):
		""" determines if a block is a header
		ie: 
				aztex
				=====

		>>> p = Parser()
		>>> p.isHeading("aztex\\n=====") 
		True

		>>> p.isHeading('Harry Potter\\n====')
		True

		>>> p.isHeading('Voldemort\\n=')
		False
		"""
		return HEADING_PATTERN.match(block) != None

	def headingText(self, block):
		""" gets the text out of a heading block
		>>> p = Parser()
		>>> p.headingText("aztex\\n====")
		'aztex'

		>>> p.headingText("Harry Potter\\n=====")
		'Harry Potter'
		"""
		return str.split(block, "\n")[0]

	def isSubHeading(self, block):
		""" determines if a block is a subheader
		ie: 
				aztex
				-----

		>>> p = Parser()
		>>> p.isSubHeading("aztex\\n=====") 
		False

		>>> p.isSubHeading("aztex\\n-----") 
		True

		>>> p.isSubHeading("Harry Potter\\n-----")
		True

		>>> p.isSubHeading('Voldemort\\n-')
		False
		"""
		return SUB_HEADING_PATTERN.match(block) != None

	def subHeadingText(self, block):
		""" gets the text out of a subheading block
		>>> p = Parser()
		>>> p.subHeadingText("aztex\\n-----")
		'aztex'

		>>> p.subHeadingText("Harry Potter\\n-----")
		'Harry Potter'
		"""
		return str.split(block, "\n")[0]

	def isSubSubHeading(self, block):
		""" determines if a block is a subsubheader
		ie: 
				#### aztex ####

		>>> p = Parser()
		>>> p.isSubSubHeading("## aztex ##") 
		True

		>>> p.isSubSubHeading("#### aztex ####") 
		True

		>>> p.isSubSubHeading("# Harry Potter #")
		True

		>>> p.isSubSubHeading('### Voldemort #')
		False

		>>> p.isSubSubHeading('## Ron')
		False
		"""
		return SUB_SUB_HEADING_PATTERN.match(block) != None

	def subSubHeadingText(self, block):
		""" gets the text out of a subsubheading block
		>>> p = Parser()
		>>> p.subSubHeadingText("## aztex ##")
		'aztex'

		>>> p.subSubHeadingText("### Harry Potter ###")
		'Harry Potter'
		"""
		pat = re.compile(r"^(\#+) (.+) \1")
		match = pat.search(block)
		return match.groups()[1]

	def subSubHeadingLevel(self, block):
		""" gets the heading level
		>>> p = Parser()
		>>> p.subSubHeadingLevel("## aztex ##")
		2

		>>> p.subSubHeadingLevel("##### aztex #####")
		5
		"""
		match = re.match(r"^#+", block)
		return len(match.group())

	def tableString(self):
		return "| id | name |     email    |\n\
				|----|------|--------------|\n\
				| 1  | bob  | bob@mail.com |\n\
				| 2  | tom  | tom@mail.com |\n\
				| 3  | ron  | ron@mail.com |"

	def isTable(self, block):
		""" determines if the block is a table
		>>> p = Parser()
		>>> p.isTable("| cat |")
		False
		>>> p.isTable(p.tableString())
		True
		"""
		return TABLE_PATTERN.match(block) != None

	def tableRowItems(self, row):
		items = row.split("|")
		return filter(lambda x: x.strip(), items)
		
	def tableHeaders(self, block):
		""" gets a list of heading elements
		>>> p = Parser()
		>>> p.tableHeaders(p.tableString())
		[' id ', ' name ', '     email    ']
		"""
		firstLine = block.split("\n")[0]	
		return self.tableRowItems(firstLine)

	def tableItems(self, block):
		""" get a 2D list of items
		>>> p = Parser()
		>>> p.tableItems(p.tableString())
		[[' 1  ', ' bob  ', ' bob@mail.com '], [' 2  ', ' tom  ', ' tom@mail.com '], [' 3  ', ' ron  ', ' ron@mail.com ']]
		"""
		lines = block.split("\n")
		lines = lines[2:] # remove first two rows (header and separator)
		return map(self.tableRowItems, lines)


	def isOrderedList(self, block):
		""" determines if the block is an ordered list
		>>> p = Parser()
		>>> p.isOrderedList("1. eggs\\n2. bread\\n3. rice")
		True
		"""
		return ORDERED_LIST_PATTERN.match(block) != None

	def orderedListItems(self, block):
		""" gets the list of items
		>>> p = Parser()
		>>> p.orderedListItems("1. cats\\n2. dogs\\n3. mice")
		['cats', 'dogs', 'mice']
		"""
		itemRegex = r"(?<=\d\. )(.+)(?=(?:\n|$))"
		return re.findall(itemRegex, block)

	def isUnorderedList(self, block):
		""" determines if the block is an ordered list
		>>> p = Parser()
		>>> p.isUnorderedList("* eggs\\n* bread\\n* rice")
		True
		>>> p.isUnorderedList("- eggs\\n- bread\\n- rice")
		True
		"""
		return UNORDERED_LIST_PATTERN.match(block) != None

	def unorderedListItems(self, block):
		""" gets the list of items
		>>> p = Parser()
		>>> p.unorderedListItems("* cats\\n* dogs\\n* mice")
		['cats', 'dogs', 'mice']
		>>> p.unorderedListItems("- apple\\n- orange\\n- banana")
		['apple', 'orange', 'banana']
		"""
		itemRegex = r"(?<=(?:\*|\-) )(.+)(?=(?:\n|$))"
		return re.findall(itemRegex, block)

	def paragraphComponents(self, block):
		""" gets the elements within a paragraph
		"""
		components = []
		while block:
			if self.startsWithBoldText(block):
				match = START_BOLD_TEXT_PATTERN.match(block)
				text = match.groups()[0]
				end = match.end()
				block = block[end:]

				components.append(BoldElement(text))

			elif self.startsWithItalicText(block):
				match = START_ITALIC_TEXT_PATTERN.match(block)
				text = match.groups()[0]
				end = match.end()
				block = block[end:]

				components.append(ItalicElement(text))

			elif self.startsWithStrikethroughText(block):
				match = START_STRIKETHROUGH_TEXT_PATTERN.match(block)
				text = match.groups()[0]
				end = match.end()
				block = block[end:]

				components.append(StrikethroughElement(text))

			elif self.startsWithUnderlineText(block):
				match = START_UNDERLINE_TEXT_PATTERN.match(block)
				text = match.groups()[0]
				end = match.end()
				block = block[end:]

				components.append(UnderlineElement(text))

			elif self.startsWithQuoteText(block):
				match = START_QUOTE_TEXT_PATTERN.match(block)
				text = match.groups()[0]
				end = match.end()
				block = block[end:]

				components.append(QuoteElement(text))

			elif self.startsWithLinkText(block):
				match = START_LINK_TEXT_PATTERN.match(block)
				text = match.groups()[0]
				url = match.groups()[1]
				end = match.end()
				block = block[end:]

				components.append(LinkElement((text, url)))

			else:
				match = START_PLAIN_TEXT_PATTERN.match(block)
				text = match.groups()[0]
				end = len(text)
				block = block[end:]
				
				components.append(TextElement(text))


		return components

	def startsWithBoldText(self, block):
		""" determines if a block starts with bold text
		>>> p = Parser()
		>>> p.startsWithBoldText("**yup, it does**")
		True
		>>> p.startsWithBoldText("*nope, this is italic*")
		False
		"""
		return START_BOLD_TEXT_PATTERN.match(block) != None

	def boldText(self, block):
		""" gets the text in bold at the start of a block
		>>> p = Parser()
		>>> p.boldText("**aztex**")
		'aztex'
		"""
		match = START_BOLD_TEXT_PATTERN.match(block)
		return match.groups()[0]

	def startsWithItalicText(self, block):
		""" determines if a block starts with italic text
		>>> p = Parser()
		>>> p.startsWithItalicText("*yup, it does*")
		True
		>>> p.startsWithItalicText("**nope, this is bold**")
		False
		"""
		return START_ITALIC_TEXT_PATTERN.match(block) != None

	def italicText(self, block):
		pass

	def startsWithStrikethroughText(self, block):
		""" determines if a block starts with strike through text
		>>> p = Parser()
		>>> p.startsWithStrikethroughText("--yup, it does--")
		True
		>>> p.startsWithStrikethroughText("**nope, this is bold**")
		False
		"""
		return START_STRIKETHROUGH_TEXT_PATTERN.match(block) != None

	def startsWithUnderlineText(self, block):
		""" determines if a block starts with underlined text
		>>> p = Parser()
		>>> p.startsWithUnderlineText("_yup, it does_")
		True
		>>> p.startsWithUnderlineText("**nope, this is bold**")
		False
		"""
		return START_UNDERLINE_TEXT_PATTERN.match(block) != None

	def startsWithQuoteText(self, block):
		""" determines if a block starts with quoted text
		>>> p = Parser()
		>>> p.startsWithQuoteText("``yup, it does\'\'")
		True
		>>> p.startsWithQuoteText("**nope, this is bold**")
		False
		"""
		return START_QUOTE_TEXT_PATTERN.match(block) != None

	def startsWithLinkText(self, block):
		""" determines if a block starts with linked text
		>>> p = Parser()
		>>> p.startsWithLinkText("[yup](http://example.com)")
		True
		>>> p.startsWithLinkText("**nope, this is bold**")
		False
		"""
		return START_LINK_TEXT_PATTERN.match(block) != None



if __name__ == "__main__":
	import doctest
	doctest.testmod()
