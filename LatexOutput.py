from Element import *
from pylatex import *
from GenericOutput import *

class LatexOutput(GenericOutput):
	def __init__(self):
		super(LatexOutput, self).__init__()

	def to_doc(self, representation):
		doc = []
		doc.append("\\documentclass{article}")
		doc.append("\\usepackage[utf8]{inputenc}")
		doc.append("\\usepackage[normalem]{ulem}")
		doc.append("\\usepackage{hyperref}")
		doc.append("\\begin{document}")
		for element in representation:
			doc.append(self.to_code(element))
		doc.append("\\end{document}")

		return doc
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





	def unordered_list(self, element):
		doc = ['\\begin{itemize}\n']
		elements = element.get_elements()
		for obje in elements:
			if hasattr(obje, 'str'):
				doc.extend('\\item ' + obje + '\n')
			else:
				doc.append('\\item ' + self.to_code(obje) + '\n')

		doc.extend('\\end{itemize}')
		return ''.join(doc)
	def ordered_list(self, element):
		doc = ['\\begin{enumerate}\n']
		elements = element.get_elements()
		for obje in elements:
			if hasattr(obje, 'str'):
				doc.extend('\\item ' + obje + '\n')
			else:
				doc.append('\\item ' + self.to_code(obje) + '\n')

		doc.extend('\\end{enumerate}')
		return ''.join(doc)
	def text(self, element):
		return element.get_elements()
	def link(self, element):
		print type(element.element)
		return "\\href{" + self.to_code(element.url) + "}{"  +element.element+ "}"
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
		if element.level == 1:
			return "\\section{" + self.to_code(element.get_elements()) + "}"
		elif element.level == 2:
			return "\\subsection{" + self.to_code(element.get_elements()) + "}"
		elif element.level == 3:
			return "\\subsubsection{" + self.to_code(element.get_elements()) + "}"
		elif element.level == 4:
			return "\\paragraph{" + self.to_code(element.get_elements()) + "}"
		elif element.level == 5:
			return "\\subparagraph{" + self.to_code(element.get_elements()) + "}"
			
	def paragraph(self, element):
		doc = []
		elements = element.get_elements()
		for obje in elements:
			if hasattr(obje, 'str'):
				doc.extend(obje)
			else:
				doc.append(self.to_code(obje))
		return ''.join(doc)
	def table(self, element):
		doc = []
		doc.append("\\noindent\n")
		headers = element.headers
		items = element.items
		texthead = []

		initial_header = "{" + "| c " * len(headers) + "|}" + "\n"
		doc.append("\\begin{tabular}" + initial_header)
		doc.append("\\hline \n")
		for subelement in headers:
			if hasattr(subelement, 'str'):
				texthead.extend(subelement)
			else:
				texthead.append(self.to_code(subelement))
		doc.append("&".join(texthead) + "\\\\\n")
		doc.append("\\hline \n")
		for subline in items:
			texthead = []
			for subelement in subline:
				if hasattr(subelement, 'str'):
					texthead.extend(subelement)
				else:
					texthead.append(self.to_code(subelement))	
			doc.append("&".join(texthead) + "\\\\\n")
			doc.append("\\hline \n")
		
		doc.append("\\end{tabular}\n")
		return "".join(doc)


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
