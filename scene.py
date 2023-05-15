import numpy as np


class Scene:

    def __init__(self, number, cast=None, dancers=None, dance=None) -> None:
        self.cast = cast
        self.dancers = dancers
        self.members = []
        self.setMembers()
        self.number=number
        self.dance = dance

    def setMembers(self):
        for actor in self.cast:
            self.members.append(actor)
        if(self.dancers is None):
            return
        for dancer in self.dancers:
            if dancer not in self.members:
                self.members.append(dancer)
        
    def display(self):
        returnStr = ""
        if(self.dance is not None): 
            returnStr +=  self.dance+"\n"+'\n'
        if(self.members is None):
            return
        for member in self.members:
            returnStr+= str(member) + '\n'
        return returnStr

    def getMembers(self):
        return self.members