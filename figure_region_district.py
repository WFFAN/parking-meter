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
from numpy import ndarray


# Basepath = districts% folder
# Basepath2 = region% folder
# This function can generate four subplots,
# represent New territories*2, Kowloon and Hong Kong Island respectively
# type should be weekend / weekday
def figure_HK(Basepath, Basepath2, Savepath, type):
    bapa = p(Basepath)
    bapa2 = p(Basepath2)
    sa_n = "HK_region_district_"+type + ".png"
    sapa = p(Savepath) / sa_n

    # districts in New Territories
    # northern? north
    nt_list = ("Islands", "Kwai Tsing", "Northern",
                "Tai Po", "Tsuen Wan","Tuen Mun", "Yuen Long", "Sha Tin", "Sai Kung" )
    # districts in Kowloon
    kln_list = ("Kowloon City", "Kwun Tong", "Sham Shui Po", "Wong Tai Sin", "Yau Tsim Mong")

    # districts in Hong Kong Island
    hk_list = ("Central & Western", "Eastern", "Southern", "Wan Chai")

    df_2 = pd.read_csv(
        r"D:\POLYU_dissertation\parking_meter_0412_0425\useful_percentage_data\HK\other_types\HK_weekday.csv",
        index_col=0, header=0)

    time_x_ori = list(df_2.columns)
    time_x_ori[0:12] = ['000', '005', '010', '015', '020', '025',
                        '030', '035', '040', '045', '050', '055']
    time_x_ori[0:120] = ['0' + x for x in time_x_ori[0:120]]
    print(time_x_ori)

    # convert numerical value to date_string (Hour, Minutes)
    time_x = [datetime.strptime(d, '%H%M') for d in time_x_ori]

    # Aver_weekday = np.array(df_2.loc["weekday"].copy())

    fig, axes = plt.subplots(1, 3, figsize=(35, 10))
    axes = axes.flatten()
    for n, ax in enumerate(axes):
        # set x y major_tick_locator
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%#H'))
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))
        ax.yaxis.set_major_locator(MultipleLocator(0.05))
        # change the appearance of ticks and tick labels
        ax.tick_params(which='major', length=5, width=0, labelsize=18, colors="#005C80",labelcolor="#005C80")# width=1
        ax.tick_params(which='minor', length=2, width=0, labelsize=18, colors="#005C80",labelcolor="#005C80")# width=0.4
        ## for x_n in ['top', "bottom", "left", "right"]:
        ##     ax.spines[x_n].set_color('none')
        for x_n in ['top', "bottom", "left", "right"]:
            ax.spines[x_n].set_color('#005C80')  # none
        ax.grid(ls="--", lw=1, color="#98CDD5")  # , color="#e0e0e0")# , color="#FFFFFF")
        ax.set_ylim(0, 1)
        ax.set_xlim([time_x[0], time_x[-1]])
        ## ax.grid(ls="-", lw=2, color="#FFFFFF")
        ## ax.set(facecolor="#EDF3FF") ##FFE7D3, #CCD2FF #E3E6FF
        ax.set_xlabel("time (hr)", color="#005C80",fontsize=18, loc="right", fontstyle='italic')
        if n == 0:
            ax.set_ylabel("Occupied Parking Meters Percentage", color="#005C80",fontsize=18,fontstyle='italic')

    #color_list = ["#4daf4a", "#984ea3", "#a65628", "#e41a1c", "#999999", "#4292c6"]
    ##D36D94
    #color_list = ["#FF6E8B", "#009D65", "#9465EB", "#D55B00", "#92A9F1", "#BFA6A2",
    #              "#FFED18", "#A7AABD", "#D4A418"]
    color_list= ["#468015", "#0056B0", "#623A9B", "#FF85A7", "#C08B8B",
                 "#94AE7A", "#00C5FF", "#C493FF", "#474554"]


    for piece in bapa2.iterdir():
        pa_na = piece.name
        if type =="weekday":
            doc = re.findall('(?!_period)(_weekday)', pa_na)
        elif type =="weekend":
            doc = re.findall('(?!_period)(_weekend)', pa_na)
        if doc:
            df_region = pd.read_csv(piece, index_col=0, header=0)
            l_region = np.array(df_region.loc[type].copy())
            label_region = pa_na.split("_")[0]
            if label_region == "New Territories":
                axes[0].plot(time_x, l_region, ls="-", lw=3.2, label=label_region, color="#C34A36")
                # axes[1].plot(time_x, l_region, ls="-", lw=3.2, label=label_region, color="#C34A36")
            elif label_region == "Kowloon":
                axes[1].plot(time_x, l_region, ls="-", lw=3.2, label=label_region, color="#C34A36")
            elif label_region == "Hong Kong":
                axes[2].plot(time_x, l_region, ls="-", lw=3.2, label="Hong Kong Island", color="#C34A36")
    i_l = [-1, -1, -1]
    for piece_csv in bapa.iterdir():
        path_name = piece_csv.name
        # find path root which contents 'areaname_weekday'
        if type =="weekday":
            r = re.findall('(?!_period)(_weekday)', path_name)
        elif type =="weekend":
            r = re.findall('(?!_period)(_weekend)', path_name)
        if r:
            df_1 = pd.read_csv(piece_csv, index_col=0, header=0)
            l_1 = np.array(df_1.loc[type].copy())
            label_name = path_name.split("_")[0]
            # print(label_name)


            if label_name in nt_list:
                i_l[0] += 1
                i = i_l[0]
                axe=axes[0]

            elif label_name in kln_list:
                i_l[1] += 1
                i = i_l[1]
                axe=axes[1]

            elif label_name in hk_list:
                i_l[2] += 1
                i = i_l[2]
                axe=axes[2]
            # print(i_l)
            # ax1.plot(time_x, l_1, ls="-", lw=0.8, label=label_name[0], color=color_list[i_f
            if i <= 4:
                axe.plot(time_x, l_1, ls="-", lw=1.6, label=label_name, color=color_list[i])
            else:
                axe.plot(time_x, l_1, ls="--", lw=1.6, label=label_name, color=color_list[i])
            axe.legend(
                loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3, frameon=False, handleheight=0.3,
                handlelength=3, fontsize=15, title_fontsize=8, labelspacing=0.25,borderpad=0.3, columnspacing=1)

    # bbox_to_anchor=(0.01, -0.2, 0.42, 0.05)
    title_name = "HK Occupied Parking Meters Percentage ("+ type.title()+")"
    #fig.suptitle(t=title_name, fontsize=12, ha="center", va="bottom", fontstyle='italic')
    fig.text(0.5, 0.01, title_name,  color="#005C80", fontsize=23, ha='center', va="bottom", fontstyle="italic")
    plt.subplots_adjust(wspace=0.1, hspace=0.3)
    plt.savefig(sapa, dpi=400)
    plt.tight_layout()
    # plt.show()

figure_HK(
  Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\weekend_percentage",
  Basepath2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\weekend_percentage",
  Savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\figures",
  type="weekend")

figure_HK(
  Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\weekday_percentage",
  Basepath2=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\weekday_percentage",
  Savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\figures",
  type="weekday")

