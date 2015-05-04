"""
@author: jovanduy
"""

class Element(object):
	""" A single component of the document """
	def __init__(self, subelements):
		""" Initializes an Element object
		"""
		self.subelements = subelements

	def __str__(self):
		subs = ""
		if isinstance(self.subelements, list):
			for element in self.subelements:
				subs += str(element) 
		else:
			subs = self.subelements

		return '(%s: %s)' % (type(self), subs)

	def get_elements(self):
		"""
		>>> element = Element('this subelement is text')
		>>> element.get_elements()
		'this subelement is text'
		"""
		return self.subelements


class ListElement(Element):
	""" An Element object that represents a list """
	def __init__(self, subelements):
		super(ListElement, self).__init__(subelements)

class UnorderedListElement(ListElement):
	""" An Element object that represents an unordered list """
	def __init__(self, subelements):
		super(ListElement, self).__init__(subelements)

class OrderedListElement(ListElement):
	""" An Element object that represents an ordered list """
	def __init__(self, subelements):
		super(ListElement, self).__init__(subelements)

class TextElement(Element):
	""" An Element object that represents text """
	def __init__(self, subelements):
		super(TextElement, self).__init__(subelements)

class ParagraphElement(Element):
	""" An Element object that represents text """
	def __init__(self, subelements):
		super(ParagraphElement, self).__init__(subelements)

class LinkElement(Element):
	""" An Element object that represents a link """
	def __init__(self, url, element):
		super(LinkElement, self).__init__((url, element))
		self.url = url
		self.element = element

class ImageElement(Element):
	""" An Element object that represents an image """
	def __init__(self, path, caption):
		super(ImageElement, self).__init__((path, caption))
		self.path = path
		self.caption = caption

class InlineEquationElement(Element):
	""" An Element object that represents an equation """
	def __init__(self, equation):
		super(InlineEquationElement, self).__init__(equation)
		self.equation = equation

class BoldItalicElement(Element):
	""" An Element object that represents bolded text """
	def __init__(self, subelements):
		super(BoldItalicElement, self).__init__(subelements)

class BoldElement(Element):
	""" An Element object that represents bolded text """
	def __init__(self, subelements):
		super(BoldElement, self).__init__(subelements)

class ItalicElement(Element):
	""" An Element object that represents italicized text """
	def __init__(self, subelements):
		super(ItalicElement, self).__init__(subelements)

class UnderlineElement(Element):
	""" An Element object that represents underlined text """
	def __init__(self, subelements):
		super(UnderlineElement, self).__init__(subelements)

class StrikethroughElement(Element):
	""" An Element object that represents strikethrough text """
	def __init__(self, subelements):
		super(StrikethroughElement, self).__init__(subelements)

class QuoteElement(Element):
	""" An Element object that represents text surrounded by quotations """
	def __init__(self, subelements):
		super(QuoteElement, self).__init__(subelements)

class HeadingElement(Element):
	""" An Element object that represents a section heading """
	def __init__(self, subelements, level):
		super(HeadingElement, self).__init__(subelements)
		self.level = level

class TableElement(Element):
	""" An Element object that represents a table """
	def __init__(self, headers, items):
		super(TableElement, self).__init__(None)
		self.headers = headers
		self.items = items

	def __str__(self):
		headers = ', '.join(map(lambda x: str(x), self.headers))
		items = ""
		for row in self.items:
			items += "\t"
			items += ", ".join(map(lambda x: str(x), row))
			items += '\n'
		return '%s:\n\t%s\n%s' % (type(self), headers, items)

class BlockEquationElement(Element):
	""" An Element object that represents an equation """
	def __init__(self, equation):
		super(BlockEquationElement, self).__init__(equation)
		self.equation = equation

if __name__ == "__main__":
	import doctest
	doctest.testmod()
