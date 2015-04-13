class InternalRepresentation:
	""" Contains the internal representation for the document and how it looks"""

	def __init__(self):
		self.internal_elements = []

	def add_line(self, list_of_elements):
		self.internal_elements.append(list_of_elements)

	def get_line(self, line_number):
		return self.internal_elements[line_number]

	def get_list(self):
		return self.internal_elements

	def get_element(self,line_number, element_number):
		return self.internal_elements[line_number][element_number]

	def add_element(self, element, line_number = None):
		if line_number == None:
			self.internal_elements.append(element)
		else:
			self.internal_elements[line_number].append(element)


