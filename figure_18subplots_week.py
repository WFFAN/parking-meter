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



def figure_weekend_weekday(ax, Basepath, Basepath2, Savepath, type):
    bapa = p(Basepath)
    bapa2 = p(Basepath2)
    sapa = p(Savepath)
    df_1 = pd.read_csv(bapa, index_col=[0, 1], header=0)
    df_2 = pd.read_csv(bapa2, index_col=0, header=0)
    # time_x = np.array(df_1.columns)
    # time_x = time_x.astype(np.int64)
    ne_value = "Occupied Percentage"
    time_x_ori = list(df_2.columns)
    time_x_ori[0:12] = ['000', '005', '010', '015', '020', '025',
                        '030', '035', '040', '045', '050', '055']
    time_x_ori[0:120] = ['0' + x for x in time_x_ori[0:120]]
    # convert numerical value to date_string (Hour, Minutes)
    time_x = [datetime.strptime(d, '%H%M') for d in time_x_ori]


    date_list = df_1.index.get_level_values(0).tolist()
    if type == "weekday":
        holiday_list = [20210701, 20210922]  # HK holiday
        for per_hol in holiday_list:
            while per_hol in date_list:
                date_list.remove(per_hol)
    date_list = tuple(set(date_list))
    weekday_list = ww(list_date=date_list, type="weekday")
    weekend_list = ww(list_date=date_list, type="weekend")
    Sat_list = ww(list_date=date_list, type="Saturday")
    Sun_list = ww(list_date=date_list, type="Sunday")

    ax = ax
    fig = plt.figure(figsize=(8, 6))

    # set x y major_tick_locator
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%#H'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))
    ax.yaxis.set_major_locator(MultipleLocator(0.2))

    # change the appearance of ticks and tick labels
    ax.tick_params(which='major', direction="in",
    length=1.5, width=1, labelsize=8, colors="#005C80", labelcolor="#005C80")  # width=1

    ax.set_ylim(0, 1)
    ax.set_xlim([time_x[0], time_x[-1]])

    #ax.set_xlabel("time (hr)", color="#005C80",fontsize=15, loc="right", fontstyle='italic')
    #ax.set_ylabel("Occupied Parking Meters Percentage", color="#005C80",fontsize=15, fontstyle='italic')
    color_list=["#ABB8BF", "#FFB6A2", "#57F7C1", "#FD7F14"]#C1C8FF"   flour_blue #6FFACC purple#D400F7 orange#FFB16F

    for x_n in ['top', "bottom", "left", "right"]:
       ax.spines[x_n].set_color('#005C80') #none
    ax.grid(ls="--",color="#98CDD5", lw=0.3)
    # ax.grid(ls="--", lw=1, color="#98CDD5")#, color="#e0e0e0")# , color="#FFFFFF")

    if type == "weekend":
        for i, wekd in enumerate(weekend_list):
            Wekd_y = np.array(df_1.loc[(wekd, ne_value)].copy())
            if i == 0:
                ax.plot(time_x, Wekd_y, ls="-", lw=0.4, label="weekend", color=color_list[0])
            else:
                ax.plot(time_x, Wekd_y, ls="-", lw=0.4, color=color_list[0])

        Aver_weekend = np.array(df_2.loc["weekend"].copy())
        ax.plot(time_x, Aver_weekend, ls="-", lw=0.7, label="average weekend", color=color_list[2])

    elif type == "weekday":
        for i, wed in enumerate(weekday_list):
            Sat_y = np.array(df_1.loc[(wed, ne_value)].copy())
            if i == 0:
                ax.plot(time_x, Sat_y, ls="-", lw=0.4, label="weekday", color=color_list[0])
            else:
                ax.plot(time_x, Sat_y, ls="-", lw=0.4, color=color_list[0])

        Aver_weekday = np.array(df_2.loc["weekday"].copy())
        ax.plot(time_x, Aver_weekday, ls="-", lw=0.7, label="average weekday", color=color_list[3])

    if bapa.stem == "Hong Kong":
        title_name = "Hong Kong Island" + " Occupied Parking Meters Percentage\n" + "(" + type.title() + ")"
    else:
        title_name = bapa.stem + "\n("+ type.title()+ ")"
    #ax.subplots_adjust(wspace=0.1, hspace=0.3)
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
             rotation_mode="anchor")
    #ax.text(0.5,1,title_name,color="0.25", fontsize=12, ha='center', va="top", fontstyle="italic" )
    ax.set_title(title_name,color="0.25", fontsize=10, ha='center', y=1.0, fontstyle="italic" )

# create a figure contains 6*6 subplots
fig_all, axes = plt.subplots(6,6, sharex=True, sharey=True,figsize=(12, 10))

ax = axes.flatten()
i = 0
# weekend
bafo1 = p(r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\all_five_minutes")
bafo2 = p(r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\weekend_percentage")
safo = p(r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\figures")
for piece_csv in bafo1.iterdir():
    nename = piece_csv.stem + "_" + "weekend" + ".csv"
    save_name = piece_csv.stem + "_" + "weekend" + ".png"
    sapa = safo / save_name
    bapa_1 = piece_csv
    bapa_2 = bafo2 / nename
    figure_weekend_weekday(ax=ax[i], Basepath=bapa_1,
                           Basepath2=bapa_2,
                           Savepath=sapa, type="weekend")
    print(i)
    i += 1

# weekday
bafo1 = p(r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\all_five_minutes")
bafo2 = p(r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\weekday_percentage")
safo = p(r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\HK\figures")
for piece_csv in bafo1.iterdir():
    nename = piece_csv.stem + "_" + "weekday" + ".csv"
    save_name = piece_csv.stem + "_" + "weekday" + ".png"
    sapa = safo / save_name
    bapa_1 = piece_csv
    bapa_2 = bafo2 / nename
    figure_weekend_weekday(
        ax=ax[i], Basepath=bapa_1,
        Basepath2=bapa_2,
        Savepath=sapa, type="weekday")
    plt.cla()
    print(i)
    i += 1
fig_all.subplots_adjust(hspace=0.5, wspace=0.2)
fig_all.subplots_adjust(bottom=0.2)

fig_all.legend(
        loc="upper left", bbox_to_anchor=(0.001, -0.06), ncol=3, frameon=False, handleheight=0.3,
        handlelength=3, fontsize=12, title_fontsize=8, labelspacing=0.25, borderpad=0.3, columnspacing=8)
title_name ="18 Districts Occupied Parking Meters Percentage\n"+"(Weekend & Weekday)"
fig_all.text(0.5,0.15,"time (hr)", color="#005C80", fontsize=15, ha="center", fontstyle='italic')
fig_all.text(0.08,0.5,"Occupied Parking Meters Percentage", color="#005C80",
             rotation='vertical', va="center", fontsize=15, fontstyle='italic')
fig_all.text(0.5, 0.98, title_name, color="0.25", fontsize=20, ha='center', va="top", fontstyle="italic")
fig_all.savefig(r"C:\Users\Asus\OneDrive - The Hong Kong Polytechnic University\Desktop\s2.png", dpi=400)


r"""
figure_by(
Basefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\all_five_minutes",
Basefolder2=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\weekend_percentage",
Savefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\figures\weekend",
type="weekend")

figure_by(
Basefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\all_five_minutes",
Basefolder2=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\weekday_percentage",
Savefolder=r"D:\POLYU_dissertation\July_2021_useful\useful_percentage_data\per_district\figures\weekday",
type="weekday")
"""
