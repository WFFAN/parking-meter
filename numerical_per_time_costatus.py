import pandas as pd
import numpy as np
import re
from pathlib import Path as p

# This script consider meters status, if status is NA then this row will be deleted,
# so, this row's OccupancyStatus will be removed
# convert per 5 minutes csv to numerical csv, only have ParkingMeterStatus

def numerical_fimin_costatus(Baseparentpath, Saveparentpath):
    base_parent = p(Baseparentpath)
    save_parent = p(Saveparentpath)
    for mid_path in base_parent.iterdir():
        save_folder_name = mid_path.name
        save_mid_path = save_parent/save_folder_name
        save_mid_path.mkdir(exist_ok=True)
        for piece in mid_path.iterdir():
            
            save_doc_name = piece.name
            save_doc_path = save_mid_path/save_doc_name
            df_o = pd.read_csv(piece, header=0, index_col=False, keep_default_na=True)
            df_o.dropna(how='any', axis=0, inplace=True)
            df1 = df_o.loc[:, ('ParkingSpaceId', 'OccupancyStatus')].copy()#
            df1.replace(['O', 'V'], [int(1), int(0)], inplace=True)
            ## ori_list = df1.loc[:, 'ParkingSpaceId'].copy()#
            ## fns = lambda s: sum(((int(n), s)for n, s in re.findall(r"(\d+)(\D+)", '0%sZ'%s)), ())
            ## so_list = sorted(ori_list, key=fns)
            ## df1['ParkingSpaceId'] = df1['ParkingSpaceId'].astype('category')
            ## df1['ParkingSpaceId'].cat.reorder_categories(so_list, inplace=True)
            ### print(so_list)
            ## df1.sort_values(by=['ParkingSpaceId'], axis=0, inplace=True)
            df1.to_csv(save_doc_path, index=False)
        print('done')
    print('DONE!!!')

numerical_fimin_costatus(Baseparentpath=r"D:\POLYU_dissertation\clean_meter_July_2021",
                 Saveparentpath=r"D:\POLYU_dissertation\July_2021_useful\area\by_HK")

