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
		return '%s: %s' % (self.element_type, self.subelements)

	def get_type(self):
		""" Returns the 
		"""
		return self.element_type

	def get_elements(self):
		return self.subelements


class ListElement(Element):
	""" An Element object that represents a list """
	def __init__(self, subelements):
		super(ListElement, self).__init__("List", subelements)

class UnorderedListElement(ListElement):
	""" An Element object that represents an unordered list """
	def __init__(self, subelements):
		super(Element, self).__init__("Unordered List", subelements)

class OrderedListElement(ListElement):
	""" An Element object that represents an ordered list """
	def __init__(self, subelements):
		super(Element, self).__init__("Ordered List", subelements)

class TextElement(Element):
	""" An Element object that represents text """
	def __init__(self, subelements):
		super(TextElement, self).__init__("Text", subelements)

class LinkElement(Element):
	""" An Element object that represents a link """
	def __init__(self, subelements):
		super(LinkElement, self).__init__("Link", subelements)

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
