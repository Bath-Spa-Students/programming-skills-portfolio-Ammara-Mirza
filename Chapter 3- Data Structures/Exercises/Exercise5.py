# invite people to dinner
guests=['jack','olivia','bob','oggy']

name = guests[0].title()
print(name+",please come to dinner.")

name = guests[1].title()
print(name+",please come to dinner.")

name = guests[2].title()
print(name+",please come to dinner.")

name = guests[3].title()
print(name+",please come to dinner.")

name = guests[2].title()
print("\nsorry," + name +"can't make it to dinner.")

# jack's can't make it to dinner let's invite cockroaches instead.
del (guests[2])
guests.insert(2,'cockroaches')

name= guests[0].title()
print("\n" + name + ",please come to dinner.")

name= guests[1].title()
print("\n" + name + ",please come to dinner.")

name= guests[2].title()
print("\n" + name + ",please come to dinner.")

name= guests[3].title()
print("\n" + name + ",please come to dinner.")
