import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path as p
import re


# this script can generate dictionary between 'ParkingSpaceId' and its information
# (etc. 'Region', 'District', 'SubDistrict', 'Street', 'Latitude', 'Longitude')
#  also get list of useless parkingmeter space id

# the first one can have one information key name
def info_meter_dict(dict_path, info_name):
    # path = p(r"D:\POLYU_dissertation\parking_meter_0412_0425\meters_region\meter_spacedf.csv")
    path = p(dict_path)
    base_df = pd.read_csv(path, header=0, index_col=0)
    base_df['Latitude'] = base_df['Latitude'].astype(np.float64)
    base_df['Longitude'] = base_df['Longitude'].astype(np.float64)
    # the first 'for' circle obtains mapping dictionary
    grouped_info = base_df.groupby(['ParkingSpaceId', info_name])
    list_dict = []
    for (spaceid, infodetail), group in grouped_info:
        list_dict.append((spaceid, infodetail))
    mapping_dict = dict(list_dict)
    return mapping_dict
    # print(mapping_dict)


# the second one can get various types of information
# (except 'Latitude' and 'Longitude')
def info_type_list(dict_path, info_name):
    path = p(dict_path)
    base_df = pd.read_csv(path, header=0, index_col=0)
    base_df['Latitude'] = base_df['Latitude'].astype(np.float64)
    base_df['Longitude'] = base_df['Longitude'].astype(np.float64)
    info_type_list = []
    if info_name != 'Latitude' or 'Longitude':
        grouped_info_type = base_df.groupby(info_name)
        for type, group in grouped_info_type:
            info_type_list.append(type)
    print(info_type_list)
    return info_type_list


# the third one can input two information key name
def two_info_meter_dict(dict_path, info_name1, info_name2):
    # this dictionary is useful when we need to get two information of paringspaceid
    # especially, latitude and longtitue are needed
    path = p(dict_path)
    base_df = pd.read_csv(path, header=0, index_col=0)
    base_df['Latitude'] = base_df['Latitude'].astype(np.float64)
    base_df['Longitude'] = base_df['Longitude'].astype(np.float64)
    # the first 'for' circle obtains mapping dictionary
    grouped_info = base_df.groupby(['ParkingSpaceId', info_name1, info_name2])
    list_dict = []
    for (spaceid, infodetail1, infodetail2), group in grouped_info:
        list_dict.append((spaceid, (infodetail1, infodetail2)))
    mapping_dict = dict(list_dict)
    return mapping_dict


# the fourth one can generate a list of useless parking spaceid
def useless_spaceid(path_name):
    path = p(path_name)
    base_df = pd.read_csv(path, header=0, index_col=0)
    base_df['Latitude'] = base_df['Latitude'].astype(np.float64)
    base_df['Longitude'] = base_df['Longitude'].astype(np.float64)
    group_useless = base_df.groupby(['Latitude', 'ParkingSpaceId'])
    useless_list = []
    for (name, infoid), group in group_useless:
        if int(name) > 30:
            useless_list.append(infoid)
    return useless_list


# this function use for the new obtained dictionary
# because some original information give us wrong name
# such as incorrectely typed the District as 'Sha Ting' rather than 'Sha Tin'
def ori_yes_no(basepath, areaname, want_identify_area='Southern'):
    path = p(basepath)
    base_df = pd.read_csv(path, header=0, index_col=0)
    base_df['Latitude'] = base_df['Latitude'].astype(np.float64)
    base_df['Longitude'] = base_df['Longitude'].astype(np.float64)
    grouped_area = base_df.groupby(areaname)
    area_list = []
    df_output = []
    for name, group in grouped_area:
        area_list.append(name)
        print(name)
        print(group.shape)
        if name == want_identify_area:
            df_output = group
    print(area_list)
    print(len(area_list))
    print(df_output)

# ori_yes_no(basepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\meters_region\parkingspaces_210504_dict.csv",
#            areaname=r"District", want_identify_area='Shatin')
## ori_yes_no(basepath=r"D:\POLYU_dissertation\parking_meter_0412_0425\meters_region\parkingspaces_210425_dict.csv",
##                     areaname=r"District", want_identify_area='Tai Po Hui')
## df = useless_spaceid(path_name=r"D:\POLYU_dissertation\parking_meter_0412_0425\meters_region\ "
##                                r"meter_spacedf_220119_dict.csv")
## print(df)

# ori_yes_no(basepath=r"D:\POLYU_dissertation\July_2021_useful\parkingspaces_210801_dict.csv",
#            areaname=r"District", want_identify_area='Prince')
# ori_yes_no(basepath=r"D:\POLYU_dissertation\July_2021_useful\parkingspaces_211005_dict.csv",
#            areaname=r"Region", want_identify_area='Hong Kong')

# ori_yes_no(basepath=r"D:\POLYU_dissertation\July_2021_useful\parkingspaces_211206_dict.csv",
#            areaname=r"District", want_identify_area='Yu Tsim Mong')
