import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path as p
import re
import meter_dictionary as medi


def meters_by_district(Baseparent, Saveparent, dictpath, div_by):
    bapa = p(Baseparent)
    sapa = p(Saveparent)

    # to create saved area folder path
    makfol_list = medi.info_type_list(dict_path=dictpath, info_name=div_by)
    for fol_name in makfol_list:
        sav_div_folpa = p(Saveparent) / fol_name
        sav_div_folpa.mkdir(exist_ok=True)

    for folder_path in bapa.iterdir():
        # to create save day_csv folder path
        sav_day_folname = folder_path.name

        for piece in folder_path.iterdir():
            sapi_name = piece.name
            df_ori = pd.read_csv(piece, header=0, index_col=0, keep_default_na=True)
            drop_list = medi.useless_spaceid(path_name=dictpath) ### delete useless space ID (If needed)
            grouped_csv = df_ori.groupby('ParkingSpaceId')  ### delete useless space ID (If needed)
            df_drme = df_ori.copy()

            ### delete useless space ID (If needed)
            for name, group in grouped_csv:
                if name in drop_list:
                    df_drme.drop(name, axis=0)
            mapping = medi.info_meter_dict(dict_path=dictpath, info_name=div_by)

            # groupby div_by (etc. 'District')
            group_clean = df_drme.groupby(mapping, axis=0)
            for dist_name, group in group_clean:
                # to create multiple path
                sav_fipa_fol = sapa / dist_name / sav_day_folname
                sav_fipa_fol.mkdir(exist_ok=True, parents=True)
                sav_fipa = sav_fipa_fol / sapi_name
                sav_df = group.copy()
                sav_df.to_csv(sav_fipa)
        print('done!')
    print('DONE!!!DONE!!!!')

# sample
# meters_by_district(Baseparent=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\by_HK\HK",
#                     Saveparent=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\by_region",
#                     dictpath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\parkingspaces_211206_dict.csv",
#                     div_by=r"Region")
# meters_by_district(Baseparent=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\by_HK\HK",
#                     Saveparent=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\area\by_district",
#                     dictpath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\parkingspaces_211206_dict.csv",
#                     div_by=r"District")


