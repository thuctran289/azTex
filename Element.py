"""
@author: jovanduy
"""

class Element(object):
	""" A single component of the document """
	def __init__(self, element_type, content):
		""" Initializes an Element object
			e_type = type of Element
		"""
		self.element_type = element_type
		self.content = content

	def get_type(self):
		return self.element_type

class ListElement(Element):
	""" An Element object that represents a list """
	def __init__(self, content):
		super(ListElement, self).__init__("List", content)

class UnorderedListElement(ListElement):
	""" An Element object that represents an unordered list """
	def __init__(self, content):
		super(UnorderedListElement, self).__init__(content)

class OrderedListElement(ListElement):
	""" An Element object that represents an ordered list """
	def __init__(self, content):
		super(OrderedListElement, self).__init__(content)

class TextElement(Element):
	""" An Element object that represents text """
	def __init__(self, content):
		super(TextElement, self).__init__("Text", content)

class LinkElement(Element):
	""" An Element object that represents a link """
	def __init__(self, content):
		super(LinkElement, self).__init__("Link", content)

class EquationElement(Element):
	""" An Element object that represents an equation """
	def __init__(self, content):
		super(EquationElement, self).__init__("Equation", content)

class BoldElement(Element):
	""" An Element object that represents bolded text """
	def __init__(self, content):
		super(BoldElement, self).__init__("Bold", content)

class ItalicElement(Element):
	""" An Element object that represents italicized text """
	def __init__(self, content):
		super(ItalicElement, self).__init__("Italic", content)

class UnderlineElement(Element):
	""" An Element object that represents underlined text """
	def __init__(self, content):
		super(UnderlineElement, self).__init__("Underline", content)

class StrikethroughElement(Element):
	""" An Element object that represents strikethrough text """
	def __init__(self, content):
		super(StrikethroughElement, self).__init__("Strikethrough", content)

class QuoteElement(Element):
	""" An Element object that represents text surrounded by quotations """
	def __init__(self, content):
		super(QuoteElement, self).__init__("Quote", content)