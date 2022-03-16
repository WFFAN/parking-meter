import pandas as pd
from pathlib import Path as p
import numpy as np
from pandas import DataFrame
from calculate_time_percentage import per_csv_percentage as cper

# this script can calculate merters occupied% every 5 minutes in one folder
def concat_per_csv_percentage(Basefolder, Savepath):
    bapa = p(Basefolder)
    sapa = p(Savepath)
    concat_csv_list = []
    for piece_csv in bapa.iterdir():
        piece_data = cper(csvpath=piece_csv)
        concat_csv_list.append(piece_data)
    data_final = pd.concat(concat_csv_list, axis=0)
    data_final.sort_index(axis=0, inplace=True)
    data_final.to_csv(sapa)
    print('Done!!!')

# concat_per_csv_percentage(Basefolder=r"D:\POLYU_dissertation\parking_meter_0412_0425\area_meters_0412_0425\concat_day_HK",
#                            Savepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data"
#                                     r"\HK\all_five_minutes\HK.csv")
