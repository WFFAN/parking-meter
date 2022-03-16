import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates
import re
from pathlib import Path as p, Path
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter
from datetime import datetime
from datetime import time

## This script consists of two functions, weekday+HK+region/district and weekend+HK+region/district
## each function generate one big figure
## Basepath should be district /region parent path
## Basepath2 should be HK_weekday.csv or HK_weekend.csv
## Savepath should be folder path
## type is region / district
def figure_weekday(Basepath, Basepath2, Savepath, type):
    bapa = p(Basepath)
    bapa2 = p(Basepath2)

    sa_n = "HK_weekday_" + type + ".png"
    sapa = p(Savepath) / sa_n
    df_2 = pd.read_csv(bapa2, index_col=0, header=0)
    # time_x_ori = np.array(df_2.columns)
    time_x_ori = list(df_2.columns)
    time_x_ori[0:12] = ['000', '005', '010', '015', '020', '025',
                       '030', '035', '040', '045', '050', '055']
    time_x_ori[0:120] = ['0'+ x for x in time_x_ori[0:120]]
    print(time_x_ori)
    # convert numerical value to date_string (Hour, Minutes)
    time_x = [datetime.strptime(d, '%H%M') for d in time_x_ori]
    # time_x = time_x.astype(np.int64)
    Aver_weekday = np.array(df_2.loc["weekday"].copy())
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111)

    # set x y major_tick_locator
    # ax.xaxis.set_major_locator(MultipleLocator(100))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%#H'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax.yaxis.set_major_locator(MultipleLocator(0.05))


    # set x y minor_tick_locator
    # ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H%M'))
    #ax.xaxis.set_minor_locator(mdates.MinuteLocator())
    # ax.xaxis.set_minor_locator(AutoMinorLocator(6))
    # ax.yaxis.set_minor_locator(AutoMinorLocator(5))

    # def major_x(x, pos):
    #     if not (x * 0.01) % 1:
    #         return int(x * 0.01)
    #     return ""

    # ax.xaxis.set_major_formatter(FuncFormatter(major_x))

    # change the appearance of ticks and tick labels
    ax.tick_params(which='major', length=8, width=1.0, colors="0.25")
    ax.tick_params(which='minor', length=3, width=0.5, labelsize=10, labelcolor="0.25")
    ax.set_ylim(0, 1)
    #ax.set_xlim(0, 24)
    ax.set_xlim([time_x[0], time_x[-1]])
    ax.set_xlabel("time (hr)", color="0.25")
    ax.set_ylabel("Occupied Parking Meters Percentage", color="0.25")
    # draw the whole HK average line
    plt.plot(time_x, Aver_weekday, ls="-", lw=1.8, label="HK", color="#1f78b4")# "#fdb462"
    i_fp = 0
    color_list = ["#4daf4a", "#984ea3", "#a65628","#e41a1c", "#999999", "#4292c6"]

    if type == "district":
        # color_list = ["#b2df8a", "#fb9a99","#fdbf6f"]
        for piece_csv in bapa.iterdir():
            path_name = piece_csv.name
            # find path root which contents 'areaname_weekday'
            # r = re.findall('[^(_period)](_weekday)', path_name)
            r = re.findall('(?!_period)(_weekday)', path_name)
            if r:
                read_path = piece_csv
                df_1 = pd.read_csv(read_path, index_col=0, header=0)
                l_1 = np.array(df_1.loc["weekday"].copy())
                label_name = path_name.split("_")
                if label_name[0] == "Hong Kong":
                    label_name[0] = "Hong Kong Island"
                if i_fp + 1 <= len(color_list):
                    plt.plot(time_x, l_1, ls="-", lw=1.2, label=label_name[0], color=color_list[i_fp])
                elif i_fp + 1 <= 2*len(color_list):
                    i_ff = i_fp - len(color_list)
                    plt.plot(time_x, l_1, ls="--", lw=1.2, label=label_name[0], color=color_list[i_ff])
                else:
                    i_ff = i_fp - 2*len(color_list)
                    plt.plot(time_x, l_1, ls="-.", lw=1.2, label=label_name[0], color=color_list[i_ff])
                i_fp += 1
    if type == "region":
        ax.grid(ls="--", lw=1, color="#e0e0e0")  # , color="#e0e0e0")# , color="#FFFFFF")
        for piece_csv in bapa.iterdir():
            path_name = piece_csv.name
            # find path root which contents 'areaname_weekday'
            # r = re.findall('[^(_period)](_weekday)', path_name)
            r = re.findall('(?!_period)(_weekday)', path_name)
            if r:
                read_path = piece_csv
                df_1 = pd.read_csv(read_path, index_col=0, header=0)
                l_1 = np.array(df_1.loc["weekday"].copy())
                label_name = path_name.split("_")
                if label_name[0] == "Hong Kong":
                    label_name[0] = "Hong Kong Island"
                if i_fp == 0:
                    plt.plot(time_x, l_1, ls=":", lw=1.8, label=label_name[0], color=color_list[i_fp])
                elif i_fp == 1:
                    plt.plot(time_x, l_1, ls="--", lw=1.8, label=label_name[0], color=color_list[i_fp])
                elif i_fp == 2:
                    plt.plot(time_x, l_1, ls="-.", lw=1.8, label=label_name[0], color=color_list[i_fp])
                i_fp += 1

    # bbox_to_anchor=(0.01, -0.2, 0.42, 0.05)
    plt.legend(
        loc="upper left", bbox_to_anchor=(0.55, 0.22, 0.42, 0.05), ncol=3, title=type, shadow=False,
        handleheight=0.5, handlelength=1.50, fontsize=8, title_fontsize=8, labelspacing=0.25)
    title_name ="HK Occupied Parking Meters Percentage\n(Weekday)"
    plt.title(label=title_name, fontsize=15)
    plt.savefig(sapa, dpi=400)
    # plt.show()

# figure_weekday(
# Basepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\per_district\other_types",
# Basepath2=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\other_types\HK_weekday.csv",
# Savepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\figures",
# type="district")

def figure_weekend(Basepath, Basepath2, Savepath, type):
    bapa = p(Basepath)
    bapa2 = p(Basepath2)
    sa_n = "HK_weekend_" + type + ".png"
    sapa = p(Savepath) / sa_n
    df_2 = pd.read_csv(bapa2, index_col=0, header=0)
    # time_x_ori = np.array(df_2.columns)
    time_x_ori = list(df_2.columns)
    time_x_ori[0:12] = ['000', '005', '010', '015', '020', '025',
                        '030', '035', '040', '045', '050', '055']
    time_x_ori[0:120] = ['0' + x for x in time_x_ori[0:120]]
    print(time_x_ori)
    # convert numerical value to date_string (Hour, Minutes)
    time_x = [datetime.strptime(d, '%H%M') for d in time_x_ori]
    # time_x = time_x.astype(np.int64)
    Aver_weekend = np.array(df_2.loc["weekend"].copy())
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%#H'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax.yaxis.set_major_locator(MultipleLocator(0.05))


    # change the appearance of ticks and tick labels
    ax.tick_params(which='major', length=8, width=1.0, colors="0.25")
    ax.tick_params(which='minor', length=3, width=0.5, labelsize=10, labelcolor="0.25")
    ax.set_ylim(0, 1)
    # ax.set_xlim(0, 24)
    ax.set_xlim([time_x[0], time_x[-1]])
    ax.set_xlabel("time (hr)", color="0.25")
    ax.set_ylabel("Occupied Parking Meters Percentage", color="0.25")
    # draw the whole HK average line
    plt.plot(time_x, Aver_weekend, ls="-", lw=1.8, label="HK", color="#1f78b4")# "#fdb462"
    i_fp = 0

    color_list = ["#4daf4a", "#984ea3", "#a65628","#e41a1c", "#999999", "#4292c6"]
    if type == "district":
        for piece_csv in bapa.iterdir():
            path_name = piece_csv.name
            # find path root which contents 'areaname_weekday'
            # r = re.findall('[^(_period)](_weekend)', path_name)
            r = re.findall('(?!_period)(_weekend)', path_name)
            if r:
                read_path = piece_csv
                df_1 = pd.read_csv(read_path, index_col=0, header=0)
                l_1 = np.array(df_1.loc["weekend"].copy())
                label_name = path_name.split("_")
                if label_name[0] == "Hong Kong":
                    label_name[0]="Hong Kong Island"
                if i_fp +1 <= len(color_list):
                    plt.plot(time_x, l_1, ls="-", lw=1.2, label=label_name[0], color=color_list[i_fp])
                elif i_fp +1 <= 2*len(color_list):
                    i_ff = i_fp - len(color_list)
                    plt.plot(time_x, l_1, ls="--", lw=1.2, label=label_name[0], color=color_list[i_ff])
                else:
                    i_ff = i_fp - 2*len(color_list)
                    plt.plot(time_x, l_1, ls="-.", lw=1.2, label=label_name[0], color=color_list[i_ff])
                i_fp += 1
    if type == "region":
        ax.grid(ls="--", lw=1, color="#e0e0e0")  # , color="#e0e0e0")# , color="#FFFFFF")
        for piece_csv in bapa.iterdir():
            path_name = piece_csv.name
            # find path root which contents 'areaname_weekday'
            # r = re.findall('[^(_period)](_weekend)', path_name)
            r = re.findall('(?!_period)(_weekend)', path_name)
            if r:
                read_path = piece_csv
                df_1 = pd.read_csv(read_path, index_col=0, header=0)
                l_1 = np.array(df_1.loc["weekend"].copy())
                label_name = path_name.split("_")
                if label_name[0] == "Hong Kong":
                    label_name[0]="Hong Kong Island"
                if i_fp == 0:
                    plt.plot(time_x, l_1, ls=":", lw=1.8, label=label_name[0], color=color_list[i_fp])
                elif i_fp == 1:
                    plt.plot(time_x, l_1, ls="--", lw=1.8, label=label_name[0], color=color_list[i_fp])
                elif i_fp == 2:
                    plt.plot(time_x, l_1, ls="-.", lw=1.8, label=label_name[0], color=color_list[i_fp])
                i_fp += 1

    # bbox_to_anchor=(0.01, -0.2, 0.42, 0.05)
    plt.legend(
        loc="upper left", bbox_to_anchor=(0.55, 0.22, 0.42, 0.05), ncol=3, title=type, shadow=False,
        handleheight=0.5, handlelength=1.35, fontsize=8, title_fontsize=8, labelspacing=0.25)
    title_name ="HK Occupied Parking Meters Percentage\n(Weekend)"
    plt.title(label=title_name, fontsize=15)
    plt.savefig(sapa, dpi=400)
    # plt.show()
figure_weekend(
Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\weekend_percentage",
Basepath2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\weekend_percentage"
                 r"\HK_weekend.csv",
Savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\figures",
type="district")

figure_weekday(
Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\weekday_percentage",
Basepath2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\weekday_percentage"
                 r"\HK_weekday.csv",
Savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\figures",
type="district")

figure_weekend(
   Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\weekend_percentage",
   Basepath2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\weekend_percentage"
                 r"\HK_weekend.csv",
   Savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\figures",
   type="region")

figure_weekday(
   Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\weekday_percentage",
   Basepath2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\weekday_percentage"
                 r"\HK_weekday.csv",
   Savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\figures",
   type="region")
