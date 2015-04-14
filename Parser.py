import re
from Element import *

class Parser(object):
    HEADING_REGEX = r"^[^\n]+\n={2,}"
    HEADING_PATTERN = re.compile(HEADING_REGEX)

    SUB_HEADING_REGEX = r"^[^\n]+\n-{2,}"
    SUB_HEADING_PATTERN = re.compile(SUB_HEADING_REGEX)

    SUB_SUB_HEADING_REGEX = r"^(?:(\#+) .+ \1)"
    SUB_SUB_HEADING_PATTERN = re.compile(SUB_SUB_HEADING_REGEX)

    ORDERED_LIST_REGEX = r"^(?:\d\..+(?:\n|$))+"
    ORDERED_LIST_PATTERN = re.compile(ORDERED_LIST_REGEX)

    UNORDERED_LIST_REGEX = r"^(?:(?:\*|\-) .+(?:\n|$))+"
    UNORDERED_LIST_PATTERN = re.compile(UNORDERED_LIST_REGEX)

    def parse(self, block):
        if self.isHeading(block):
            return HeaderElement(self.headingText(block), 1)
        elif self.isSubHeading(block):
            return HeaderElement(self.subHeadingText(block), 2) 
        elif self.isSubSubHeading(block):
            return HeaderElement(self.subSubHeadingText(block, subSubHeadingLevel(block))) 
        elif self.isOrderedList(block):
            return OrderedListElement(listElements(block))
        elif self.isUnorderedList(block):
            return UnorderedListElement(listElements(block))
        elif self.isParagraph(block):
            return ParagraphElement(block)

    def isHeading(self, block):
        """ determines if a block is a header
        ie: 
                aztex
                =====

        >>> p = Parser()
        >>> p.isHeading("aztex\\n=====") 
        True

        >>> p.isHeading('Harry Potter\\n====')
        True

        >>> p.isHeading('Voldemort\\n=')
        False
        """
        return self.HEADING_PATTERN.match(block) != None

    def headingText(self, block):
        """ gets the text out of a heading block
        >>> p = Parser()
        >>> p.headingText("aztex\\n====")
        'aztex'

        >>> p.headingText("Harry Potter\\n=====")
        'Harry Potter'
        """
        return str.split(block, "\n")[0]

    def isSubHeading(self, block):
        """ determines if a block is a subheader
        ie: 
                aztex
                -----

        >>> p = Parser()
        >>> p.isSubHeading("aztex\\n=====") 
        False

        >>> p.isSubHeading("aztex\\n-----") 
        True

        >>> p.isSubHeading("Harry Potter\\n-----")
        True

        >>> p.isSubHeading('Voldemort\\n-')
        False
        """
        return self.SUB_HEADING_PATTERN.match(block) != None

    def subHeadingText(self, block):
        """ gets the text out of a subheading block
        >>> p = Parser()
        >>> p.subHeadingText("aztex\\n-----")
        'aztex'

        >>> p.subHeadingText("Harry Potter\\n-----")
        'Harry Potter'
        """
        return str.split(block, "\n")[0]

    def isSubSubHeading(self, block):
        """ determines if a block is a subsubheader
        ie: 
                #### aztex ####

        >>> p = Parser()
        >>> p.isSubSubHeading("## aztex ##") 
        True

        >>> p.isSubSubHeading("#### aztex ####") 
        True

        >>> p.isSubSubHeading("# Harry Potter #")
        True

        >>> p.isSubSubHeading('### Voldemort #')
        False

        >>> p.isSubSubHeading('## Ron')
        False
        """
        return self.SUB_SUB_HEADING_PATTERN.match(block) != None

    def subSubHeadingText(self, block):
        """ gets the text out of a subsubheading block
        >>> p = Parser()
        >>> p.subSubHeadingText("## aztex ##")
        'aztex'

        >>> p.subSubHeadingText("### Harry Potter ###")
        'Harry Potter'
        """
        pat = re.compile(r"^(\#+) (.+) \1")
        match = pat.search(block)
        return match.groups()[1]

    def subSubHeadingLevel(self, block):
        """ gets the heading level
        >>> p = Parser()
        >>> p.subSubHeadingLevel("## aztex ##")
        2

        >>> p.subSubHeadingLevel("##### aztex #####")
        5
        """
        match = re.match(r"^#+", block)
        return len(match.group())

    def isOrderedList(self, block):
        """ determines if the block is an ordered list
        >>> p = Parser()
        >>> p.isOrderedList("1. eggs\\n2. bread\\n3. rice")
        True
        """
        return self.ORDERED_LIST_PATTERN.match(block) != None

    def orderedListItems(self, block):
        """ gets the list of items
        >>> p = Parser()
        >>> p.orderedListItems("1. cats\\n2. dogs\\n3. mice")
        ['cats', 'dogs', 'mice']
        """
        itemRegex = r"(?<=\d\. )(.+)(?=(?:\n|$))"
        return re.findall(itemRegex, block)

    def isUnorderedList(self, block):
        """ determines if the block is an ordered list
        >>> p = Parser()
        >>> p.isUnorderedList("* eggs\\n* bread\\n* rice")
        True
        >>> p.isUnorderedList("- eggs\\n- bread\\n- rice")
        True
        """
        return self.UNORDERED_LIST_PATTERN.match(block) != None

    def unorderedListItems(self, block):
        """ gets the list of items
        >>> p = Parser()
        >>> p.unorderedListItems("* cats\\n* dogs\\n* mice")
        ['cats', 'dogs', 'mice']
        >>> p.unorderedListItems("- apple\\n- orange\\n- banana")
        ['apple', 'orange', 'banana']
        """
        itemRegex = r"(?<=(?:\*|\-) )(.+)(?=(?:\n|$))"
        return re.findall(itemRegex, block)

class HeaderElement(object):

    def __init__(self, subelements, level):
        self.subelements = subelements
        self.level = level


if __name__ == "__main__":
    import doctest
    doctest.testmod()
