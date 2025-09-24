students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
#This is a list of dictionaries
#Each student has their own dictionaries

for student in students: #loop the list and call the data of each value, sep by coma
    print(student["name"], student["house"], student["patronus"], sep=", ")