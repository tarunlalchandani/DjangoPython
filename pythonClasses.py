class Incarnations:
    def __init__(self,name, yuga,enemy, devotee, weapons):
        self.name = name
        self.yuga = yuga
        self.enemy = enemy
        self.time = yuga
        self.devotee = devotee
        self.weapons = weapons
    def printDetails(self):
        print("Krsna in {} incarnated as {} and he killed {} and protected {} and he used the weapons {}".format(self.yuga,self.name,self.enemy,self.devotee,self.weapons))

Rama = Incarnations("Rama","TretaYuga","Ravana","Sita",["bow","Arrow","Sword","Sudarshan Cakra"])
Rama.printDetails()
