import pandas as pd
import numpy as np
from pathlib import Path as p, Path


def impute_linear(Basepath, savepath):
    bapa = p(Basepath)
    for piece in bapa.iterdir():
        sa_name = piece.name
        df = pd.read_csv(piece, header=0, index_col=[0,1])
        ne_df = df.interpolate(method="linear", axis=1)
        sapa = p(savepath)/sa_name
        # sapa = p(r"E:\2022dissertation\July_clustering\cluster_csv")/ sa_name
        ne_df.to_csv(sapa)

def check_nan(Basepath):
    bapa = p(Basepath)

    for piece in bapa.iterdir():
        ne_na = piece.stem
        df = pd.read_csv(piece, header=0, index_col=[0,1])
        # print(df.isnull().any())
        arr = df.to_numpy(dtype="float64")
        Z = np.isnan(arr)
        if True in Z:
            print(ne_na, "Nan True")
        else:
            print(ne_na, "done")


# print("HK_check: ")
# check_nan(Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\before_interpo\HK_all_five")

# print("region_check: ")
# check_nan(Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\before_interpo\region_all_five")

# print("district_check: ")
# check_nan(Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\before_interpo\district_all_five")


impute_linear(
    Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\before_interpo\HK_all_five",
    savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_five_minutes")
impute_linear(
    Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\before_interpo\region_all_five",
    savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\all_five_minutes")
impute_linear(
    Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\before_interpo\district_all_five",
    savepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\all_five_minutes")

# Sample
# print("HK_check: ")
# check_nan(
# Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\HK\all_five_minutes")

# print("region_check: ")
# check_nan(
# Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_region\all_five_minutes")

# print("district_check: ")
# check_nan(
# Basepath=r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\useful_percentage_data\per_district\all_five_minutes")
