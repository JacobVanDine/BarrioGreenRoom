


class Scene:

    def __init__(self, number, cast=None, dancers=None) -> None:
        self.cast = cast
        self.dancers = dancers
        self.members = self.setMembers()
        self.number=number

    def setMembers(self):
        self.members = self.dancers
        filteredCast = filter(lambda x: (x not in self.members), self.cast)
        self.members += filteredCast
    
    def getMembers(self):
        return self.members