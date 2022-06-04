import pandas as pd
from pathlib import Path as p
import numpy as np
import apply_concat_per_time as acpt
import meter_dictionary as medi
import concat_calculate_time_percentage as cctp
import calculate_average_percentage as cap
from identify_weekday_list import weekend_weekday as ww


# the first step can create new district folder for saving day_csv
# day_csv is created after using 'acpt.apply_time_day'
# Basepath consists of sub_type folders such as some district data
# Savepath will be the parent path of folders
def per_day(Basepath, Savepath):
    bapa = p(Basepath)
    sapa = p(Savepath)
    for folder in bapa.iterdir():
        cr_fn = folder.name
        save_folpa = sapa / cr_fn
        save_folpa.mkdir(exist_ok=True)
        acpt.apply_time_day(Base_parent=folder,
                            Save_parent=save_folpa)
    print('DDoonne!')



## per_day(Basepath=r"D:\POLYU_dissertation\July_2021_useful\area\by_region",
##         Savepath=r"D:\POLYU_dissertation\July_2021_useful\area\concat_day_region")
# per_day(Basepath=r"D:\POLYU_dissertation\July_2021_useful\area\by_HK",
#         Savepath=r"D:\POLYU_dissertation\July_2021_useful\area\concat_day_HK")


# this script can calculate merters occupied% every 5 minutes
# in one parent path (etc. by_region) which includes many folders(etc. New Terrorities, Hong Kong)

def time_percentage(Basepath, Savepath):
    bapa = p(Basepath)
    sapa = p(Savepath)
    for folder in bapa.iterdir():
        cr_fn = folder.name + '.csv'
        save_pa = sapa / cr_fn
        cctp.concat_per_csv_percentage(Basefolder=folder,
                                       Savepath=save_pa)
    print('DDoonne!')


## time_percentage(
##   Basepath=r"D:\POLYU_dissertation\July_2021_useful\area\concat_day_HK",
##    Savepath=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\all_five_minutes")
## time_percentage(
##    Basepath=r"D:\POLYU_dissertation\July_2021_useful\area\concat_day_region",
##     Savepath=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_region\all_five_minutes")



## this script can calculate one hour percentage in one folder which consists of many area_csv
## this area_csv has two level index, one is date, and the other is 'content' which consists of
## 'Occupied Percentage', 'all', 'occupied'
def hour_percentage(Basefolder, Savefolder):
    bapa = p(Basefolder)
    sapa = p(Savefolder)
    for piece_csv in bapa.iterdir():
        cap.average_period_percentage(Basepath=piece_csv,
                                      Savepath=Savefolder)
    print('Done!')


## hour_percentage(
##     Basefolder=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\per_district\all_five_minutes",
##     Savefolder=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\per_district\all_one_hour")


## this document can calcualat weekend average percentage, this is a tempoary document
## it may be adjusted next time

def weekend_percentage_minute(Basefolder, Savefolder):
    bapa = p(Basefolder)
    sapa = p(Savefolder)
    for piece_csv in bapa.iterdir():
        df_base = pd.read_csv(piece_csv, index_col=[0, 1], header=0)
        date_list = df_base.index.get_level_values(0).tolist()
        date_list = tuple(set(date_list))
        weekend_list = ww(list_date=date_list, type="weekend")
        print("weekend_list:")
        print(weekend_list)
        cap.average_several_percentage_minute(Basepath=piece_csv,
                                       Savepath=sapa,
                                       days_type='weekend',
                                       days_name=weekend_list)

## this document can calcualat weekend average percentage, this is a tempoary document
## it may should be adjusted next time
## here, weekends list are changeable
def sunday_percentage_minute(Basefolder, Savefolder):
    bapa = p(Basefolder)
    sapa = p(Savefolder)
    for piece_csv in bapa.iterdir():
        df_base = pd.read_csv(piece_csv, index_col=[0, 1], header=0)
        date_list = df_base.index.get_level_values(0).tolist()
        date_list = tuple(set(date_list))
        sunday_list = ww(list_date=date_list, type="Sunday")
        print("sunday_list:")
        print(sunday_list)
        cap.average_several_percentage_minute(Basepath=piece_csv,
                                       Savepath=sapa,
                                       days_type='sunday',
                                       days_name=sunday_list)

# def weekend_percentage_hour(Basefolder, Savefolder):
#     bapa = p(Basefolder)
#     sapa = p(Savefolder)
#     for piece_csv in bapa.iterdir():
#         df_base = pd.read_csv(piece_csv, index_col=[0, 1], header=[0, 1])
#         date_list = df_base.index.get_level_values(0).tolist()
#         date_list = tuple(set(date_list))
#         weekend_list = ww(list_date=date_list, type="weekend")
#         cap.average_several_percentage_hour(Basepath=piece_csv,
#                                       Savepath=sapa,
#                                        days_type='weekend',
#                                        days_name=weekend_list)


## this document can calcualat weekday average percentage, this is a tempoary document
## the list may be adjusted next time
def weekday_percentage_minute(Basefolder, Savefolder):
    bapa = p(Basefolder)
    sapa = p(Savefolder)
    for piece_csv in bapa.iterdir():
        df_base = pd.read_csv(piece_csv, index_col=[0, 1], header=0)
        date_list = df_base.index.get_level_values(0).tolist()
        holiday_list = [20210701, 20210922] # HK holiday July-Sept
        for per_hol in holiday_list:
            while per_hol in date_list:
                date_list.remove(per_hol)
        date_list = tuple(set(date_list))
        weekday_list = ww(list_date=date_list, type="weekday")
        print("weekday_list:")
        print(weekday_list)
        cap.average_several_percentage_minute(Basepath=piece_csv,
                                       Savepath=sapa,
                                       days_type='weekday',
                                       days_name=weekday_list)

def weekday_percentage_hour(Basefolder, Savefolder):
    bapa = p(Basefolder)
    sapa = p(Savefolder)
    for piece_csv in bapa.iterdir():
        df_base = pd.read_csv(piece_csv, index_col=[0, 1], header=[0, 1])
        date_list = df_base.index.get_level_values(0).tolist()
        date_list = tuple(set(date_list))
        weekday_list = ww(list_date=date_list, type="weekday")
        cap.average_several_percentage_hour(Basepath=piece_csv,
                                       Savepath=sapa,
                                       days_type='weekday',
                                       days_name=weekday_list)

def allday_percentage_minute(Basefolder, Savefolder):
    bapa = p(Basefolder)
    sapa = p(Savefolder)
    for piece_csv in bapa.iterdir():
        df_base = pd.read_csv(piece_csv, index_col=[0, 1], header=0)
        date_list = df_base.index.get_level_values(0).tolist()
        date_list = tuple(set(date_list))
        print("allday_list:")
        print(date_list)
        cap.average_several_percentage_minute(Basepath=piece_csv,
                                       Savepath=sapa,
                                       days_type='days',
                                       days_name=date_list)
## sample

## weekend_percentage_hour(
##      Basefolder=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\per_region\all_one_hour",
##      Savefolder=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\per_region\other_types")

# allday_percentage_minute(
#     Basefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\all_five_minutes",
#     Savefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\other_types")
# allday_percentage_minute(
#      Basefolder=r"E:\2022dissertation\July_clustering\per_district\all_five_minutes",
#      Savefolder=r"E:\2022dissertation\July_clustering\per_district\all_percentage")
# allday_percentage_minute(
#     Basefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_region\all_five_minutes",
#     Savefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_region\all_percentage")

### weekend_percentage_minute(
###     Basefolder=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\per_region\all_five_minutes",
###     Savefolder=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\per_region\other_types")

### weekday_percentage_hour(
###     Basefolder=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\per_district\all_one_hour",
###     Savefolder=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\per_district\other_types")

### weekday_percentage_minute(
###     Basefolder=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\per_region\all_five_minutes",
###     Savefolder=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\per_region\other_types")


# weekend_percentage_minute(
#    Basefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\all_five_minutes",
#    Savefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\other_types")
# weekend_percentage_minute(
#     Basefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_region\all_five_minutes",
#     Savefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_region\other_types")
# weekday_percentage_minute(
#     Basefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\all_five_minutes",
#     Savefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\other_types")
# weekday_percentage_minute(
#     Basefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_region\all_five_minutes",
#     Savefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_region\other_types")


# per_day(Basepath=r"D:\POLYU_dissertation\July_2021_useful\area\by_district",
#         Savepath=r"D:\POLYU_dissertation\July_2021_useful\area\concat_day_district")
#  time_percentage(
#  Basepath=r"D:\POLYU_dissertation\July_2021_useful\area\concat_day_district",
#  Savepath=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\all_five_minutes")

# weekend_percentage_minute(
#   Basefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\all_five_minutes",
#   Savefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\other_types")
# weekday_percentage_minute(
#    Basefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\all_five_minutes",
#    Savefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\other_types")
