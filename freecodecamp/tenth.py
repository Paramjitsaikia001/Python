#dict-dictionary data type

students =[
   {
    "name":"one Saikia",
    "age":"20",
    "home":"jorhat"
    },
    {
 "name":"two Saikia",
    "age":"23",
    "home":"darang"
    },
    {
     "name":"three Saikia",
    "age":"30",
    "home":"Chirang"
    }
]

for student in students:
    print(f"{student["name"]} is living in {student["home"]}" )