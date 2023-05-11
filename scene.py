import numpy as np


class Scene:

    def __init__(self, number, cast=None, dancers=None) -> None:
        self.cast = cast
        self.dancers = dancers
        self.members = []
        self.setMembers()
        self.number=number

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
        if(self.members is None):
            return
        for member in self.members:
            returnStr+= member + '\n'
        return returnStr

    def getMembers(self):
        return self.members