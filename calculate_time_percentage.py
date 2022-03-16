import pandas as pd
from pathlib import Path as p
import numpy as np
from pandas import DataFrame

# this script can calculate merters occupied% every 5 minutes in one csv doc
def per_csv_percentage(csvpath):
    path = p(csvpath)
    df = pd.read_csv(path, index_col=False, header=0, keep_default_na=True, dtype=np.float64)
    # set index type
    df.index.astype(dtype=np.int64, copy=True)
    # print(df.index.dtype)
    # groupby time
    df_grouped = df.groupby(axis=1, level=0)
    df_occupied_list = {}
    df_all_list = {}
    df_percentage_list = {}
    for name, group in df_grouped:
        occupied_meter = np.float64(group.sum())
        all_meter = np.float64(group.count())
        # calculate occupied percentage every 5 minutes
        per_time_percentage = np.float64(occupied_meter / all_meter)
        ind_occu = pd.MultiIndex.from_product([[int(path.stem)], ['occupied']])
        df_occupied_list[np.int64(name)] = pd.Series([occupied_meter], index=ind_occu)
        ind_all = pd.MultiIndex.from_product([[int(path.stem)], ['all']])
        df_all_list[np.int64(name)] = pd.Series([all_meter], index=ind_all)
        # print(per_time_percentage)
        ind_perc = pd.MultiIndex.from_product([[int(path.stem)], ['Occupied Percentage']])
        df_percentage_list[np.int64(name)] = pd.Series([per_time_percentage], index=ind_perc)
    df_occupied = pd.DataFrame(df_occupied_list)
    df_occupied.sort_index(axis=1, inplace=True)
    df_all = pd.DataFrame(df_all_list)
    df_all.sort_index(axis=1, inplace=True)
    df_percentage = pd.DataFrame(df_percentage_list)
    df_percentage.sort_index(axis=1, inplace=True)
    df_final = pd.concat([df_occupied, df_all, df_percentage], axis=0)
    df_final.columns.name = "time"
    df_final.sort_index(level=0, axis=0, inplace=True)
    print('done')
    return df_final
    ## df_test = pd.concat([df_percentage, df_percentage2], axis=0)
    # print(df_test.dtypes)
    # print(df_percentage)
    # path2 = p(r"D:\POLYU_dissertation\parking_meter_0412_0425\2\co20210414.csv")
    # df_test.to_csv(path2)
