#Gra przygodowa wykorzystująca obiekty, gdzie gracz może podróżować,
#pomiędzy różnymi wzajemnie połączonymi miejscami

class Voyager(object):
    def __init__(self, name, response, location_name = "Dom"):
        
        self.name = name
        self.location_name = location_name
        self.response = response
        
    
    def location(self, response):
        
        if response != None:
            self.location_name = response
        else: 
            
            return(self.location_name)

        
    def __str__(self):  

        
        atribute = "name" + self.name + "location_name" + self.location_name
     
        return atribute

class Place(object):
    def __init__(self, name, greeting, curiosity_1, curiosity_2):
        self.name = name
        self.greeting = greeting
        self.curiosity_1 = curiosity_1
        self.curiosity_2 = curiosity_2

    def __str__(self):  
       
        atribute = "name: " + self.name + "greeting:" + self.greeting+ "curiosity1:" + self.curiosity_1 + "curiosity2:" + self.curiosity_2
  
        return atribute
    



#main
def main():
    
    
    name = input("Hej, jak się nazywasz? ")
    response = None
    voyager_name = Voyager(name, response)

    
    
    
    print("\n\nPodróż\n")
    print("Czesc " + name + ", rozpoczynamy podroz po Polsce. Miłej zabawy.")

    
    capital = Place("Warszawa", "Jestes w Warszawie\n", 
                    "Ciekawostka 1: jest stolica od 18 marca 1596\n",
                    "W Warszawie znajduje się najwęższy budynek świata czyli Dom Kereta.\n")
    
    city1 = Place("Lublin", "Jestes w Lublinie\n",
                  "Miasto otrzymało prawo składu w 1392. Prawo to nakazywało przejeżdżającym przez miasto kupcom, wystawić swoje towary. Dzięki temu przywilejowy Lublin zaczął się bardzo prężnie i szybko rozwijać.\n",
                  "W roku 1630 wybuchła w Lublinie epidemia dżumy pochłaniając aż 5 tysięcy ofiar.\n")
    
    city2 = Place("Poznan", "Jestes w Poznaniu\n",
                  "Ciekawostka 1: W Poznaniu można zjesc szneke z glancem - drożdzówkę z lukrem, pyry z gzikiem - ziemniaki z twarogiem, przejechać się bimbą - tramwajem lub założyć laczki - pantofle",
                  "W północnej części Poznania znajduje się rezerwat Morasko, w którym odkryto największy meteoryt w Polsce ważący 261 kg..\n")
    
    city3 = Place("Rzeszow", "Jestes w Rzeszowie\n",
                  "Ciekawostka 1: Rzeszów założono jako prywatne miasto szlacheckie. Lokacja miasta miała miejsce w 1353 roku.\n",
                  "W Bziance(obecnie w granicach Rzeszowa) w 1851 r. znaleziono czaszkę mamuta mającą ok 14 tys. lat.\n")
    
    home = Place("Dom", "Jestes w domu\n", "brak ciekawostek","brak ciekawostek")
    
    list_of_places =[capital.name, city1.name, city2.name, city3.name]
    

    
    choice = None
    while choice != "0":
        print ("""
        Podróż
        0 - zakończ
        1 - sprawdz gdzie jestem
        2 - 1 ciekawostka dotyczace miejsca w ktorym jestes
        3 - 2 ciekawostka dotyczace miejsca w ktorym jestes
        4 - wybór miejsca do którego chcesz jechać
        """)
                   
        choice = input("Wybierasz: ")
        list_of_places = [capital.name, city1.name, city2.name, city3.name, home.name]
                   
        #wyjdź z pętli
        if choice == "0":
            print("Do widzenia " + str(voyager_name.name))                     
        #sprawdz gdzie jestem
        elif choice == "1":
            
            voyager_name.location(response = None)
            print(voyager_name.location(response = None))
        
        #ciekawostki dotyczace miejsca w którym jestes
        elif choice == "2":
            if voyager_name.location(response = None) == "Warszawa":
                print(capital.curiosity_1)
            elif voyager_name.location(response = None) == "Lublin":
                print(city1.curiosity_1)
            elif voyager_name.location(response = None) == "Poznan":
                print(city2.curiosity_1)
            elif voyager_name.location(response = None) == "Rzeszow":
                print(city3.curiosity_1)
            else:
                print(home.curiosity_1)
                
            
        #ciekawostki dotyczace miejsca w którym jestes
        elif choice == "3":
            if voyager_name.location(response = None) == "Warszawa":
                print(capital.curiosity_2)
            elif voyager_name.location(response = None) == "Lublin":
                print(city1.curiosity_2)
            elif voyager_name.location(response = None) == "Poznan":
                print(city2.curiosity_2)
            elif voyager_name.location(response = None) == "Rzeszow":
                print(city3.curiosity_2)
            else:
                print(home.curiosity_2)
            
            
        #wybór miasta do którego chcesz jechać
        elif choice == "4":
            print("Miejsca gdzie możesz jechać:")
            list_of_places.remove(voyager_name.location(response = None))
            #print(list_of_places)
            for places in list_of_places:
                print(places)
            
            """Wybierz miasto."""
            response = None
            while response not in list_of_places:
                response = str(input("Wpisz wybrane miasto: "))
                print(response)
                voyager_name.location(response)
                
            if voyager_name.location(response = None) == "Warszawa":
                print(capital.greeting)
            elif voyager_name.location(response = None) == "Lublin":
                print(city1.greeting)
            elif voyager_name.location(response = None) == "Poznan":
                print(city2.greeting)
            elif voyager_name.location(response = None) == "Rzeszow":
                print(city3.greeting)
            else:
                print(home.greeting)
 

           
        #nieznany wybór
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem")  


main()
input("\n\nAby zakończyć program nacisnij Enter.")