import sys
from Element import Element
from LatexOutput import *

if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	filename = "input.txt"
f = open(filename, 'r')
text = f.read()

print "===== ORIGINAL FILE =====\n"
print text
print "=========================\n\n"

from Tokenizer import Tokenizer
from Parser import Parser

tokenizer = Tokenizer(text)
parser = Parser()

elements = []
block = tokenizer.get_next_block()
while block:
    element = parser.parseBlock(block)
    elements.append(element)
    block = tokenizer.get_next_block()

print "===== DOCUMENT ELEMENTS ====="
A = LatexOutput()

#for element in elements:
#	print A.to_code(element)
#	print ""
for element in  A.to_doc( elements):
	print element

print "==============================\n\n"


print "==============="
print "=== SUCCESS ==="
print "==============="




