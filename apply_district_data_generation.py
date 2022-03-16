import pandas as pd
from pathlib import Path as p
import numpy as np
import district_data_generation as ddg

ddg.per_day(Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\by_HK",
        Savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\concat_day_HK")
print("per_day HK DONE!")
ddg.per_day(Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\by_region",
       Savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\concat_day_region")
print("per_day region DONE!")
ddg.per_day(Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\by_district",
      Savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\concat_day_district")
print("per_day district DONE!")

ddg.time_percentage(
        Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\concat_day_HK",
        Savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_five_minutes")
print("time_percentage HK DONE!")
ddg.time_percentage(
    Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\concat_day_region",
    Savepath=r'E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\all_five_minutes')
print("time_percentage region DONE!")

ddg.time_percentage(
    Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\concat_day_district",
    Savepath=r'E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\all_five_minutes')
print("time_percentage district DONE!")

ddg.allday_percentage_minute(
    Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_five_minutes",
    Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_percentage")
print("allday_percentage_minute HK DONE!")
ddg.allday_percentage_minute(
     Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\all_five_minutes",
     Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\all_percentage")
print("allday_percentage_minute region DONE!")
ddg.allday_percentage_minute(
    Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\all_five_minutes",
    Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\all_percentage")
print("allday_percentage_minute district DONE!")

ddg.sunday_percentage_minute(
   Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_five_minutes",
   Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\sunday_percentage")
print("sunday_percentage_minute HK DONE!")

ddg.sunday_percentage_minute(
    Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\all_five_minutes",
    Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\sunday_percentage")
print("sunday_percentage_minute region DONE!")

ddg.sunday_percentage_minute(
  Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\all_five_minutes",
  Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\sunday_percentage")
print("sunday_percentage_minute district DONE!")


ddg.weekend_percentage_minute(
   Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_five_minutes",
   Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\weekend_percentage")
print("weekend_percentage_minute HK DONE!")

ddg.weekend_percentage_minute(
    Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\all_five_minutes",
    Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\weekend_percentage")
print("weekend_percentage_minute region DONE!")

ddg.weekend_percentage_minute(
  Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\all_five_minutes",
  Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\weekend_percentage")
print("weekend_percentage_minute district DONE!")


ddg.weekday_percentage_minute(
    Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_five_minutes",
    Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\weekday_percentage")
print("weekday_percentage_minute HK DONE!")

ddg.weekday_percentage_minute(
    Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\all_five_minutes",
    Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\weekday_percentage")
print("weekday_percentage_minute region DONE!")

ddg.weekday_percentage_minute(
   Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\all_five_minutes",
   Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\weekday_percentage")
print("weekday_percentage_minute district DONE!")
