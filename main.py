import os
import pandas as pd
import time
import scene

CAST = dict()
DANCES = dict()
NINJAS = []
SCENES = []


def gen_data():
    dance_df = pd.read_excel("./22-23_ALL_PEOPLE_INVOLVED.xlsx", "Dances")
    dance_df = dance_df.dropna().drop()
    cast_df = pd.read_excel("./22-23_ALL_PEOPLE_INVOLVED.xlsx", "Cast")

    for (col_name, col_data) in dance_df.iteritems():
        DANCES[col_name] = col_data




def display():
    return


if __name__ == "__main__":
    gen_data() 
    print(DANCES)

