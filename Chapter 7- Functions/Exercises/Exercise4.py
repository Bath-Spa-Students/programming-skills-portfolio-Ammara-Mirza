'''Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

medium shirt with the default message, and a shirt of any size with a different message.
'''



def make_shirt(sixe = 'medium', text = '"I hate python"'):
     print("\nYou've orderd a" + sixe + "shirt that says" + text)


make_shirt('large')
make_shirt()
make_shirt('small','"I am a big brother"')
