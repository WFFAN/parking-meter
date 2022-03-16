from typing import Iterator
import pandas as pd
from pathlib import Path as p
import numpy as np
import re
from datetime import datetime


# This script can return a weekend list or weekday list (exclude Monday)(it will be tuple type)
# if you give it a list
# values in list should be numerical


def weekend_weekday(list_date, type):
    list_weekend = []
    list_weekday = []
    list_Saturday = []
    list_Sunday = []
    for per_day in list_date:
        str_per_day = str(per_day)
        which_day = datetime.strptime(str_per_day, '%Y%m%d').weekday()
        which_day += 1
        if which_day <= 5 and which_day >= 2:
            list_weekday.append(per_day)

        if which_day == 6 or which_day == 7:
            list_weekend.append(per_day)
        if which_day == 6:
            list_Saturday.append(per_day)
        if which_day == 7:
            list_Sunday.append(per_day)

    list_weekday = tuple(list_weekday)
    list_weekend = tuple(list_weekend)
    list_Saturday = tuple(list_Saturday)
    list_Sunday = tuple(list_Sunday)

    if type == "weekday":
        return list_weekday
    if type == "weekend":
        return list_weekend
    if type == "Saturday":
        return list_Saturday
    if type == "Sunday":
        return list_Sunday


# = weekend_weekday(
#   list_date=[
#        20220124, 20220125, 20220126,
#        20220127, 20220128, 20220129,
#        20220130, 20220131, 20220201,
#        20220202, 20220203, 20220204], type="Saturday")
# print(a)



# b = weekend_weekday(
#     list_date=[
#         20220124, 20220125, 20220126,
#         20220127, 20220128, 20220129,
#         20220130, 20220131, 20220201,
#         20220202, 20220203, 20220204],
#     type="weekday")
# print(b)
