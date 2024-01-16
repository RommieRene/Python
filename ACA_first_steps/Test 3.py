
import datetime

import random

year_date_1 = int(input("Enter with commas: "))
year_date_2 = int(input('Enter with commas: '))

user_count = int(input('Enter number from 100-10000:'))
#



new_list = []
for i in range(user_count):
    new_list.append(datetime.date(random.randint(year_date_1, year_date_2), random.randint(1, 12), random.randint(1, 31)))

print(new_list)
from collections import *
import json

            # if


class read_file:

        def __init__(self, my_list:list):
            self.my_list = my_list


        def for_week(self,S:list ):
            for i in S:
                if i == self.WEEK:








new_list = []
with open('expenses.json') as json_file:
        data = json.load(json_file)
        print(data)
        for i in data:

             print(i)










