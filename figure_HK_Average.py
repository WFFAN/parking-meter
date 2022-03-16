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

# if type=="weekend_weekday"
# Basepath=weekend path
# Basepath2 =weekday path

def figure_hk_many(Basepath_allfive, Basepath_avweknd, Basepath_avwkday, Basepath_avperday,Savepath):
    bapa = p(Basepath_allfive)
    bapa_weknd = p(Basepath_avweknd)
    bapa_wkday = p(Basepath_avwkday)
    bapa_day = p(Basepath_avperday)

    sapa = p(Savepath)
    df_1 = pd.read_csv(bapa, index_col=[0, 1], header=0)
    df_weknd = pd.read_csv(bapa_weknd, index_col=0, header=0)
    df_wkday = pd.read_csv(bapa_wkday , index_col=0, header=0)
    df_day = pd.read_csv(bapa_day, index_col=0, header=0)
    # time_x = np.array(df_1.columns)
    # time_x = time_x.astype(np.int64)
    ne_value = "Occupied Percentage"
    time_x_ori = list(df_weknd.columns)
    time_x_ori[0:12] = ['000', '005', '010', '015', '020', '025',
                        '030', '035', '040', '045', '050', '055']
    time_x_ori[0:120] = ['0' + x for x in time_x_ori[0:120]]
    # convert numerical value to date_string (Hour, Minutes)
    time_x = [datetime.strptime(d, '%H%M') for d in time_x_ori]


    date_list = df_1.index.get_level_values(0).tolist()
    date_list = tuple(set(date_list))
    weekday_list = ww(list_date=date_list, type="weekday")
    weekend_list = ww(list_date=date_list, type="weekend")
    Sat_list = ww(list_date=date_list, type="Saturday")
    Sun_list = ww(list_date=date_list, type="Sunday")


    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(111)

    # set x y major_tick_locator
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%#H'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax.yaxis.set_major_locator(MultipleLocator(0.05))
    # change the appearance of ticks and tick labels
    # ax.tick_params(which='major', length=5, width=1, labelsize=12, colors="0.25")  # width=1
    # ax.tick_params(which='minor', length=2, width=0.4, labelsize=12, labelcolor="0.25")  # width=0.4
    ax.tick_params(which='major', length=5, width=0, labelsize=12, colors="#005C80", labelcolor="#005C80")  # width=1
    ax.tick_params(which='minor', length=2, width=0, labelsize=12, colors="#005C80",labelcolor="#005C80")  # width=0.4
    ax.set_ylim(0, 1)
    ax.set_xlim([time_x[0], time_x[-1]])

    ax.set_xlabel("time (hr)",  color="#005C80",fontsize=18, loc="right", fontstyle='italic')
    ax.set_ylabel("Occupied Parking Meters Percentage", color="#005C80",fontsize=18, fontstyle='italic')
    # color_list=["#ABB8BF", "#FFB6A2", "#45B86D", "#FFB16F", "#FF5DAB"]#C1C8FF"
    color_list = ["#C2C5CA", "#FFB6A2", "#FF0267", "#007CFF", "#00A011"]
    for x_n in ['top', "bottom", "left", "right"]:
       ax.spines[x_n].set_color('#005C80') #none
    ax.grid(ls="--", lw=1, color="#98CDD5")#, color="#e0e0e0")# , color="#FFFFFF")
    #ax.set(facecolor="#EDF3FF")  #"#EDF3FF"#FFE7D3, #CCD2FF #E3E6FF
    for i, per_day in enumerate(date_list):
        all_y = np.array(df_1.loc[(per_day, ne_value)].copy())
        if i == 0:
            plt.plot(time_x, all_y, ls="-", lw=0.8, label="per day", color=color_list[0])
        else:
            plt.plot(time_x, all_y, ls="-", lw=0.8, color=color_list[0])
    Aver_days = np.array(df_day.loc["days"].copy())
    plt.plot(time_x, Aver_days, ls="-", lw=2.2, label="average days", color=color_list[4])
    Aver_weekend = np.array(df_weknd.loc["weekend"].copy())
    plt.plot(time_x, Aver_weekend, ls="--", lw=2.2, label="average weekend", color=color_list[2])
    Aver_weekday = np.array(df_wkday.loc["weekday"].copy())
    plt.plot(time_x, Aver_weekday, ls="-.", lw=2.2, label="average weekday", color=color_list[3])




    plt.legend(
        loc="upper left", bbox_to_anchor=(0.001, -0.08), ncol=4, frameon=False, handleheight=0.3,
        handlelength=2, fontsize=12, title_fontsize=8, labelspacing=0.15, borderpad=0.3, columnspacing=5)
    title_name = bapa.stem + " Occupied Parking Meters Percentage\n"
    plt.subplots_adjust(wspace=0.1, hspace=0.3)
    fig.text(0.5, 0.93, title_name, color="#005C80", fontsize=20, ha='center', va="top", fontstyle="italic")
    plt.savefig(sapa, dpi=400)


# figure_hk_many(Basepath_allfive=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\all_five_minutes\HK.csv",
#                Basepath_avweknd=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\other_types\HK_weekend.csv",
#                Basepath_avwkday=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\other_types\HK_weekday.csv",
#                Basepath_avperday=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\other_types\HK_days.csv",
#                Savepath=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\figures\HK_average1.png")
figure_hk_many(
Basepath_allfive=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK"
                                r"\all_five_minutes\HK.csv",
Basepath_avweknd=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\weekend_percentage"
                 r"\HK_weekend.csv",
Basepath_avwkday=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\weekday_percentage"
                 r"\HK_weekday.csv",
Basepath_avperday=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_percentage"
                  r"\HK_days.csv",
Savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\figures\HK_average.png")
