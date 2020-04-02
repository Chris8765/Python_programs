#first program with object oriented programming

class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name):
        print("Urodził się nowy zwierzak!")
        self.name = name
        
    def __str__(self):
        rep = "Objekt klasy Critter\n"
        rep += "name: " + self.name + "\n"
        return rep
    
    def talk(self):
        print("Czesc! Jestem", self.name, "\n")

# częsc główna

crit1 = Critter("Reksio")
crit1.talk()

crit2 = Critter("Pucek")
crit2.talk()
     
print("Wyswietl obiekt crit1:")
print (crit1)

print("Bezposrednie wyswitlenie wartosci atrybutu crit1.name:")
print(crit1.name)

input("\n\nAby zakończyć program, nacinij klawisz Enter.")   
