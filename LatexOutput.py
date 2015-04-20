from Element import *
from pylatex import *
from GenericOutput import *

class LatexOutput(GenericOutput):
	def __init__(self):
		super(LatexOutput, self).__init__()

	def to_doc(self, representation):
		pass
	
	def to_code(self, elements):

			if(not hasattr(elements, '__iter__')):				
				element = elements
				e_type = element.get_type()

				if e_type == 'Unordered List':
					pass
				elif e_type == 'Ordered List':
					pass
				elif e_type == "Paragraph":
					return self.paragraph(element)
				elif e_type == "Image":
					pass
				elif e_type == 'Text':
					return self.text(element)
				elif e_type == 'Link':
					pass
				elif e_type == 'Equation':
					pass
				elif e_type == 'Bold':
					return self.bold(element)
				elif e_type == 'Italic':
					return self.italic(element)
				elif e_type == 'Underline':
					return self.underline(element)
				elif e_type == 'Strikethrough':
					return self.strikethrough(element)
				elif e_type == 'Quote':
					return self.quote(element)
				elif e_type == "Heading":
					return self.heading(element)
				elif e_type == "Table":
					pass

			else:
				for element in elements:
					e_type = element.get_type()

					if e_type == 'Unordered List':
						pass
					elif e_type == 'Ordered List':
						pass
					elif e_type == "Paragraph":
						pass
					elif e_type == "Image":
						pass
					elif e_type == 'Text':
						return self.text(element)
					elif e_type == 'Link':
						pass
					elif e_type == 'Equation':
						pass
					elif e_type == 'Bold':
						return self.bold(element)
					elif e_type == 'Italic':
						return self.italic(element)
					elif e_type == 'Underline':
						return self.underline(element)
					elif e_type == 'Strikethrough':
						return self.strikethrough(element)
					elif e_type == 'Quote':
						return self.quote(element)
					elif e_type == "Heading":
						return self.heading(element)
					elif e_type == "Table":
						pass


	def unordered_list(self, element):
		pass
	def ordered_list(self, element):
		pass
	def text(self, element):
		return element.get_elements()
	def link(self, element):
		"""
		Need to clarify how this will work later on. 
		"""
		pass
	def equation(self, element):
		pass
	def bold(self, element):
		return "\\textbf{" + self.to_code(element.get_elements()) + "}"
	def italic(self, element):
		return "\\textit{" + self.to_code(element.get_elements()) + "}"
	def underline(self, element):
		return "\\underline{" + self.to_code(element.get_elements()) + "}"
	def strikethrough(self, element):
		return "\\sout{" + self.to_code(element.get_elements()) + "}"
	def quote(self, element):
		return "``" + self.to_code(element.get_elements()) + "''"
	def heading(self, element): 
		return "\\section{" + self.to_code(element.get_elements()) + "}"
	def paragraph(self, element):
		doc = []
		elements = element.get_elements()
		for obje in elements:
			if hasattr(obje, 'str'):
				doc.extend(obje)
			else:
				doc.append(self.to_code(obje))
		return ''.join(doc)


if __name__ == "__main__":
	uolist = UnorderedListElement(['these are words', 'more words', 'omg even more!'])
	text = TextElement("Hello")
	bolded = BoldElement(text)
	italics = ItalicElement(bolded)
	head = HeadingElement(TextElement("HELLO"),4)
	print text
	print head.get_elements().get_elements()
	print uolist
	print type(uolist)
	print uolist.get_type()
	print uolist.get_elements()
	A = LatexOutput()
	print type(A)
	print A.to_code(italics)
