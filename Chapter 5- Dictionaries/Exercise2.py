'''A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 

their meanings as values.

* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 

the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 

each word-meaning pair in your output.'''

glossary ={
'variable':'a variable in a python program gives data to the computer for processing.',
'float':'Float is a function or reusable code in the Python programming language that converts values into floating point numbers.',
'comment':'Comments in Python are the lines in the code that are ignored by the interpreter during the execution of the program.',
'print':'The print() function prints the specified message to the screen, or other standard output device.',
'dictionary':'A dictionary in Python is a collection of key-value pairs.'}

word = 'variable'
print ("\n" + word.title() + ":" +glossary[word])

word = 'float'
print ("\n" + word.title() + ":" +glossary[word])

word = 'comment'
print ("\n" + word.title() + ":" +glossary[word])

word = 'print'
print ("\n" + word.title() + ":" +glossary[word])

word = 'dictionary'
print ("\n" + word.title() + ":" +glossary[word])
