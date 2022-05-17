import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import re
from pathlib import Path as p, Path
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter
from identify_weekday_list import weekend_weekday as ww
import matplotlib.dates as mdates
from datetime import datetime
from datetime import time
from numpy import ndarray
import seaborn as sns

# this programme is a heatmap of day-district pattern of on-street parking

plt.rcParams["figure.figsize"] = (10, 10)
bapa = p(r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\all_percentage")
district = []
ne_arr = np.zeros((18,  288),dtype="float32")
i = 0
for piece in bapa.iterdir():
    df = pd.read_csv(piece, header=0, index_col=0)
    district.append(piece.stem.split("_")[0])
    arr = df.to_numpy(dtype="float32")
    arr = np.around(arr, decimals=2)
    # print(arr)
    ne_arr[i, :] = np.array(arr)
    i += 1

ba_li= bapa / r"Central & Western_days.csv"
df_time = pd.read_csv(ba_li, index_col=0, header=0)
time_y_ori = list(df_time.columns)
time_y_ori[0:12] = ['000', '005', '010', '015', '020', '025',
                        '030', '035', '040', '045', '050', '055']
time_y_ori[0:120] = ['0' + x for x in time_y_ori[0:120]]
time_y = [datetime.strptime(d, '%H%M') for d in time_y_ori]
time_y_ori = [x[0:2] + ":" + x[2:4] for x in time_y_ori]

print(time_y_ori)
print(ne_arr)
print(ne_arr.shape)
# print(time_y)
district_arr = np.array(district)
df = pd.DataFrame(ne_arr.T, index=time_y_ori, columns=district_arr)

ax = sns.heatmap(df,xticklabels=True, yticklabels=6,cmap="nipy_spectral")



ax.set_ylabel("Time", color="0.25",fontsize=20)
ax.set_xlabel("District", color="0.25",fontsize=20)
# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=25, ha="right",
         rotation_mode="anchor")

ax.set_title("Heat map of the mean on-street parking occupancy rate\n per five minutes for July 2021 in Hong Kong",
             fontsize=20, ha="center")

plt.savefig(r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\figures\HK_day_district_heatmap.png")
