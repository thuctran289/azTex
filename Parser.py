import re
from Element import *
from Regex import *
from Matcher import *
from Equation import EquationParser

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
		container = Container()
		if container.set(self.matcher.matchHeading(block)):
			match = container.get()
			em = HeadingMatch(match)
			element = self.parseText(em.text())
			return HeadingElement(element, 1)

		elif container.set(self.matcher.matchSubHeading(block)):
			match = container.get()
			em = SubHeadingMatch(match)
			element = self.parseText(em.text())
			return HeadingElement(element, 2) 

		elif container.set(self.matcher.matchSubSubHeading(block)):
			match = container.get()
			em = SubSubHeadingMatch(match)
			element = self.parseText(em.text())
			return HeadingElement(element, em.level()) 

		elif container.set(self.matcher.matchTable(block)):
			match = container.get()
			em = TableMatch(match)
			tableHeaders = map(self.parseText, em.tableHeaders())
			tableItems = map(lambda row: map(self.parseText, row), em.tableItems())
			return TableElement(tableHeaders, tableItems)

		elif container.set(self.matcher.matchOrderedList(block)):
			match = container.get()
			em = OrderedListMatch(match)
			listItems = map(self.parseText, em.listItems())
			return OrderedListElement(listItems)

		elif container.set(self.matcher.matchUnorderedList(block)):
			match = container.get()
			em = UnorderedListMatch(match)
			listItems = map(self.parseText, em.listItems())
			return UnorderedListElement(listItems)

		
	#	elif container.set(self.matcher.matchEquation(block)):
	#		match = container.get()
	#		em = EquationMatcher(match)
	#		listItems = map(self.parseText, em.listItems())
	#		return EquationParser().parseEquation(block)

		else:
			return ParagraphElement(self.parseText(block))

	def parseText(self, block):
		""" gets the elements within a paragraph
		"""
		components = []
		container = Container()
		while block:
			if container.set(self.matcher.matchBoldText(block)):
				match = container.get()
				em = BoldTextMatch(match)
				subelement = self.parseText(em.text())
				element = BoldElement(subelement)

			elif container.set(self.matcher.matchItalicText(block)):
				match = container.get()
				em = ItalicTextMatch(match)
				subelement = self.parseText(em.text())
				element = ItalicElement(subelement)

			elif container.set(self.matcher.matchStrikethroughText(block)):
				match = container.get()
				em = StrikethroughTextMatch(match)
				subelement = self.parseText(em.text())
				element = StrikethroughElement(subelement)

			elif container.set(self.matcher.matchUnderlineText(block)):
				match = container.get()
				em = UnderlineTextMatch(match)
				subelement = self.parseText(em.text())
				element = UnderlineElement(subelement)

			elif container.set(self.matcher.matchQuoteText(block)):
				match = container.get()
				em = QuoteTextMatch(match)
				subelement = self.parseText(em.text())
				element = QuoteElement(subelement)

			elif container.set(self.matcher.matchLinkText(block)):
				match = container.get()
				em = LinkTextMatch(match)
				subelement = self.parseText(em.text())
				element = LinkElement(subelement, em.url())

			elif container.set(self.matcher.matchImage(block)):
				match = container.get()
				em = ImageMatch(match)
				subelement = self.parseText(em.text())
				element = ImageElement(subelement, em.path())

			elif container.set(self.matcher.matchInlineEquation(block)):
				match = container.get()
				em = InlineEquationMatch(match)
				equationStr = em.equation()
				element = EquationParser().parseEquation(equationStr)

			elif container.set(self.matcher.matchPlainText(block)):
				match = container.get()
				em = PlainTextMatch(match)
				element = TextElement(em.text())

			components.append(element)
			block = block[em.end():]

		return components

if __name__ == "__main__":
	import doctest
	doctest.testmod()
