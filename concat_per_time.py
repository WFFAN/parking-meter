import pandas as pd
from pathlib import Path as p
import numpy as np

# this script can base one folder path to concat csv_doc inside
# column name will be sorted and data will be numerical
def time_day(Basepath, Savepath):
    base_path = p(Basepath)
    save_folder = p(Savepath)
    bapa_name = base_path.name
    save_name = bapa_name + '.csv'
    save_path = save_folder/save_name
    df_dic = {}
    for piece_csv in base_path.iterdir():
        piece_name = piece_csv.name
        piece_time = int(int(piece_csv.stem)*0.01)

        #index_col=False,,to ignore the index
        df_piece = pd.read_csv(piece_csv, index_col=False, header=0)

        #select the useful data in original data
        #to facilitate calculation later, dtype set as np.int64
        df_dic[piece_time] = pd.Series(df_piece.loc[:]['OccupancyStatus'].copy(), dtype=np.int64)
    df = pd.DataFrame(df_dic)
    df.columns.name = 'time'
    df.sort_index(axis=1, inplace=True)
    df.to_csv(save_path, index=False)
    print('done')

# time_day(Basepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\1\20210413",
#          Savepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\2")
