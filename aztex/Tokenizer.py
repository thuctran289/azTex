import re

class Tokenizer(object):
    BLOCK_REGEX = "([^\n]+(?:\n[^\n]+)*(?=\n|$))"
    BLOCK_PATTERN = re.compile(BLOCK_REGEX)
    
    def __init__(self, text):
        self.text = text
        self.text_index = 0

    def get_next_block(self):
        match = self.BLOCK_PATTERN.search(self.text, self.text_index)     

        if match == None:
            return None

        self.text_index = match.end()
        block = match.group()
        return block

if __name__ == "__main__":
    t = Tokenizer("block1\nblock1\nblock1\n\nblock2\nblock2")

    b = t.get_next_block()
    print "==== 1 ===="
    print b
    print "==========="

    b = t.get_next_block()
    print "==== 2 ===="
    print b
    print "==========="
