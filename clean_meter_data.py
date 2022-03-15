## clean_meter_data.py can deal with csv_data under one folder(input one parent path)
import pandas as pd
from pathlib import Path as p
# need_clean_path should input a parent path, namely every_day folder
# saved_path should give a created parent path, namely folder to save every_csv
def clean_data(need_clean_path,saved_path):
    p_need_clean_path = p(need_clean_path)
    p_saved_path = p(saved_path)
    # header=0 means the first row will be its name
    for piecepath in p_need_clean_path.iterdir():
        created_name = piecepath.name
        created_path = p_saved_path / created_name
        #header=0 means the first row will be its name
        #index_col=False means that the first column is not seen as index
        #keep_default_na=False means 'NA' in original csv can be read
        df = pd.read_csv(piecepath, header=0, index_col=False, keep_default_na=False)
        ##df.dropna can delete empty row or column, axis=0 means delete row, axis=1 means delete column
        #how='all' means the whole row(or column) is empty will be deleted
        #how='any' means every empty value will cause row(or column be deleted)
        ##drop_duplicates can delete repeated row by given column's name
        clean1_df = df.dropna(axis=0, how='all')
        clean2_df = clean1_df.drop_duplicates(['ParkingSpaceId'])
        clean2_df.to_csv(created_path, index=False)
    return print('done')

## path = p(r'C:\Users\Asus\OneDrive - The Hong Kong Polytechnic University\Desktop\ok.csv')
## path2 = p(r'C:\Users\Asus\OneDrive - The Hong Kong Polytechnic University\Desktop\clean.csv')
# clean_data(need_clean_path=r'D:\POLYU_dissertation\meter_Oct_Nov_2021\20211001',
#            saved_path=r'D:\POLYU_dissertation\clean_Oct_Nov_2021')
