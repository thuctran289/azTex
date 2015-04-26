import re

class EquationParser(object):
	EQUALITY_PATTERN = re.compile(r"[=<>]+")
	POS_NEG_VAL_PATTERN = re.compile(r"^[+-]\w+$")

	def parseEquation(self, equation):
		""" parses an equation
		>>> str(p.parseEquation("y = 3"))
		'(y) = (3)'
		>>> str(p.parseEquation("c = (a ^ 2 + b ^ 2) ^ (1 / 2)"))
		'(c) = ((((a) ^ (2)) + ((b) ^ (2))) ^ ((1) / (2)))'
		>>> str(p.parseEquation("y - 3 >= b ^ 2 - 5"))
		'((y) - (3)) >= (((b) ^ (2)) - (5))'
		>>> str(p.parseEquation("y = -5"))
		'(y) = (-5)'
		>>> str(p.parseEquation("y = +5 - x"))
		'(y) = ((+5) - (x))'
		>>> str(p.parseEquation("F = (G * m1 * m2) / r^2"))
		'(F) = (((G) * ((m1) * (m2))) / ((r) ^ (2)))'
		"""
		left, right, mid = self.splitEquation(equation)

		left = self.parseExpression(left)
		right = self.parseExpression(right)

		return Equation(left, right, mid)

	def parseExpression(self, expr):
		""" parses an expression
		>>> p.parseExpression("3")
		'3'
		>>> e = p.parseExpression("2 + 2")
		>>> (e.left, e.right, e.operator)
		('2', '2', '+')
		"""
		# remove outer parens if there are any
		expr = self.removeOuterParentheses(expr)

		# base case
		# expr is a single value
		if self.isValue(expr):
			return expr	

		left, right, oper = self.splitExpression(expr)

		left  = self.parseExpression(left)
		right = self.parseExpression(right)
		return Expression(left, right, oper)

	def removeOuterParentheses(self, expr):
		""" removes the outer parens if there are any
		>>> p.removeOuterParentheses("(3)")
		'3'
		>>> p.removeOuterParentheses("3")
		'3'
		>>> p.removeOuterParentheses("(3 * (x - 5))")
		'3 * (x - 5)'
		>>> p.removeOuterParentheses("(3 * x) - (4 + y)")
		'(3 * x) - (4 + y)'
		"""
		if self.hasExtraParentheses(expr):
			return expr[1:-1]
		return expr

	def hasExtraParentheses(self, expr):
		""" determines if an expression has extra outer parens
		>>> p.hasExtraParentheses("(3)")
		True
		>>> p.hasExtraParentheses("3 * x")
		False
		>>> p.hasExtraParentheses("(1 + 2) - (3 + 4)")
		False
		"""
		parensLevel = 0
		for char in expr:
			if char == '(':
				parensLevel += 1
			elif char == ')':
				parensLevel -= 1
			elif parensLevel == 0:
				return False

		return True


	def splitExpression(self, expr):
		""" split expression into left, right and operator
		>>> p.splitExpression("3 + 3")
		('3', '3', '+')
		>>> p.splitExpression("3 * x - 5")
		('3 * x', '5', '-')
		"""
		operatorIndex = self.leastPrecedenceOperatorIndex(expr)
		left = expr[:operatorIndex]
		right = expr[operatorIndex+1:]
		operator = expr[operatorIndex] 

		left = left.strip()
		right = right.strip()

		return (left, right, operator)


	def leastPrecedenceOperatorIndex(self, expr):
		""" finds the index of the operator with least precedence
		>>> p.leastPrecedenceOperatorIndex("3 + 3")
		2
		>>> p.leastPrecedenceOperatorIndex("3 * x - 5")
		6
		>>> p.leastPrecedenceOperatorIndex("(a ^ 2 + b ^ 2) ^ (1 / 2)")
		16
		>>> p.leastPrecedenceOperatorIndex("G * m1 * m2")
		2
		"""
		for operator in self.operators():
			parensLevel = 0
			for index in range(len(expr)):
				if expr[index] == '(':
					parensLevel += 1
				elif expr[index] == ')':
					parensLevel -= 1
				elif parensLevel == 0 and expr[index] == operator:
					return index

	def splitEquation(self, equation):
		""" splits the equation into its two sides
		>>> p.splitEquation("y = 3 * x")
		('y', '3 * x', '=')
		>>> p.splitEquation("a + b < (3 * c) / 2")
		('a + b', '(3 * c) / 2', '<')
		"""
		match = self.EQUALITY_PATTERN.search(equation)
		midStart = match.start()
		midEnd = match.end()

		left = equation[:midStart]
		right = equation[midEnd+1:]
		middle = equation[midStart:midEnd]

		left = left.strip()
		right = right.strip()

		return (left, right, middle)

	def isValue(self, expr):
		""" is expr a single value
		>>> p.isValue("3")
		True
		>>> p.isValue("3 + 5")
		False
		>>> p.isValue("-4")
		True
		>>> p.isValue("+4")
		True
		"""
		if self.POS_NEG_VAL_PATTERN.match(expr):
			return True
		return not any(operator in expr for operator in self.operators()) 

	def operators(self):
		""" reverse pemdas operators """
		return ['-', '+', '/', '*', '^']
	
class Equation(object):

	def __init__(self, left, right, mid):
		self.left = left
		self.right = right
		self.mid = mid

	def __str__(self):
		return "(" + str(self.left) + ") " + \
			   self.mid + \
			   " (" + str(self.right) + ")"

class Expression(object):

	def __init__(self, left, right, operator):
		self.left = left
		self.right = right
		self.operator = operator

	def __str__(self):
		return "(" + str(self.left) + ") " + \
			   self.operator + \
			   " (" + str(self.right) + ")"

if __name__ == "__main__":
	import doctest
	doctest.testmod(extraglobs={'p': EquationParser()})

	# p = EquationParser()
	# equation = "\\rho = x ^ 2 - 3 / y"
	# print equation
	# print p.parseEquation(equation)
