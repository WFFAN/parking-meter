import pandas as pd
from pathlib import Path as p
import numpy as np
import concat_per_time

# this script can base parent path with some day folders
# to concat per folder's csv_doc inside
# column name will be sorted and data will be numerical
def apply_time_day(Base_parent, Save_parent):
    bapa = p(Base_parent)
    sapa = p(Save_parent)
    for mid_path in bapa.iterdir():
        sa_fol_name = mid_path.name
        concat_per_time.time_day(Basepath=mid_path,
                                 Savepath=sapa)
    print("DONE!!!")

## apply_time_day(Base_parent=r"D:\POLYU_dissertation\parking_meter_0412_0425\day_consider_status",
##               Save_parent=r"D:\POLYU_dissertation\parking_meter_0412_0425\concat_day_costa")

