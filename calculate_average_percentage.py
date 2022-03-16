import pandas as pd
from pathlib import Path as p
import numpy as np
from pandas import DataFrame
import re
from identify_weekday_list import weekend_weekday as ww

# this script has theses functions below
# average_several_percentage_minute(Basepath, Savepath, days_type, days_name)
# average_several_percentage_hour(Basepath, Savepath, days_type, days_name)
# average_period_percentage(Basepath, Savepath)

# this script can calculate different days' average percentage
# base one five-minute csv document
def average_several_percentage_minute(Basepath, Savepath, days_type, days_name):
    bapa = p(Basepath)
    save_parent = p(Savepath)
    sapa_name = bapa.stem + '_' + days_type + '.csv'
    sapa = save_parent / sapa_name
    base_df = pd.read_csv(bapa, header=0, index_col=[0, 1], keep_default_na=True)
    base_df[:] = base_df[:].astype(np.float64)
    group_min = base_df.groupby(axis=1, level=0)
    df_averperc_list = {}
    for name, group in group_min:
        sum_all = np.float64(0)
        occupied_all = np.float64(0)

        for per_day in days_name:
            # to accumulative days' values
            if pd.notna(group.loc[(per_day, 'all')][name].copy()) and \
                    pd.notna(group.loc[(per_day, 'occupied')][name].copy()):
                sum_all += np.float64(group.loc[(per_day, 'all')][name].copy())
                occupied_all +=np.float64(group.loc[(per_day, 'occupied')][name].copy())
        aver_perc = np.float64(occupied_all / sum_all)
        df_averperc_list[np.int64(name)] = pd.Series([aver_perc], index=[days_type])
    df_averperc = pd.DataFrame(df_averperc_list)
    df_averperc.sort_index(axis=1, inplace=True)
    df_averperc.to_csv(sapa)


# average_several_percentage_minute(
#     Basepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\all_five_minutes\HK.csv",
#     Savepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\other_types",
#     days_type="weekday",
#     days_name=(20210413, 20210414, 20210415, 20210420, 20210421, 20210422))
# average_several_percentage_minute(
#     Basepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\all_five_minutes\HK.csv",
#     Savepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\other_types",
#     days_type="weekend",
#     days_name=(20210417, 20210418, 20210424, 20210425))


# this script can calculate different days' average percentage
# base one one-hour csv document
def average_several_percentage_hour(Basepath, Savepath, days_type, days_name):
    bapa = p(Basepath)
    save_parent = p(Savepath)
    sapa_name = bapa.stem + '_' + days_type + '.csv'
    sapa = save_parent / sapa_name
    base_df = pd.read_csv(bapa, header=[0, 1], index_col=[0, 1])
    base_df[:] = base_df[:].astype(np.float64)
    group_min = base_df.groupby(axis=1, level=0)
    df_averperc_list = {}
    for name, group in group_min:
        sum_all = np.float64(0)
        occupied_all = np.float64(0)
        for per_day in days_name:
            # to accumulative days' values
            if pd.notna(group.loc[(per_day, 'all')][name].copy()) and \
                    pd.notna(group.loc[(per_day, 'occupied')][name].copy()):
                sum_all += np.float64(group.loc[(per_day, 'all')][name].copy())
                occupied_all += np.float64(group.loc[(per_day, 'occupied')][name].copy())
            period_name = str(int(name)) + ':00-' + str(int(name)+int(1)) + ':00'
        aver_perc = np.float64(occupied_all / sum_all)
        df_averperc_list[(np.int64(name), period_name)] = pd.Series([aver_perc], index=[days_type])
    df_averperc = pd.DataFrame(df_averperc_list)
    df_averperc.sort_index(axis=1, inplace=True)
    df_averperc.to_csv(sapa)

# average_several_percentage_hour(
#      Basepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\all_one_hour\HK_period.csv",
#      Savepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\other_types",
#      days_type="weekday",
#      days_name=(20210413, 20210414, 20210415, 20210420, 20210421, 20210422))
# average_several_percentage_hour(
#     Basepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\all_one_hour\HK_period.csv",
#     Savepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\other_types",
#     days_type="weekend",
#     days_name=(20210417, 20210418, 20210424, 20210425))

## this script can calculate one hour percentage in one area_csv path
## this area_csv has two level index, one is date, and the other is 'content' which consists of
## 'Occupied Percentage', 'all', 'occupied'
## Savepath is folder path
def average_period_percentage(Basepath, Savepath):
    global concat_data_list
    bapa = p(Basepath)
    save_parent = p(Savepath)
    sapa_name = bapa.stem + '_' + 'period' + '.csv'
    sapa = save_parent / sapa_name
    base_df = pd.read_csv(bapa, header=0, index_col=[0, 1])
    group_day = base_df.groupby(axis=0, level=0)
    occupied_list = pd.DataFrame()
    all_list = pd.DataFrame()
    percentage_list = pd.DataFrame()
    i_co = int(0)
    concat_data_list = []
    for day_name, day_group in group_day:
        group_period = day_group.groupby(axis=1, level=0)
        # values of 24 periods will be saved in these list
        occupied_list = np.zeros(24)
        all_list = np.zeros(24)
        percentage_list = np.zeros(24)
        df_oc_list = {}
        df_all_list = {}
        df_perc_list = {}
        for minute_name, minute_group in group_period:
            period_name = str(int(int(minute_name)*0.01)) + ':00-' + str(int(int(minute_name)*0.01+1)) + ':00'
            list_number = int(int(minute_name)*0.01)
            occupied_list[list_number] += np.float64(minute_group.loc[day_name, "occupied"][minute_name].copy())
            all_list[list_number] += np.float64(minute_group.loc[day_name, "all"][minute_name].copy())
            percentage_list[list_number] = occupied_list[list_number] / all_list[list_number]

            in_oc = pd.MultiIndex.from_product([[day_name], ["occupied"]])
            df_oc_list[(int(int(minute_name)*0.01), period_name)] = pd.Series(occupied_list[list_number], index=in_oc)
            in_all = pd.MultiIndex.from_product([[day_name], ["all"]])
            df_all_list[(int(int(minute_name)*0.01), period_name)] = pd.Series(all_list[list_number], index=in_all)
            in_perc = pd.MultiIndex.from_product([[day_name], ["Occupied Percentage"]])
            df_perc_list[(int(int(minute_name)*0.01), period_name)] = pd.Series(percentage_list[list_number],
                                                                                index=in_perc)

        df_oc = pd.DataFrame(df_oc_list)
        df_oc.sort_index(axis=1, inplace=True)
        df_all = pd.DataFrame(df_all_list)
        df_all.sort_index(axis=1, inplace=True)
        df_perc = pd.DataFrame(df_perc_list)
        df_perc.sort_index(axis=1, inplace=True)
        df_per_day = pd.concat([df_oc, df_all, df_perc], axis=0)
        df_per_day.sort_index(level=0, axis=0, inplace=True)
        concat_data_list.append(df_per_day)
        i_co += int(1)
    final_data = pd.concat(concat_data_list, axis=0)
    final_data.sort_index(level=0, axis=0, inplace=True)
    final_data.sort_index(level=0, axis=1, inplace=True)
    final_data.to_csv(sapa)
    print('done!!')

# average_period_percentage(Basepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\3\Sha Tin.csv",
#                           Savepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\3")

# average_period_percentage(
#     Basepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\all_five_minutes\HK.csv",
#     Savepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\all_one_hour")
