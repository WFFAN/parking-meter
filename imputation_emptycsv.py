import pandas as pd
import numpy as np
import re
from pathlib import Path as p
import copy



def imputation(bapa1, bapa2, savpa):
    bapa1 = p(bapa1)
    bapa2 = p(bapa2)
    df1 = pd.read_csv(bapa1, header=0, index_col=0)
    df2 = pd.read_csv(bapa2, header=0, index_col=0)
    df_ne = pd.DataFrame() # columns=["ParkingSpaceId", "OccupancyStatus"]
    ne_dict = {}
    # zip1 = list(zip(df1["ParkingSpaceId"],df1["OccupancyStatus"]))
    # zip2 = list(zip(df2["ParkingSpaceId"],df2["OccupancyStatus"]))
    list1 = df1.index.tolist()
    list2 = df2.index.tolist()
    for i in list1:
        if i in list2:
            value1 = df1.loc[i]["OccupancyStatus"]
            value2 = df2.loc[i]["OccupancyStatus"]
            if value1 == value2:
                ne_dict[i] = value1
            else:
                # print(i,"1", value1)
                # print(i,"2", value2)
                ne_dict[i] = np.random.choice([value1, value2], 1, p=[0.5, 0.5])
                # print (ne_dict[i])
    # print(ne_dict)
    df_ne = pd.DataFrame(ne_dict, index=["OccupancyStatus"])
    df_new = df_ne.T
    df_new.index.name = "ParkingSpaceId"
    df_new.reset_index(inplace=True)
    print(df_new.head())
    df_new.to_csv(savpa, index=None)


# imputation(
# bapa1 = r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\imputation_csv\20210913_084501\084001.csv",
# bapa2 = r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\imputation_csv\20210913_084501\085001.csv",
# savpa = r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\imputation_csv\20210913_084501\084501.csv",
# )




imputation(
bapa1 = r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\imputation_csv\20210919_083001\082501.csv",
bapa2 = r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\imputation_csv\20210919_083001\083501.csv",
savpa = r"E:\2022dissertation\July_Sept\July_Sept_2021_useful\imputation_csv\20210919_083001\083001.csv",
)
