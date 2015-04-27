from Element import *
from pylatex import *
from GenericOutput import *

class LatexOutput(GenericOutput):
	def __init__(self):
		super(LatexOutput, self).__init__()

	def to_doc(self, representation):
		""" Returns a list of the lines of the LaTeX code
			analogous to representation.

			representation: the internal representation to be
							turned into LaTeX code
			returns: list of lines of LaTeX code
		"""
		doc = []
		doc.append("\\documentclass{article}\n")
		doc.append("\\usepackage[utf8]{inputenc}\n")
		doc.append("\\usepackage[normalem]{ulem}\n")
		doc.append("\\usepackage{amsmath}\n")
		doc.append("\\usepackage{hyperref}\n")
		doc.append("\\begin{document}\n")
		for element in representation:
			doc.append(self.to_code(element))
		doc.append("\\end{document}")

		return doc

	def unordered_list(self, element):
		doc = ['\\begin{itemize}\n']
		elements = element.get_elements()
		for obje in elements:
			if hasattr(obje, 'str'):
				doc.extend('\\item ' + obje + '\n')
			else:
				doc.append('\\item ' + self.to_code(obje) + '\n')

		doc.extend('\\end{itemize}\n')
		return ''.join(doc)
	def ordered_list(self, element):
		doc = ['\\begin{enumerate}\n']
		elements = element.get_elements()
		for obje in elements:
			if hasattr(obje, 'str'):
				doc.extend('\\item ' + obje + '\n')
			else:
				doc.append('\\item ' + self.to_code(obje) + '\n')

		doc.extend('\\end{enumerate}\n')
		return ''.join(doc)
	def text(self, element):
		return element.get_elements()
	def link(self, element):
		# print type(element.element)
		return "\\href{" + element.element + "}{"  +self.to_code(element.url)+ "}"

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
			return "\\section{" + self.to_code(element.get_elements()) + "}\n"
		elif element.level == 2:
			return "\\subsection{" + self.to_code(element.get_elements()) + "}\n"
		elif element.level == 3:
			return "\\subsubsection{" + self.to_code(element.get_elements()) + "}\n"
		elif element.level == 4:
			return "\\paragraph{" + self.to_code(element.get_elements()) + "}\n"
		elif element.level == 5:
			return "\\subparagraph{" + self.to_code(element.get_elements()) + "}\n"
			
	def paragraph(self, element):
		doc = []
		elements = element.get_elements()
		for obje in elements:
			if hasattr(obje, 'str'):
				doc.extend(obje)
			else:
				doc.append(self.to_code(obje))
		doc.append("\n")
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
		
		doc.append("\\end{tabular}\n\n")

		return "".join(doc)
	

	def equation(self, element):
		doc = []
		doc.append("\\begin{equation}\n")
		eqn = self.equationhelper(element.left) + element.mid + self.equationhelper(element.right)
		doc.append(eqn + "\n")
		doc.append("\\end{equation}\n")
		return "".join(doc)

	def equationhelper(self, expression):
		if type(expression) == str:
			return expression
		else:
			if expression.operator == "/":
				return "\\frac{" + self.equationhelper(expression.left) + "}{" + self.equationhelper(expression.right) + "}"
			else:
				return self.equationhelper(expression.left) + expression.operator + self.equationhelper(expression.right)

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
