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
		""" set data and allow for evaluation """
		self.data = data
		return data
	
	def get(self):
		""" get the data """
		return self.data

class Parser(object):
	""" parses blocks of input and returns Elements """

	def __init__(self):
		self.matcher = Matcher()
		self.equationParser = EquationParser()

	def parseBlock(self, block):
		""" parse a block of input and return the corresponding Element """
		container = Container()
		if container.set(self.matcher.matchHeading(block)):
			match = container.get()
			em = HeadingMatch(match)
			subelement = self.parseText(em.text())
			element = HeadingElement(subelement, 1)

		elif container.set(self.matcher.matchSubHeading(block)):
			match = container.get()
			em = SubHeadingMatch(match)
			subelement = self.parseText(em.text())
			element = HeadingElement(subelement, 2) 

		elif container.set(self.matcher.matchSubSubHeading(block)):
			match = container.get()
			em = SubSubHeadingMatch(match)
			subelement = self.parseText(em.text())
			element = HeadingElement(subelement, em.level()) 

		elif container.set(self.matcher.matchTable(block)):
			match = container.get()
			em = TableMatch(match)
			tableHeaders = map(self.parseBlock, em.tableHeaders())
			tableItems = map(lambda row: map(self.parseBlock, row), em.tableItems())
			element = TableElement(tableHeaders, tableItems)

		elif container.set(self.matcher.matchOrderedList(block)):
			match = container.get()
			em = OrderedListMatch(match)
			listItems = map(self.parseBlock, em.listItems())
			element = OrderedListElement(listItems)

		elif container.set(self.matcher.matchUnorderedList(block)):
			match = container.get()
			em = UnorderedListMatch(match)
			listItems = map(self.parseBlock, em.listItems())
			element = UnorderedListElement(listItems)

		elif container.set(self.matcher.matchBlockEquation(block)):
			match = container.get()
			em = BlockEquationMatch(match)
			equationStr = em.equation()
			equation = self.equationParser.parseEquation(equationStr)
			element = BlockEquationElement(equation)

		else:
			element = ParagraphElement(self.parseText(block))

		return element

	def parseText(self, block):
		""" gets the elements within a paragraph """
		components = []
		container = Container()
		while block:

			if container.set(self.matcher.matchBoldItalicText(block)):
				match = container.get()
				em = BoldItalicTextMatch(match)
				subelement = self.parseText(em.text())
				element = BoldItalicElement(subelement)

			elif container.set(self.matcher.matchBoldText(block)):
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
				element = ImageElement(em.path(), em.caption())

			elif container.set(self.matcher.matchInlineEquation(block)):
				match = container.get()
				em = InlineEquationMatch(match)
				equationStr = em.equation()
				equation = self.equationParser.parseEquation(equationStr)
				element = InlineEquationElement(equation)

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
