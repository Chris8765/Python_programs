# Farma zwierzakóW - ćwiczenie 4
# Zadania:
# - losowy początkowy poziom głodu i nudy;
# - opieka nad całą farmą (czynnosci zbiorowe dla wszystkich zwierzaków - zabawa, karmienie i słuchanie zwierząt);
# - sledzenie stanu zwierząt poprzez listę; 

import random




class zwierzak(object):
    """Wirtualna farma"""
    
    def __init__(self, name):


        hunger = random.randint(1, 10)
        boredom = random.randint(1, 10)
        
        
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
  
    




    def new_name(self):
        print("Zwierzaki nazywają się: " + self.name)
        
        
    def talk(self):
        print("Nazywam się", self.name, "i jestem", self.mood, "teraz.\n")
        self.__pass_time()
    
    def eat(self, food):
        
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self):
        fun = int(input("Ile czasu chcesz poswiecic każdemu swojemu zwierzakowi w skali od 1 -10 [minut]? "))
        print("Hura!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

        
    def __str__(self):  
       
        attributes = "name: " + self.name + "\n" + "hunger: " + str(self.hunger) + "\n" + "boredom: " + str(self.boredom) + "\n"
    
        
        return attributes    







def create_animals():
    amount_of_animals = int(input("ILe zwierząt chcesz posiadać?: "))    
    counter = 0
    list_of_animals= []
    while counter < amount_of_animals:
        
        animal_name = input("Jak nazywa się twoj zwierzak?: ")
        list_of_animals.append(zwierzak(animal_name))
        counter += 1 
        
    

    
    return list_of_animals
    
    
    
    
    
def main():
   
    
    list_of_animals = create_animals()
    print(list_of_animals)
    
    choice = None
    while choice != "0":
        print ("""
        Farma zwierzakow
        0 - zakończ
        1 - Imiona zwierzat
        2 - słuchaj swoich zwierzat
        3 - nakarm swoje zwierzeta
        4 - pobaw się ze swoimi zwierzakami
        5 - poziom głodu i zadowolenia zwierzow
        """)
                   
        choice = input("Wybierasz: ")
        print()
                   
        #wyjdź z pętli
        if choice == "0":
            print("Do widzenia.")
 
       
        #sprawdzenie imion zwierzat:
        elif choice == "1":
            for animal in list_of_animals:
                #print(animal)
                animal.new_name()

              
        #słuchaj swoje zwierzaki
        elif choice == "2":
            for animal in list_of_animals:
                animal.talk()
            
            
        #nakarm swoje zwierzaki
        elif choice == "3":
            food = int(input("Ile żywnosci podajesz każdemu zwierzakowi? "))
            for animal in list_of_animals:
                animal.eat(food)
            
        
            
        #pobaw się ze swoimi zwierzakami
        elif choice == "4":
            for animal in list_of_animals:
                animal.play()
            
        
        #sprawdzenie poziomu głodu zwierzat
        elif choice == "5":
            for animal in list_of_animals:
                print(animal)
          
        
           
        #nieznany wybór
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem")             


                   
main()
input("\n\nAby zakończyć program, nacisnij klawisz Enter.")