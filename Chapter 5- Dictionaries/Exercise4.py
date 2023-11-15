'''Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

* Use a loop to print the name of each river included in the dictionary.

* Use a loop to print the name of each country included in the dictionary.'''

rivers = {
    'nile':'egypt',
    'mississippi':'united states',
    'faser':'canada',
    'kuskokwim':'alaska'
    'yangtze':'china'
}
for river, country in rivers.items():
    print("The"+ river.title()+"flows through"+ country.title()+".")

print("\nthe following rivers are included in this data set:")
for river in rivers.key():
    print("-"+ river.title())

print("\nthe following countries are included in this  data set:")
for country in rivers.values():
    print("-"+ country. title())