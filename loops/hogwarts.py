students = [
    {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slitherin", "patronus": "some value"},
]

for student in students:
    if student["house"] == "Slitherin":
        print(student["name"], student["house"], student["patronus"], sep=", ")




"""

|#      |   name     |     house      |     patronus      |
-----------------------------------------------------------
|0       |  Hermione  |  Griffindor    |     Otter        |
|1       |  Harry     |  Griffindor    |     Stag         |

"""