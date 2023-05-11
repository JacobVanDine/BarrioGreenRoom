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
        print(dancer_arr)
    DANCES['COMMERICIALS'] = []
    
    for elem in range(len(role_list)):
        CAST[role_list[elem]] = actor_list[elem]


def castToActor(arr):
    for role in arr:
        arr[arr.index(role)] = CAST.get(role)
    return arr
    
def gen_scenes():
    for scene in range(NUM_SCENES+1):
        if(scene==1): 
            SCENES.append(Scene(scene, castToActor(['hana', 'lola', 'Child #1','Child #2','emerlinda', 'sampaguita', 'benilde', 'bendito', 'agapito', 'tita baby', 'tito boy', 'althea', 'alejandro' ]), DANCES.get('Traditional Tinikling')))
        elif(scene==2):
            SCENES.append(Scene(scene, castToActor(['hana', 'tita baby', 'tito boy', 'althea', 'alejandro', 'lola', 'bendito', 'sampaguita', 'benilde' ]), DANCES.get('Binasuan')))
        elif(scene==3):
            SCENES.append(Scene(scene, castToActor(['hana','emerlinda', 'sampaguita', 'benilde', 'bendito', 'agapito', 'tita baby', 'tito boy', 'althea', 'alejandro' , 'lola' ]), DANCES.get('Co-Ed Modern')))
        elif(scene==4):
            SCENES.append(Scene(scene, castToActor(['hana', 'lola', 'sampaguita', 'althea', 'emerlinda', 'bendito', 'agapito']), DANCES.get('Pandanggo Sa Ilaw')))
        elif(scene==5):
          SCENES.append(Scene(scene, castToActor(['hana','emerlinda', 'sampaguita', 'benilde', 'bendito', 'agapito', 'tita baby', 'tito boy', 'althea', 'alejandro' , 'lola' ]), DANCES.get('Magla')))
        elif(scene==6):
            SCENES.append(Scene(scene, castToActor(['hana', 'bendito', 'tita baby', 'andres' ]), DANCES.get('Singkil')))
            SCENES.append(Scene(scene, [], DANCES.get('COMMERCIALS')))
        elif(scene==7):
            SCENES.append(Scene(scene, castToActor(['hana', 'lola', 'benilde', 'bendito', 'tita baby', 'tito boy', 'tita althea', 'tito alejandro']), DANCES.get('Couples Modern')))
        elif(scene==8):
            SCENES.append(Scene(scene, castToActor(['hana', 'lola', 'sampaguita', 'benilde', 'emerlinda', 'bendito', 'agapito', 'tita baby', 'tito boy', 'althea', 'alejandro', 'andres']), DANCES.get('Bangko')))
        elif(scene==9):
            SCENES.append(Scene(scene, castToActor(['hana', 'tito aldo', 'bendito', 'agapito', 'tito boy']), DANCES.get('Boys Modern')))
        elif(scene==10):
          SCENES.append(Scene(scene, castToActor(['hana', 'lola', 'sampaguita', 'tito aldo', 'emerlinda', 'agapito', 'tita baby', 'alejandro']), DANCES.get('Pagapir')))
        elif(scene==11):
            SCENES.append(Scene(scene, castToActor(['hana', 'lola', 'sampaguita', 'emerlinda', 'agapito', 'tita baby', 'althea']), DANCES.get('Girls Modern')))
        elif(scene==12):
            SCENES.append(Scene(scene, castToActor(['hana', 'lola', 'sampaguita', 'benilde','emerlinda', 'bendito', 'agapito', 'tita baby', 'tito boy', 'althea', 'alejandro'])))
        elif(scene==13):
            SCENES.append(Scene(scene, castToActor(['hana', 'lola', 'sampaguita', 'tito aldo', 'bendito', 'tita baby', 'tito boy', 'andres']), DANCES.get('Alcamfor')))
        elif(scene==14):
            SCENES.append(Scene(scene, castToActor(['lola', 'bendito', 'tita baby', 'tito boy']), DANCES.get('Modern Tinikling')))

def display_all():
    for sceneNum in range(len(SCENES)-1):
        print("CURRNET SCENE: SCENE "+ str(SCENES[sceneNum].number)+ '\n'+ SCENES[sceneNum].display() )
        print("ON DECK: SCENE " + str(SCENES[sceneNum+1].number)+ '\n'+  SCENES[sceneNum+1].display() )
    print("FINAL SCENE: SCENE "+ str(SCENES[-1].number)+ '\n'+ SCENES[-1].display() )

def barrio():
    cmd = input("Green Room Commands: \nEnter key for Next Scene\nType exit to exit the program.")
    scenes_index=0
    while(cmd!='exit'):
        if(scenes_index==14):
            print("FINAL SCENE: SCENE "+ str(SCENES[-1].number)+ '\n'+ SCENES[-1].display() )
            cmd="exit"
        else:
            print("CURRNET SCENE: SCENE "+ str(SCENES[scenes_index].number)+ '\n'+ SCENES[scenes_index].display() )
            print("ON DECK: SCENE " + str(SCENES[scenes_index+1].number)+ '\n'+  SCENES[scenes_index+1].display() )
            scenes_index+=1
            cmd = input("Green Room Commands: \nEnter key for Next Scene\nType exit to exit the program.")



if __name__ == "__main__":
    gen_data() 
    gen_scenes()
    #display_all()
    #barrio()
    
        

