#Opiekun zwierzaka
#Wirtualny pupil, którym należy się opiekować

class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęsliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "poddenerowany"
        else:
            m = "wsciekły"
        return m
  
        
        
        
    def talk(self):
        print("Nazywam się", self.name, "i jestem", self.mood, "teraz.\n")
        self.__pass_time()
    def eat(self, food = 0):
        food = int(input("Ile pożywienia chcesz dać zwierzakowi? (wybierz wartosc z zakresu 1 - 10) "))
        print("Mniam, mniam. Dziękuję.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, fun = 0):
        fun = int(input("Ile czasu chcesz poswiecic swojemu zwierzakowi w skali od 1 -10 [minut]? "))
        print("Hura!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
    def volume(self):
        print("Obecny poziom głodu (jeżeli 0 to max najedzony, a > 15 wsciekły) to: ", self.hunger)
        print("Obecny poziom szczęscia (jeżeli 0 to  max szczęsliwy, a ) to: ", self.boredom)
        
    def __str__(self):  
       
        attributes = ("name: " + self.name + "\n" + "hunger: " + str(self.hunger) + "\n" + "boredom: " + str(self.boredom) + "\n")
    
        
        return attributes

        
        
def main():
    crit_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
    crit = Critter(crit_name)
        
    choice = None
    while choice != "0":
        print ("""
        Opiekun zwierzaka
        0 - zakończ
        1 - słuchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw się ze swoim zwierzakiem
        4 - poziom głodu i zadowolenia zwierzaka
        5 - mechanizm \"tylnych drzwi\" wg. zadania 3 - Atrybuty obiektu klasy Critter (naszego zwierzaka)
        """)
                   
        choice = input("Wybierasz: ")
        print()
                   
        #wyjdź z pętli
        if choice == "0":
            print("Do widzenia.")
                       
        #słuchaj swojego zwierzaka
        elif choice == "1":
            crit.talk()
            
        #nakarm swojego zwierzaka
        elif choice == "2":
            crit.eat()
            
        #pobaw się ze swoim zwierzakiem
        elif choice == "3":
            crit.play()
        
        #sprawdzenie poziomu głodu zwierzaka
        elif choice == "4":
            crit.volume()
        
        #mechanizm "tylnych drzwi"
        elif choice == "5":
            print(crit)
           
        #nieznany wybór
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem")             


                   
main()
input("\n\nAby zakończyć program, nacisnij klawisz Enter.")