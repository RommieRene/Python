sample_dicte = {
        'emp1': {'name': 'John', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}}
s = sample_dicte['emp3']['salary'] = 8500
print(sample_dicte)


sample_dict = {
    "class": {
         "student": {
             "name": "Mike",
             "marks": {
                 "physics": 70,
                 "history": 80
             }
         }
     }
}
print(sample_dict['class']['student']['marks']['history'])



tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1 = tuple2 = tuple1

print(tuple2,'<---tuple1 tuple2 ---->',tuple1)





