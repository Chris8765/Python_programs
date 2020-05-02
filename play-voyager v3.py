#Gra przygodowa wykorzystująca obiekty, gdzie gracz może podróżować,
#pomiędzy różnymi wzajemnie połączonymi miejscami

class Voyager(object):
    def __init__(self, name, response, location_name = "Dom"):
        
        self.name = name
        self.location_name = location_name
        self.response = response
        

        
    def __str__(self):  

        
        atribute = "name" + self.name + "location_name" + self.location_name
     
        return atribute

class Place(object):
    def __init__(self, name, greeting, curiosity_list):
        self.name = name
        self.greeting = greeting
        self.curiosity_list = curiosity_list


    def __str__(self):  
       
        atribute = "name: " + self.name + "greeting:" + self.greeting+ "curiosity1:" + self.curiosity_list 
  
        return atribute
    



#main
def main():
    
    
    name = input("Hej, jak się nazywasz? ")
    response = None
    voyager_name = Voyager(name, response)

    
    
    
    print("\n\nPodróż\n")
    print("Czesc " + name + ", rozpoczynamy podroz po Polsce. Miłej zabawy.")

    
    capital = Place("Warszawa", "Jestes w Warszawie\n", 
                    ["Ciekawostka 1: jest stolica od 18 marca 1596\n",
                    "W Warszawie znajduje się najwęższy budynek świata czyli Dom Kereta.\n"])
    
    city1 = Place("Lublin", "Jestes w Lublinie\n",
                  ["Miasto otrzymało prawo składu w 1392. Prawo to nakazywało przejeżdżającym przez miasto kupcom, wystawić swoje towary. Dzięki temu przywilejowy Lublin zaczął się bardzo prężnie i szybko rozwijać.\n",
                  "W roku 1630 wybuchła w Lublinie epidemia dżumy pochłaniając aż 5 tysięcy ofiar.\n"])
    
    city2 = Place("Poznan", "Jestes w Poznaniu\n",
                  ["Ciekawostka 1: W Poznaniu można zjesc szneke z glancem - drożdzówkę z lukrem, pyry z gzikiem - ziemniaki z twarogiem, przejechać się bimbą - tramwajem lub założyć laczki - pantofle",
                  "W północnej części Poznania znajduje się rezerwat Morasko, w którym odkryto największy meteoryt w Polsce ważący 261 kg..\n"])
    
    city3 = Place("Rzeszow", "Jestes w Rzeszowie\n",
                  ["Ciekawostka 1: Rzeszów założono jako prywatne miasto szlacheckie. Lokacja miasta miała miejsce w 1353 roku.\n",
                  "W Bziance(obecnie w granicach Rzeszowa) w 1851 r. znaleziono czaszkę mamuta mającą ok 14 tys. lat.\n"])
    
    home = Place("Dom", "Jestes w domu\n", ["brak ciekawostek","brak ciekawostek"])
    
    dict_of_places ={"Warszawa": capital, "Lublin": city1, "Poznan": city2, "Rzeszow" : city3}
    

    
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
        dict_of_places ={"Warszawa": capital, "Lublin": city1, "Poznan": city2, "Rzeszow" : city3, "Dom": home}
                   
        #wyjdź z pętli
        if choice == "0":
            print("Do widzenia " + str(voyager_name.name))                     
        #sprawdz gdzie jestem
        elif choice == "1":
            
            voyager_name.location_name
            print(voyager_name.location_name)
        
        #ciekawostki dotyczace miejsca w którym jestes
        elif choice == "2":
            print(dict_of_places[voyager_name.location_name].curiosity_list[0])
            
                
            
        #ciekawostki dotyczace miejsca w którym jestes
        elif choice == "3":
            print(dict_of_places[voyager_name.location_name].curiosity_list[1])
            
            
        #wybór miasta do którego chcesz jechać
        elif choice == "4":
            print("Miejsca gdzie możesz jechać:")
            
            
            del dict_of_places[voyager_name.location_name]
            #print(element_of_dictionary)
            for places in dict_of_places:
                print(places)
            
            """Wybierz miasto."""
            response = None
            while response not in dict_of_places:
                response = str(input("Wpisz wybrane miasto: "))
                print(response)
                voyager_name.location_name = response
                
                
            print(dict_of_places[voyager_name.location_name].greeting)
 

           
        #nieznany wybór
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem")  


main()
input("\n\nAby zakończyć program nacisnij Enter.")