from Element import *
from Equation import *
from pylatex import *
from GenericOutput import *

class LatexOutput(GenericOutput):
	def __init__(self):
		super(LatexOutput, self).__init__()

	def doc_header(self):
		doc = "\\documentclass{article}\n"
		doc += "\\usepackage[utf8]{inputenc}\n"
		doc += "\\usepackage[normalem]{ulem}\n"
		doc += "\\usepackage{amsmath}\n"
		doc += "\\usepackage{graphicx}\n"
		doc += "\\usepackage{hyperref}\n"
		doc += "\\begin{document}\n"
		return doc
		
	def doc_footer(self):
		doc = "\\end{document}"
		return doc

	def unordered_list(self, element):
		""" Returns a sting that represents the latex output that corresponds to an unordered list. This will call to_code on each item of the list in order 
			to get the proper latex output. 

		"""
		doc = ['\\begin{itemize}\n']
		elements = element.get_elements()
		for obje in elements:
			#Prints strings or objects with string attribute directly.
			if hasattr(obje, 'str'):
				doc.extend('\\item ' + obje + '\n')
			else:
			#Prints the converted to string item for those that items that are elements w.o. string attribute.
				doc.append('\\item ' + self.to_code(obje) + '\n')

		doc.extend('\\end{itemize}\n')
		return ''.join(doc)

	def ordered_list(self, element):
		"""Returns a sting that represents the latex output that corresponds to an ordered list. This will call to_code on each item of the list in order 
			to get the proper latex output. 
		"""
		doc = ['\\begin{enumerate}\n']
		elements = element.get_elements()
		for obje in elements:
			if hasattr(obje, 'str'):
			#Prints strings or objects with string attribute directly.
				doc.extend('\\item ' + obje + '\n')
			else:
			#Prints the converted to string item for those that items that are elements w.o. string attribute.
				doc.append('\\item ' + self.to_code(obje) + '\n')

		doc.extend('\\end{enumerate}\n')
		return ''.join(doc)

	def text(self, element):
		"""returns a string associated with the text
		"""
		return element.get_elements()

	def link(self, element):
		"""Returns a formated latex link output, the text associated with the URL can be formatted like any other element using to_code
		
		"""
		return "\\href{" + element.element + "}{"  +self.to_code(element.url)+ "}"

	def image(self, element):
		"""Returns a latex figure that contains the desired graphic. 
		"""
		return "\\begin{figure}[h]\n\\caption{" + element.caption + "}\n\\centering\n\\includegraphics{" + element.path + "}\n\\end{figure}"

	def bold(self, element):
		""" Returns a formatted bold statement, the interior of the statement can be variable and also formatted using to_code.
		"""
		return "\\textbf{" + self.to_code(element.get_elements()) + "}"

	def italic(self, element):
		""" Returns a formatted italic statement, the interior of the statement can be variable and also formatted using to_code.
		"""
		return "\\textit{" + self.to_code(element.get_elements()) + "}"

	def underline(self, element):
		"""Returns a formatted underline statement, the interior of the statement can be variable and also formatted using to_code.
		"""
		
		return "\\underline{" + self.to_code(element.get_elements()) + "}"

	def strikethrough(self, element):
		"""Returns a formatted strikethrough statement, the interior of the statement can be variable and also formatted using to_code.
		"""
		return "\\sout{" + self.to_code(element.get_elements()) + "}"

	def bold_italic(self, element):
		"""Returns a formatted bold and italicized statement, the interior of the statement can be variable and also formatted using to_code.
		"""
		return "\\textit{\\textbf{" + self.to_code(element.get_elements()) + "}}"

	def quote(self, element):
		"""Returns a formatted quotation statement, the interior of the statement can be variable and also formatted using to_code.
		"""
		return "``" + self.to_code(element.get_elements()) + "''"

	def heading(self, element): 
		"""Returns a formatted header statement. Each level corresponds to levels of depth for the heading. We do not currently
		implement chapter and part headers.
		"""
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
		""" Contains the structure of a paragraph, which can contain various text elements, link elements, etc.
		"""
		doc = []
		elements = element.get_elements()
		for obje in elements:
			#Adds a str if no other formatting there
			if hasattr(obje, 'str'):
				doc.extend(obje)
			else:
			#Otherwise, it formats the code first by to_code and then appends it to the doc,
				doc.append(self.to_code(obje))
		doc.append("\n")
		return ''.join(doc)

	def table(self, element):
		"""Creates a table in latex format, will format each subelement, and outputs as a tabular table. Assumption is that there will be no indents in this block. 
		Additionally, this will be in its own block of text. 
		"""
		doc = []
		#creates some initial text needed to setup . 
		doc.append("\\noindent\n")
		headers = element.headers
		items = element.items
		texthead = []
		#creates some initial formatting for number of columns in header. 
		initial_header = "{" + "| c " * len(headers) + "|}" + "\n"
		doc.append("\\begin{tabular}" + initial_header)
		doc.append("\\hline \n")
		#builds a header based on the headers element and adds them to the doc.
		for subelement in headers:
			if hasattr(subelement, 'str'):
				texthead.extend(subelement)
			else:
				texthead.append(self.to_code(subelement))
		#actually generates & appends together a first line of the header with custom input. 
		doc.append("&".join(texthead) + "\\\\\n")
		doc.append("\\hline \n")
		#generates lines one by one via appending subelements together.
		for subline in items:
			texthead = []
			for subelement in subline:
				if hasattr(subelement, 'str'):
					texthead.extend(subelement)
				else:
					texthead.append(self.to_code(subelement))	
			doc.append("&".join(texthead) + "\\\\\n")
			doc.append("\\hline \n")
		#ends the table structure. 
		doc.append("\\end{tabular}\n")

		return "".join(doc)

	def block_equation(self, element):
		""" Generates an equation that lies in its own block. Uses equationhelper to do so. 
		"""
		doc = []
		#initial formatting to begin equation block.
		doc.append("\\begin{equation}\n")
		#uses equation helper to generate the text of an equation. 
		eqn = self.equationhelper(element.equation.left) + element.equation.mid + self.equationhelper(element.equation.right)
		doc.append(eqn + "\n")
		#ends the equation block. 
		doc.append("\\end{equation}\n")
		return "".join(doc)

	def inline_equation(self, element):
		""" Generates an equation that lies in-line with the text. Uses equationhelper to do so.
		"""
		doc = []
		#How to start latex inline equation
		doc.append("$")
		#Generates & appends an equation using equationhelper
		eqn = self.equationhelper(element.equation.left) + element.equation.mid + self.equationhelper(element.equation.right)
		doc.append(eqn)
		#how to end latex inline equations.
		doc.append("$")
		return "".join(doc)


	def equationhelper(self, expression):
		"""Recursive function that helps to generate expressions for an equation. 
		"""
		#If the epxression are just characters or numbers, than returns a string.
		if type(expression) == str:
			return expression
		#if the expression is a function, then it returns the formmated latex function + formatted interior .
		elif isinstance(expression, Function):
			return "{\\" + expression.func + "(" + self.equationhelper(expression.param) + ")}"
		else:
			#otherwise, it just checks for different special behaviors (i.e. fractions and such) and formatas the output accordingly
			if expression.operator == "/":
				return "{\\frac{" + self.equationhelper(expression.left) + "}{" + self.equationhelper(expression.right) + "}}"
			elif expression.operator == '*':
				return "{"+ self.equationhelper(expression.left) +" "+ self.equationhelper(expression.right)+ "}"
			else:
				return "{"+ self.equationhelper(expression.left) + expression.operator + self.equationhelper(expression.right)+ "}"


if __name__ == "__main__":
	import doctest
	doctest.testmod()
