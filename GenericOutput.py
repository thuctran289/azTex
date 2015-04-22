import InternalRepresentation
import Element

class GenericOutput(object):
	"""generates an output document given some internal respresentation"""

	def __init__(self):
		pass
	#def to_code(self, internal_reprentation):
	#	pass

	def generate_doc():
		pass

	
	def to_code(self, elements):
			if(not hasattr(elements, '__iter__')):				
				element = elements
				e_type = element.get_type()

				if e_type == 'Unordered List':
					return self.unordered_list(element)
				elif e_type == 'Ordered List':
					return self.ordered_list(element)
				elif e_type == "Paragraph":
					return self.paragraph(element)
				elif e_type == "Image":
					pass
				elif e_type == 'Text':
					return self.text(element)
				elif e_type == 'Link':
					return self.link(element)
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
					return self.table(element)

			else:
				for element in elements:
					e_type = element.get_type()

					if e_type == 'Unordered List':
						pass
					elif e_type == 'Ordered List':
						pass
					elif e_type == "Image":
						pass
					elif e_type == 'Text':
						return self.text(element)
					elif e_type == 'Link':
						return self.link(element)
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
						return self.table(element)



