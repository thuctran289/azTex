# aztex
## About
aztex is a program written in Python that provides a quick, simple way to create a professional-looking .pdf document.
aztex is a compiler that compiles aztex language (very similar to Markdown) into LaTeX code. aztex can be used by people
who do not know how to write fluently in LaTeX, would like a tool that can act as an introduction to the LaTeX syntax,
or do not want to waste time worrying about some of the small intricacies of LaTeX.

## Installation
Simply type "sudo pip install aztex" into your terminal (for Linux and OSX users). Or, clone this repository on GitHub.

## Use

To compile a text file written in markdown run:
$ aztex input.txt or $ python aztex/main.py input.txt

To compile some text run:
$ aztex "some text" or $ python aztex/main.py "some text"

To use our GUI run:
$ python aztex/AztexRunnerGUI.py

## The Story Behind aztex
aztex was born as a an idea for the final project for the Software Design course at Franklin W. Olin College of Engineering by us: three 
first years (idgetto, jovanduy, thuctran289) in the spring semester of 2015. None of us knew how to use LaTeX efficiently, nor did we
know anything about how compilers work, so we thought that aztex would be an interesting idea to explore and a great opportunity for us
to expand our knowledge. 

## FAQ
#### Why is aztex always written in lower case?
The creators of aztex decided on this as a stylistic choice.
#### In what language is aztex written?
aztex is written almost completely in pure Python. The only external library is wxPython, which is used in the framework of
the GUI.
#### Who is the target audience for aztex?
Anyone who wants to make a .pdf quickly! We (the creators of aztex) have envisioned that it will be used by
people who want a way to quickly take notes that are organized in a nice-looking document, high school students that 
need to make professional-looking reports, and ourselves (we aren't even fluent in LaTeX)!
#### How does aztex (the program, not the language) work?
aztex is a compiler! aztex is made up of a front end and a back end.
Basically, aztex works by first splitting up the aztex code into different *tokens*, or types of
characters in the document, in the front end. aztex then reads through all of these tokens and figure out what type of *element* each
token is; for instance, is a certain token simply a word? an equation? a link? a bolded word? Each of these elements
has its own analogous LaTeX code, so, from the different elements, in the back end aztex is able to output LaTeX code! The code is
all open source and avaiable on GitHub, so for a more in-depth understanding, please read through the code or look up how compilers work.
