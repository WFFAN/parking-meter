import pandas as pd
from pathlib import Path as p

path_parent =p(r"E:\2022dissertation\July") 

Basepath=\
    r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\per_district\all_five_minutes\Sha Tin.csv "

bapa = p(Basepath)
df_1 = pd.read_csv(bapa, index_col=[0, 1], header=0)
time_x_ori = list(df_1.columns)
time_x_ori[0:12] = ['000', '005', '010', '015', '020', '025',
                    '030', '035', '040', '045', '050', '055']
time_x_ori[0:120] = ['0' + x for x in time_x_ori[0:120]]
print(time_x_ori)

for medium_path in path_parent.iterdir():

    if len(list(p(medium_path).iterdir())) != 288:
        print("not 288")
        print(medium_path)
        print(len(list(p(medium_path).iterdir())))

    for piece_path in medium_path.iterdir():
        name = piece_path.stem
        ne_na = name[:-2]
        if ne_na not in time_x_ori:
           print("not 5")
           print(piece_path)

        if piece_path.stat().st_size == 0:
            print("empty")
            print(piece_path)
