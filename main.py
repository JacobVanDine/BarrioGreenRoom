import os
import pandas as pd
import numpy as np
import time
from scene import Scene

CAST = dict()
DANCES = dict()
NINJAS = []
SCENES = []
NUM_SCENES=14


def gen_data():
    dance_df = pd.read_excel("./22-23_ALL_PEOPLE_INVOLVED.xlsx", "Dances")
    dance_df = dance_df.dropna()
    cast_df = pd.read_excel("./22-23_ALL_PEOPLE_INVOLVED.xlsx", "Cast")

    dancer_arr = dance_df.T.to_numpy()
    dances_arr = dance_df.columns.to_numpy()
    role_list = cast_df["Role"].tolist()
    actor_list = cast_df["Actor"].tolist()

    for elem in range(len(dances_arr)):
        DANCES[dances_arr[elem]] = dancer_arr[elem]
    DANCES['COMMERICIALS'] = []
    
    for elem in range(len(role_list)):
        CAST[role_list[elem]] = actor_list[elem]
        
def gen_scenes():
    for scene in range(NUM_SCENES):
        if(scene==1): 
            SCENES.append(Scene(scene, ['hana'], DANCES.get('Traditional Tinikling')))
        elif(scene==2):
            SCENES.append(Scene(scene, {}, DANCES.get('Binasuan')))
        elif(scene==3):
            SCENES.append(Scene(scene, {}, DANCES.get('Co-Ed Modern')))
        elif(scene==4):
            SCENES.append(Scene(scene, {}, DANCES.get('Pandanggo')))
        elif(scene==5):
          SCENES.append(Scene(scene, {}, DANCES.get('Magla')))
        elif(scene==6):
            SCENES.append(Scene(scene, {}, DANCES.get('Singkil')))
            SCENES.append(Scene(scene, {}, DANCES.get('COMMERCIALS')))
        elif(scene==7):
            SCENES.append(Scene(scene, {}, DANCES.get('Couples Modern')))
        elif(scene==8):
            SCENES.append(Scene(scene, {}, DANCES.get('Bangko')))
        elif(scene==9):
            SCENES.append(Scene(scene, {}, DANCES.get('Boys Modern')))
        elif(scene==10):
          SCENES.append(Scene(scene, {}, DANCES.get('Pagapir')))
        elif(scene==11):
            SCENES.append(Scene(scene, {}, DANCES.get('Girls Modern')))
        elif(scene==12):
            SCENES.append(Scene(scene, {}))
        elif(scene==13):
            SCENES.append(Scene(scene, {}, DANCES.get('Alcamfor')))
        elif(scene==14):
            SCENES.append(Scene(scene, {}, DANCES.get('Modern Tinikling')))

if __name__ == "__main__":
    gen_data() 
    print(DANCES)
    print(CAST)

