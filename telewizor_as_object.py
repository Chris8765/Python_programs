# Program "Telewizor" z użyciem programowania obiektowego.
# Użytkownik będzie miał możliwosc zmiany kanału i poziomu głosnosci.

class Telewizor(object):
    """Twój telewizor"""
    def __init__(self, name, channel_number = 1, sound_level = 0):
        self.name = name
        self.channel_number = channel_number
        self.sound_level = sound_level
    
    def brand(self):
        print("Marka twojego telewizora to: ", self.name, "\n")
    
    def state(self):
        print("Atualny numer kanału to: ", self.channel_number)
        print("Atualny poziom głosnosci to: ", self.sound_level)
    
    def channel(self):
        temp_channel_number = int(input("Jaki kanał wybierasz? (wybierz wartosc z zakresu 1 - 100) "))
        if temp_channel_number < 1 or temp_channel_number > 100:
            print("Zmiana kanału nie powiodła się, wybrano numer po za zakresem.")
        else:
            self.channel_number = temp_channel_number
            print("Dokonano zmiany kanału.")
    
    def volume(self):
        temp_sound_level = int(input("Jaki poziom głosnosci wybierasz? (wybierz wartosc z zakresu 0 - 30) "))
        if temp_sound_level < 0 or temp_sound_level > 30:
            print("Zmiana poziomu głosnosci nie powiodla się, wybrano numer po za zakresem.")
        else:
            self.sound_level = temp_sound_level
            print("Dokonano zmiany poziomu głosnosci.")
        



def main():
    telewizor_name = input("Podaj markę twojego telewizora? ")
    tele = Telewizor(telewizor_name)
    
    choice = None
    while choice != "0":
        print ("""
        Twój telewizor
        0 - zakończ
        1 - Marka Twojego telewizora
        2 - Aktualny numer kanału i poziom głosnosci.
        3 - Zmiana numeru kananłu <1-100>
        4 - Zmiana poziomu głosnosci <0-30>
        """)
                   
        choice = input("Wybierasz: ")
        print()
                   
        #wyjdź z pętli
        if choice == "0":
            print("Do widzenia.")
                       
        #Wyswietla markę twojego telewizora
        elif choice == "1":
            tele.brand()
        
        #sprawdzam numer kanału i poziom głosnosci
        elif choice == "2":
            tele.state()
            
        #Zmiana numeru kananłu <1-100>
        elif choice == "3":
            tele.channel()
            
        #Zmiana poziomu głosnosci <0-30>
        elif choice == "4":
            tele.volume()
                           
        #nieznany wybór
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem")             
 
        
main()
input("\n\nAby zakończyć program, nacisnij klawisz Enter.")