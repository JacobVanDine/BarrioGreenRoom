import os
import pandas as pd
import time
import member
import dance
import scene

CAST = {}
DANCES = {}
NINJAS = []
SCENES = []


def get_data():
    dance_df = pd.read_excel("./test/dance.xlsx")
    cast_df = pd.read_excel("./test/cast.xlsx")
    dance_df.head()
    cast_df.head()

def display():
    return


if __name__ == "__main__":
    get_data() 

