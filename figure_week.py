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

def figure_weekend_weekday(Basepath, Basepath2, Savepath, type):
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


    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111)

    # set x y major_tick_locator
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%#H'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax.yaxis.set_major_locator(MultipleLocator(0.05))
    # change the appearance of ticks and tick labels
    ax.tick_params(which='major', length=5, width=1, labelsize=12, colors="#005C80", labelcolor="#005C80")  # width=1
    ax.tick_params(which='minor', length=2, width=0.4, labelsize=12, colors="#005C80", labelcolor="#005C80")  # width=0.4
    # ax.tick_params(which='major', length=5, width=0, labelsize=12, colors="0.25")  # width=1
    # ax.tick_params(which='minor', length=2, width=0, labelsize=12, labelcolor="0.25")  # width=0.4
    ax.set_ylim(0, 1)
    ax.set_xlim([time_x[0], time_x[-1]])

    ax.set_xlabel("time (hr)", color="#005C80",fontsize=18, loc="right", fontstyle='italic')
    ax.set_ylabel("Occupied Parking Meters Percentage", color="#005C80",fontsize=18, fontstyle='italic')
    color_list=["#ABB8BF", "#FFB6A2", "#57F7C1", "#FD7F14"]#C1C8FF"   flour_blue #6FFACC purple#D400F7 orange#FFB16F
    # for x_n in ['top', "bottom", "left", "right"]:
    #      ax.spines[x_n].set_color('none')
    #  ax.grid(ls="-", lw=1, color="#FFFFFF")# , color="#FFFFFF")
    #  ax.set(facecolor="#EDF3FF")  #"#EDF3FF"#FFE7D3, #CCD2FF #E3E6FF
    for x_n in ['top', "bottom", "left", "right"]:
       ax.spines[x_n].set_color('#005C80') #none
    ax.grid(ls="--", lw=1, color="#98CDD5")#, color="#e0e0e0")# , color="#FFFFFF")

    if type == "weekend":
        for i, wekd in enumerate(weekend_list):
            Wekd_y = np.array(df_1.loc[(wekd, ne_value)].copy())
            if i == 0:
                plt.plot(time_x, Wekd_y, ls="-", lw=0.8, label="weekend", color=color_list[0])
            else:
                plt.plot(time_x, Wekd_y, ls="-", lw=0.8, color=color_list[0])

        #for n, sun in enumerate(Sun_list):
        #    Sun_y = np.array(df_1.loc[(sun, ne_value)].copy())
        #    if n==0:
        #        plt.plot(time_x, Sun_y, ls="-", lw=0.8, label="Sunday", color=color_list[1])
        #    else:
        #        plt.plot(time_x, Sun_y, ls="-", lw=0.8, color=color_list[1])

        Aver_weekend = np.array(df_2.loc["weekend"].copy())
        plt.plot(time_x, Aver_weekend, ls="-", lw=1.8, label="average weekend", color=color_list[2])

    elif type == "weekday":
        for i, wed in enumerate(weekday_list):
            Sat_y = np.array(df_1.loc[(wed, ne_value)].copy())
            if i == 0:
                plt.plot(time_x, Sat_y, ls="-", lw=0.8, label="weekday", color=color_list[0])
            else:
                plt.plot(time_x, Sat_y, ls="-", lw=0.8, color=color_list[0])

        Aver_weekday = np.array(df_2.loc["weekday"].copy())
        plt.plot(time_x, Aver_weekday, ls="-", lw=1.8, label="average weekday", color=color_list[3])
    elif type == "days":
        for i, per_day in enumerate(weekday_list):
            all_y = np.array(df_1.loc[(per_day, ne_value)].copy())
            if i == 0:
                plt.plot(time_x, all_y, ls="-", lw=0.8, label="per day", color=color_list[0])
            else:
                plt.plot(time_x, all_y, ls="-", lw=0.8, color=color_list[0])

        Aver_days = np.array(df_2.loc["days"].copy())
        plt.plot(time_x, Aver_days, ls="-", lw=1.8, label="average days", color=color_list[2])

    plt.legend(
        loc="upper left", bbox_to_anchor=(0.001, -0.06), ncol=3, frameon=False, handleheight=0.3,
        handlelength=3, fontsize=12, title_fontsize=8, labelspacing=0.25, borderpad=0.3, columnspacing=8)
    if bapa.stem == "Hong Kong":
        title_name = "Hong Kong Island" + " Occupied Parking Meters Percentage\n" + "(" + type.title() + ")"
    else:
        title_name = bapa.stem + " Occupied Parking Meters Percentage\n"+"("+ type.title()+ ")"
    plt.subplots_adjust(wspace=0.1, hspace=0.3)
    fig.text(0.5, 1.001, title_name, color="0.25", fontsize=20, ha='center', va="top", fontstyle="italic")
    plt.savefig(sapa, dpi=400)




#figure_weekend(
#   Basepath=r"D:\POLYU_dissertation\parking_meter_0412_0425"
#            r"\useful_percentage_data\per_district\all_five_minutes\Sha Tin.csv",
#   Basepath2=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data"
#             r"\per_district\other_types\Sha Tin_weekday.csv",
#   Savepath=r"C:\Users\Asus\OneDrive - The Hong Kong Polytechnic University\Desktop\f4",
#   type="weekday")


def figure_aver_ww(Basepath_weekend, Basepath_weekday, Savepath):
    bapa_weekend = p(Basepath_weekend)
    bapa_weekday = p(Basepath_weekday)
    sapa = p(Savepath)
    df_weekend = pd.read_csv(bapa_weekend, index_col=0, header=0)
    df_weekday = pd.read_csv(bapa_weekday, index_col=0, header=0)
    time_x_ori = list(df_weekend.columns)
    time_x_ori[0:12] = ['000', '005', '010', '015', '020', '025',
                        '030', '035', '040', '045', '050', '055']
    time_x_ori[0:120] = ['0' + x for x in time_x_ori[0:120]]
    # convert numerical value to date_string (Hour, Minutes)
    time_x = [datetime.strptime(d, '%H%M') for d in time_x_ori]

    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111)

    # set x y major_tick_locator
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%#H'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax.yaxis.set_major_locator(MultipleLocator(0.05))
    # change the appearance of ticks and tick labels
    ax.tick_params(which='major', length=5, width=1, labelsize=12, colors="#005C80", labelcolor="#005C80")  # width=1
    ax.tick_params(which='minor', length=2, width=0.4, labelsize=12,colors="#005C80", labelcolor="#005C80")  # width=0.4
    ax.set_ylim(0, 1)
    ax.set_xlim([time_x[0], time_x[-1]])

    ax.set_xlabel("time (hr)", color="#005C80",fontsize=18, loc="right", fontstyle='italic')
    ax.set_ylabel("Occupied Parking Meters Percentage", color="#005C80",fontsize=18, fontstyle='italic')
    color_list=["#ABB8BF", "#FFB6A2", "#6FFACC", "#FFB16F"]#C1C8FF"
    for x_n in ['top', "bottom", "left", "right"]:
       ax.spines[x_n].set_color('#005C80') #none
    ax.grid(ls="--", lw=1, color="#98CDD5")#, color="#e0e0e0")# , color="#FFFFFF")
    Aver_weekend = np.array(df_weekend.loc["weekend"].copy())
    plt.plot(time_x, Aver_weekend, ls="-", lw=1.8, label="average weekend", color=color_list[2])

    Aver_weekday = np.array(df_weekday.loc["weekday"].copy())
    plt.plot(time_x, Aver_weekday, ls="-", lw=1.8, label="average weekday", color=color_list[3])

    plt.legend(
        loc="upper left", bbox_to_anchor=(0.001, -0.06), ncol=3, frameon=False, handleheight=0.3,
        handlelength=3, fontsize=12, title_fontsize=8, labelspacing=0.25, borderpad=0.3, columnspacing=8)
    if bapa_weekend.stem.split("_")[0] == "Hong Kong":
        title_name = "Hong Kong Island" + " Occupied Parking Meters Percentage\n"+\
                     "(average weekend & average weekday)"
    else:
        title_name = bapa_weekend.stem.split("_")[0] + " Occupied Parking Meters Percentage\n"+"(average weekend & average weekday)"
    plt.subplots_adjust(wspace=0.1, hspace=0.3)
    fig.text(0.5, 1.001, title_name, color="0.25", fontsize=20, ha='center', va="top", fontstyle="italic")
    plt.savefig(sapa, dpi=400)
    # plt.show()

# if type==weekend_weekday, Basefolder=all_5minutes, Basefolder2=other types
def figure_by(Basefolder, Basefolder2, Savefolder, type):
    bafo1 = p(Basefolder)
    bafo2 = p(Basefolder2)
    safo = p(Savefolder)
    for piece_csv in bafo1.iterdir():
        nename = piece_csv.stem + "_" + type + ".csv"
        save_name = piece_csv.stem + "_" + type + ".png"
        sapa = safo / save_name
        bapa_1 = piece_csv
        bapa_2 = bafo2 / nename
        figure_weekend_weekday(Basepath=bapa_1,
                               Basepath2=bapa_2,
                               Savepath=sapa,type=type)
        print("done!")
    print("DONE")



# average weekend and weekday
def figure_by_ww(Basefolder, Savefolder):

    bafo = p(Basefolder)
    bafo_weekend = bafo / "weekend_percentage"
    bafo_weekday = bafo / "weekday_percentage"
    safo = p(Savefolder)
    for piece_csv in bafo_weekend.iterdir():
        path_name=piece_csv.name
        r = re.findall('(?!_period)(_weekend)', path_name)

        if r:
            print(path_name)
            ne_na = path_name.split("_")[0]+"_weekday.csv"
            p_weekend = piece_csv
            p_weekday = bafo_weekday / ne_na
            savename = path_name.split("_")[0] + "_weekend_weekday.png"
            sapa = safo / savename
            figure_aver_ww(Basepath_weekend=p_weekend,
                           Basepath_weekday=p_weekday,
                           Savepath=sapa)
        print("done!")
    print("DONE!!")

### July_August
# HK
figure_by_ww(
 Basefolder=
    r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK",
 Savefolder=
    r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\figures")
figure_by(
Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_five_minutes",
Basefolder2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\weekend_percentage",
Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\figures",
type="weekend")

figure_by(
Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_five_minutes",
Basefolder2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\weekday_percentage",
Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\figures",
type="weekday")

figure_by(
Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_five_minutes",
Basefolder2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_percentage",
Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\figures",
type="days")

# region
figure_by_ww(
Basefolder=
    r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region",
Savefolder=
    r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\figures\weekend_weekday")

figure_by(
Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\all_five_minutes",
Basefolder2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\weekend_percentage",
Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\figures\weekend",
type="weekend")

figure_by(
Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\all_five_minutes",
Basefolder2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\weekday_percentage",
Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\figures\weekday",
type="weekday")

# district
figure_by_ww(
Basefolder=
  r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district",
Savefolder=
   r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\figures\weekend_weekday")

figure_by(
Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\all_five_minutes",
Basefolder2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\weekend_percentage",
Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\figures\weekend",
type="weekend")

figure_by(
Basefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\all_five_minutes",
Basefolder2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\weekday_percentage",
Savefolder=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\figures\weekday",
type="weekday")
