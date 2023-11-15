
'''Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 

each pet'''

#Make an empty list to store the pets in.
pets = []
# Make individual pets, and store each one in the list.
pet = {
'animal type':'python',
'name':'john',
'owner':'guido',
'weight':'25',
'eats':'oats',
}

pets.append(pet)

pet = {
    'animal type':'chicken',
    'name':'bozo',
    'owner':'broski',
    'weight':'54',
    'eats':'pasta',
    
}
pets.append(pet)

pet = {
    'animal type':'bunny',
    'name':'cutie',
    'owner':'Ammara',
    'weight':'15',
    'eats':'carrots',
    
}
pets.append(pet)
# display information about each pet

for pet in pets:
    print("\nHere's what I know about" + pet['name'].title()+":")
    for key, value in pet.items():
        print("\t" + key + ":"+str(value))
