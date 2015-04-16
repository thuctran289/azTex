import sys
from Element import Element

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
    element = parser.parse(block)
    elements.append(element)
    block = tokenizer.get_next_block()

print "===== DOCUMENT ELEMENTS ====="
for i in range(len(elements)):
    print "%d. %s" % (i+1, elements[i])
print "==============================\n\n"


print "==============="
print "=== SUCCESS ==="
print "==============="


