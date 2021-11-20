ls_people = [
    {"name": "Ron", "house": "Castle"},
    {"name": "Siara", "house": "Island"},
    {"name": "Chak", "house": "Tower"}
]

ls_people.sort(key=lambda ls_people : ls_people["name"])
print(ls_people)