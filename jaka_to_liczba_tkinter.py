 
# Gra: "jaka to liczb"
# Podajesz, przedział oraz ilosc prob a komputer losuje i sprawdza
# czy trafiłes, gdy trafisz komputer poda ile potrzebowałes szans,
# lub przegrasz gdy wykorzystasz szanse i nie znajdziesz szukanej liczby.. 

from tkinter import *
import random
trial_num = 0
upper_boud = 0
lower_boud = 0


class Application_second(Frame):
    def __init__(self, master, trial_1, upper_boud, lower_boud):
        """Inicjalizuj ramkę."""
        super(Application_second, self).__init__(master)
        self.grid()
        self.trial = trial_1
        self.upper = upper_boud
        self.lower = lower_boud
        
        new_count = random.randint(int(self.lower), int(self.upper))
        
        self.new_count = new_count

        
        
        self.bttn_clicks = 0 #liczba klikniec przycisku
        
        self.create_widgets()
        
        
        
    def create_widgets(self):
        
        
        
        """
        Utwórz widżety potrzebne do pobrania informacji podanych przez użytkownika
        i wyswietlenia wyników- 1 x etykieta, 1 x ENTRY, 1 x Button,   
        """
        
        #utwórz etykietę z instrukcją
        Label(self, text ="Masz "+str(self.trial) + " prób, wprowadz liczbę z zakresu od " + str(self.lower) +" do "+ str(self.upper) +" :").grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        
        
        #utwórz etykietę i pole znakowe służące do wpisywania ilosci prob
        Label(self, text = "Podaj zgadywana liczbe z założonego zakresu: ").grid(row = 1, column = 0, sticky = W)
        self.your_count = Entry(self)
        self.your_count.grid(row = 1, column = 1, sticky = W)
        
        #utwórz przycisk akceptacji danych
        self.bttn = Button(self)
        self.bttn["text"] = "Kliknij aby sprawdzić wynik, liczba prob: " + str(self.trial)
      
        self.bttn["command"] = self.update_count_and_tell_result
        self.bttn.grid(row = 7, column = 0, sticky = W)
        
        
        
        self.result_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.result_txt.grid(row = 8, column = 0, columnspan = 4)    
        
    def update_count_and_tell_result(self):
        if (int(self.trial) - self.bttn_clicks) > 0:
            """Zwiększ licznik klikniec i wyswietl jego nową wartosc."""
            self.bttn_clicks += 1
            self.bttn["text"] = "Kliknij aby sprawdzić wynik, pozostało ci: " + str(int(self.trial) - self.bttn_clicks) + " prob"
        else:
            self.bttn["text"] = "Mozesz klikac ale i tak przegrales"
         
        result = ""
        
        
        
        user_count = self.your_count.get()
        
        
      
            
        if int(self.trial) > self.bttn_clicks and int(user_count) == self.new_count:
            result = "Trafiłes i wygrales, pozostało Ci: " + str(int(self.trial) - self.bttn_clicks) +" prob."         

        else:
            comment = "Nie trafiłes, pozostalo Ci:" + str(int(self.trial) - self.bttn_clicks) +" prob."  
            if int(user_count) < self.new_count:
                help1 = " Twoja liczba jest za mała."
                result = comment + help1
            elif int(user_count) > self.new_count:
                help1 = " Twoja liczba jest za duża."
                result = comment + help1
            else:
                result = "To już koniec - przegrałes"
            
        if int(self.trial) == self.bttn_clicks and int(user_count) != self.new_count:
            r1 = "To była Twoja ostatnia próba, nie trafiłes.\n"
            r2 = "Szukaną liczbą była:" + str(self.new_count)
            result = r1 +r2  
        
           
            
            
        #pobierz wartosci z interfejsu GUI
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, result)















class Application_start(Frame):
    def __init__(self, master):
        """Inicjalizuj ramkę."""
        super(Application_start, self).__init__(master)
        self.grid()
        self.create_widgets()
       
    
    def create_widgets(self):
        """
        Utwórz widżety potrzebne do pobrania informacji podanych przez użytkownika
        i wyswietlenia wyników- 3 x ENTRY,  
        """
        
        #utwórz etykieteę z instrukcją
        Label(self, text ="Wprowadz dane do gry").grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        #utwórz etykietę i pole znakowe służące do wpisywania ilosci prob
        Label(self, text = "Ilosc prob: ").grid(row = 1, column = 0, sticky = W)
        self.trial = Entry(self)
        self.trial.grid(row = 1, column = 1, sticky = W)

        #utwórz etykietę i pole znakowe służące do górnego zakresu
        Label(self, text = "Podaj górny zakres(liczba dodatnia): ").grid(row = 2, column = 0, sticky = W)
        self.high_range = Entry(self)
        self.high_range.grid(row = 2, column = 1, sticky = W)        

        #utwórz etykietę i pole znakowe służące do dolnego zakresu
        Label(self, text = "Podaj dolny zakres(liczba dodatnia): ").grid(row = 3, column = 0, sticky = W)
        self.low_range = Entry(self)
        self.low_range.grid(row = 3, column = 1, sticky = W)
        
        #utwórz przycisk akceptacji danych
        Button(self,
               text = "Kliknij aby zaakcetowac swoj wybor",
               command = self.save_variables
               ).grid(row = 4, column = 0, sticky = W)

    def save_variables(self):
        global trial_num
        global upper_boud
        global lower_boud

        trial_num = self.trial.get()
        
        upper_boud = self.high_range.get()
        lower_boud = self.low_range.get()
        root.destroy()
        root2 = Tk()
        root2.title("Gra: Jaka to liczba? - gra i wyniki")
        app2 = Application_second(root2, trial_num, upper_boud, lower_boud)
        root2.mainloop()


#czesc głowna
root = Tk()
root.title("Gra: Jaka to liczba? - Podawanie zalozen do gry")
app = Application_start(root)
root.mainloop()      







        





