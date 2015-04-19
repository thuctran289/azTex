import re
from Element import *
from Regex import *
from Matcher import Matcher

class Container(object):
	""" simple class to hold data
		makes if else look better"""

	def __init__(self, data=None):
		self.data = data

	def set(self, data):
		self.data = data
		return data
	
	def get(self):
		return self.data

class Parser(object):

	def __init__(self):
		self.matcher = Matcher()

	def parseBlock(self, block):
		if self.matcher.matchHeading(block):
			return HeadingElement(self.headingText(block), 1)
		elif self.matcher.matchSubHeading(block):
			return HeadingElement(self.subHeadingText(block), 2) 
		elif self.matcher.matchSubSubHeading(block):
			return HeadingElement(self.subSubHeadingText(block), self.subSubHeadingLevel(block)) 
		elif self.matcher.matchTable(block):
			return TableElement(self.tableHeaders(block), self.tableItems(block))
		elif self.matcher.matchOrderedList(block):
			return OrderedListElement(self.orderedListItems(block))
		elif self.matcher.matchUnorderedList(block):
			return UnorderedListElement(self.unorderedListItems(block))
		else:
			return ParagraphElement(self.parseText(block))

	def headingText(self, block):
		""" gets the text out of a heading block
		>>> p = Parser()
		>>> res = p.headingText("aztex\\n====")
		'aztex'

		>>> p.headingText("Harry Potter\\n=====")
		'Harry Potter'
		"""
		text = str.split(block, "\n")[0]
		return self.parseText(text)

	def subHeadingText(self, block):
		""" gets the text out of a subheading block
		>>> p = Parser()
		>>> p.subHeadingText("aztex\\n-----")
		'aztex'

		>>> p.subHeadingText("Harry Potter\\n-----")
		'Harry Potter'
		"""
		text = str.split(block, "\n")[0]
		return self.parseText(text)

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
		text = match.groups()[1]
		return self.parseText(text)

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

		return TABLE_PATTERN.match(block) != None

	def tableRowItems(self, row):
		items = row.split("|")
		items = filter(lambda x: x.strip(), items)
		return map(self.parseBlock, items)
		
	def tableHeaders(self, block):
		""" gets a list of heading elements """
		firstLine = block.split("\n")[0]	
		return self.tableRowItems(firstLine)

	def tableItems(self, block):
		""" get a 2D list of items """
		lines = block.split("\n")
		lines = lines[2:] # remove first two rows (header and separator)
		return map(self.tableRowItems, lines)

	def orderedListItems(self, block):
		""" gets the list of items """
		itemRegex = r"(?<=\d\. )(.+)(?=(?:\n|$))"
		items = re.findall(itemRegex, block)
		return map(self.parseBlock, items)

	def unorderedListItems(self, block):
		""" gets the list of items """
		itemRegex = r"(?<=(?:\*|\-) )(.+)(?=(?:\n|$))"
		items = re.findall(itemRegex, block)
		return map(self.parseBlock, items)

	def parseText(self, block):
		""" gets the elements within a paragraph
		"""
		container = Container()
		components = []
		while block:
			if container.set(self.matcher.matchBoldText(block)):
				match = container.get()
				text = match.groups()[0]
				end = match.end()
				block = block[end:]

				element = self.parseText(text)
				components.append(BoldElement(element))

			elif container.set(self.matcher.matchItalicText(block)):
				match = container.get()
				text = match.groups()[0]
				end = match.end()
				block = block[end:]

				element = self.parseText(text)
				components.append(ItalicElement(element))

			elif container.set(self.matcher.matchStrikethroughText(block)):
				match = container.get()
				text = match.groups()[0]
				end = match.end()
				block = block[end:]

				element = self.parseText(text)
				components.append(StrikethroughElement(element))

			elif container.set(self.matcher.matchUnderlineText(block)):
				match = container.get()
				text = match.groups()[0]
				end = match.end()
				block = block[end:]

				element = self.parseText(text)
				components.append(UnderlineElement(element))

			elif container.set(self.matcher.matchQuoteText(block)):
				match = container.get()
				text = match.groups()[0]
				end = match.end()
				block = block[end:]

				element = self.parseText(text)
				components.append(QuoteElement(element))

			elif container.set(self.matcher.matchLinkText(block)):
				match = container.get()
				text = match.groups()[0]
				url = match.groups()[1]
				end = match.end()
				block = block[end:]

				element = self.parseText(text)
				components.append(LinkElement((element, url)))

			elif container.set(self.matcher.matchImage(block)):
				match = container.get()
				text = match.groups()[0]
				url = match.groups()[1]
				end = match.end()
				block = block[end:]

				element = self.parseText(text)
				components.append(ImageElement((element, url)))

			elif container.set(self.matcher.matchPlainText(block)):
				match = container.get()
				text = match.groups()[0]
				end = len(text)
				block = block[end:]
				
				components.append(TextElement(text))


		return components

if __name__ == "__main__":
	import doctest
	doctest.testmod()
