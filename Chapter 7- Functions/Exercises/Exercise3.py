'''Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 

should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 

arguments to make a shirt. Call the function a second time using keyword arguments.
'''
def make_shirt(size,text):
    print("\nYou've orderd a" + size + "shirt that says" + text)


make_shirt('large','"suck it Trebek"') 
make_shirt(size='smedium' , text = '"I need a bigger shirt"')
