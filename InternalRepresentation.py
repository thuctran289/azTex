class InternalRepresentation(object):
	""" Contains the internal representation for the document and how it looks"""

	def __init__(self):
		self.internal_elements = []

	def get_list(self):
		return self.internal_elements

	def get_element(self, element_number):
		return self.internal_elements[element_number]

	def add_element(self, element):
		self.internal_elements.append(element)

	def __str__(self):
		return str(self.internal_elements)

