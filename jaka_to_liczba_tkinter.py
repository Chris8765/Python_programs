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
    def __init__(self, master, trial_1):
        """Inicjalizuj ramkę."""
        super(Application_second, self).__init__(master)
        self.grid()
        self.trial = trial_1
        self.create_widgets()
        
        print(self.trial)
        
    def create_widgets(self):
        """
        Utwórz widżety potrzebne do pobrania informacji podanych przez użytkownika
        i wyswietlenia wyników- 1 x etykieta, 1 x ENTRY, 1 x Button,   
        """
        
        #utwórz etykieteę z instrukcją
        Label(self, text ="Masz "+str(self.trial) + " prób, wprowadz liczbę z zakresu od 1 do 10").grid(row = 0, column = 0, columnspan = 2, sticky = W)








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
        
        upper_boud = self.high_range
        lower_boud = self.low_range
        root.destroy()
        root2 = Tk()
        root2.title("Gra: Jaka to liczba? - gra i wyniki")
        app2 = Application_second(root2, trial_num)
        root2.mainloop()


#czesc głowna
root = Tk()
root.title("Gra: Jaka to liczba? - Podawanie zalozen do gry")
app = Application_start(root)
root.mainloop()      







        




      
