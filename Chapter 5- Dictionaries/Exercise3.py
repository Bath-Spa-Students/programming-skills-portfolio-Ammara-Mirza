'''Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.'''

glossary = {
    'variable':'a variable in a python program gives data to the computer for processing.',
    'Float':'Float is a function or reusable code in the Python programming language that converts values into floating point numbers.',
    'Comment':'Comments in Python are the lines in the code that are ignored by the interpreter during the execution of the program.',
    'print':'The print() function prints the specified message to the screen, or other standard output device.',
    'dictionary':'A dictionary in Python is a collection of key-value pairs.',
    'loop':'Looping means repeating something over and over until a particular condition is satisfied.',
    'boolean expression':'an expression that evaluates weather the statement is true of false',
    'key':'the first item in a key value pair in dictionary',
    'conditional test':'A comparison between two values',
    'string':'A series of characters'}

for word, defination in glossary.items():
 print("\n" + word.title()+ ":" + defination)
