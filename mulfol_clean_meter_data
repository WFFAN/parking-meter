## this document is used to clean repeated rows and space rows in parking meter data
## this document based on clean_meter_data.py, which can deal with csv_data under one folder
## while this one can use for more folders under one parent path
import pandas as pd
from pathlib import Path as p
from clean_meter_data import clean_data as c_d

# create folder, how to name it and saved path
# how to clean data in different folder
def mulfol_clean_data(based_parent_folder, saved_parent_folder):
    #based_parent_path include piece_basedfolder
    based_parent_path = p(based_parent_folder)
    # saved_parent_path include piece_savedfolder
    saved_parent_path = p(saved_parent_folder)
    for piece_basedfolder in based_parent_path.iterdir():
        piece_savedfolder_name = piece_basedfolder.name
        piece_savedfolder = saved_parent_path/piece_savedfolder_name

        #every 'for' circle creates new folder the same name as original folder name
        #if this folder exist, then it will be continued
        piece_savedfolder.mkdir(exist_ok=True,parents=True)

        #now let's clean original csv in every day folder(namely,'piece_basedfolder')
        #piece_csv means original every csv path under everyday folder
        c_d(need_clean_path=piece_basedfolder, saved_path=piece_savedfolder)
    print('DONE!!!')

# mulfol_clean_data(based_parent_folder=r'D:\POLYU_dissertation\meter_July_2021',
#                   saved_parent_folder=r'D:\POLYU_dissertation\clean_meter_July_2021')

mulfol_clean_data(based_parent_folder=r'E:\2022dissertation\August_Sept_ori',
                  saved_parent_folder=r'E:\2022dissertation\August_Sept_clean')
