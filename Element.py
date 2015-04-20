"""
@author: jovanduy
"""

class Element(object):
	""" A single component of the document """
	def __init__(self, element_type, subelements):
		""" Initializes an Element object
			e_type = type of Element
		"""
		self.element_type = element_type
		self.subelements = subelements

	def __str__(self):
		subs = ""
		for element in self.subelements:
			subs += str(element) 
		return '(%s: %s)' % (self.element_type, subs)

	def get_type(self):
		""" Returns the element_type of self

		>>> element = Element('e_type', 'this subelement is text')
		>>> element.get_type()
		'e_type'
		"""
		return self.element_type

	def get_elements(self):
		""" Returns the element_type of self

		>>> element = Element('e_type', 'this subelement is text')
		>>> element.get_elements()
		'this subelement is text'
		"""
		return self.subelements


class ListElement(Element):
	""" An Element object that represents a list """
	def __init__(self, subelements):
		super(ListElement, self).__init__("List", subelements)

class UnorderedListElement(ListElement):
	""" An Element object that represents an unordered list """
	def __init__(self, subelements):
		super(ListElement, self).__init__("Unordered List", subelements)

class OrderedListElement(ListElement):
	""" An Element object that represents an ordered list """
	def __init__(self, subelements):
		super(ListElement, self).__init__("Ordered List", subelements)

class TextElement(Element):
	""" An Element object that represents text """
	def __init__(self, subelements):
		super(TextElement, self).__init__("Text", subelements)

class ParagraphElement(Element):
	""" An Element object that represents text """
	def __init__(self, subelements):
		super(ParagraphElement, self).__init__("Paragraph", subelements)

class LinkElement(Element):
	""" An Element object that represents a link """
	def __init__(self, url, element):
		super(LinkElement, self).__init__("Link", (url, element))
		self.url = url
		self.element = element

class ImageElement(Element):
	""" An Element object that represents an image """
	def __init__(self, path, element):
		super(ImageElement, self).__init__("Image", (path, element))
		self.path = path
		self.element = element

class EquationElement(Element):
	""" An Element object that represents an equation """
	def __init__(self, subelements):
		super(EquationElement, self).__init__("Equation", subelements)

class BoldElement(Element):
	""" An Element object that represents bolded text """
	def __init__(self, subelements):
		super(BoldElement, self).__init__("Bold", subelements)

class ItalicElement(Element):
	""" An Element object that represents italicized text """
	def __init__(self, subelements):
		super(ItalicElement, self).__init__("Italic", subelements)

class UnderlineElement(Element):
	""" An Element object that represents underlined text """
	def __init__(self, subelements):
		super(UnderlineElement, self).__init__("Underline", subelements)

class StrikethroughElement(Element):
	""" An Element object that represents strikethrough text """
	def __init__(self, subelements):
		super(StrikethroughElement, self).__init__("Strikethrough", subelements)

class QuoteElement(Element):
	""" An Element object that represents text surrounded by quotations """
	def __init__(self, subelements):
		super(QuoteElement, self).__init__("Quote", subelements)

class HeadingElement(Element):
	""" An Element object that represents a section heading """
	def __init__(self, subelements, level):
		super(HeadingElement, self).__init__("Heading", subelements)
		self.level = level

class TableElement(Element):
	""" An Element object that represents a table """
	def __init__(self, headers, items):
		super(TableElement, self).__init__("Table", None)
		self.headers = headers
		self.items = items

	def __str__(self):
		headers = ', '.join(map(lambda x: str(x), self.headers))
		items = ""
		for row in self.items:
			items += "\t"
			items += ", ".join(map(lambda x: str(x), row))
			items += '\n'
		return '%s:\n\t%s\n%s' % (self.element_type, headers, items)

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	uolist = LinkElement(['these are words', 'more words', 'omg even more!'])
	print uolist
	print type(uolist)
	print uolist.get_type()
	print uolist.get_elements()
	# text = TextElement('these are words yay')
	# print text
	# print type(text)

	# print text.get_type()
	# print text.get_elements()
