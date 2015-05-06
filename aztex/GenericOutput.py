import InternalRepresentation
from Element import *

class GenericOutput(object):
	"""generates an output document given some internal respresentation"""

	def doc_header(self):
		""" returns the string that should precede the document """
		pass

	def doc_footer(self):
		""" returns the string that should follow the document """
		pass

	def generate_doc(self, representation):
		""" generates a string out of the representation """
		doc = ""
		doc += self.doc_header()

		for element in representation:
			doc += self.to_code(element)

		doc += self.doc_footer()
		return doc

	def to_code(self, elements):
		"""Recursive function that takes in an element, figures out what kind of element it is, than passes the element along to the corresponding function to generate the appropriate 
		output. 
		"""
		if(not hasattr(elements, '__iter__')):				
			element = elements
			e_type = type(element)

			func = self.element_dict().get(e_type)
			return func(element)

		else:
			els = map(self.to_code, elements)
			return ''.join(els)

	def element_dict(self):
		""" returns the dictionary of elements and functions """
		return { UnorderedListElement: 		self.unordered_list,
				 OrderedListElement: 		self.ordered_list,
				 TextElement: 				self.text,
				 ParagraphElement: 			self.paragraph,
				 LinkElement: 				self.link,
				 ImageElement: 				self.image,
				 InlineEquationElement: 	self.inline_equation,
				 BoldItalicElement: 		self.bold_italic,
				 BoldElement: 				self.bold,
				 ItalicElement: 			self.italic,
				 UnderlineElement: 			self.underline,
				 StrikethroughElement: 		self.strikethrough,
				 QuoteElement: 				self.quote,
				 HeadingElement: 			self.heading,
				 TableElement: 				self.table,
				 BlockEquationElement: 		self.block_equation }
