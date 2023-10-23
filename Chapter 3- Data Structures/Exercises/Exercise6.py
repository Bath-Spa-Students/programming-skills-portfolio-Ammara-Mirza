## Exercise 6: oh no the table won't arrive on time !!

guests=['jack','olivia','bob','oggy']

name = guests[0].title()
print(name+",please come to dinner.")

name = guests[1].title()
print(name+",please come to dinner.")

name = guests[2].title()
print(name+",please come to dinner.")

name = guests[3].title()
print(name+",please come to dinner.")


print("\nsorry, we can only invite two people to dinner.") 

name=guests.pop()
print("sorry," + name.title() +"there's no table in the room.")

name=guests.pop()
print("sorry," + name.title() +"there's no table in the room.")

name=guests.pop()
print("sorry," + name.title() +"there's no table in the room.")

name=guests.pop()
print("sorry," + name.title() +"there's no table in the room.")

#there should be two people left. let's invite them.
name = guests[3].title()
print(name + ",please come to dinner.")

name = guests[1].title()
print(name + ",please come to dinner.")

del(guests[0])
del(guests[2])

print(guests)