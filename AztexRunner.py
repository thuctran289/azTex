text = "\
aztex is cool\n\
=============\n\
\n\
1. build tokenizer\n\
2. build parser\n\
3. build internal representation\n\
4. ???\n\
5. profit\n\
\n\
### Latex ###\n\
\n\
- difficult to learn\n\
- verbose\n\
- no fun\n\
\n\
#### It's so hard ####\n\
"

print text

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

print elements

