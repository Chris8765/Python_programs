 
# Gra: "jaka to liczb"
# Podajesz, przedział oraz ilosc prob a komputer losuje i sprawdza
# czy trafiłes, gdy trafisz komputer poda ile potrzebowałes szans,
# lub przegrasz gdy wykorzystasz szanse i nie znajdziesz szukanej liczby.. 

from tkinter import *
import random
amount_of_people = 0



class Application_second(Frame):
    def __init__(self, master, amount_of_people):
        """Inicjalizuj ramkę."""
        super(Application_second, self).__init__(master)
        self.grid()
        self.amount_of_people = amount_of_people
        

        
        
        self.bttn_clicks = 0 #liczba klikniec przycisku
        
        self.create_widgets()
        
        
        
    def create_widgets(self):
        
        
        
        """
        Utwórz widżety potrzebne do pobrania informacji podanych przez użytkownika
        i wyswietlenia wyników- 1 x etykieta,  1 x Button,   
        """
        
        #utwórz etykietę z instrukcją
        Label(self, text ="Max liczba osob w sklepie wynosi: " + self.amount_of_people, font=("Arial",24,"italic"),

                 foreground="yellow", background="blue").grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        
        
        
        self.counter_txt = Text(self, font=("Arial",24,"italic"), width = 5, height = 1, wrap = WORD)
        self.counter_txt.grid(row = 1, column = 0, columnspan = 4)
        
    
        
        #utwórz przycisk dodawania
        self.bttn1 = Button(self, bg ="red", fg = "white", font=("Arial",24,"italic"))
        self.bttn1["text"] = "+"
        self.bttn1["command"] = self.update_count_plus
        self.bttn1.grid(row = 4, column = 4, sticky = W)
        
        
        #utwórz przycisk odejmowania
        self.bttn2 = Button(self, bg = "green", fg = "white", font=("Arial",24,"italic"))
        self.bttn2["text"] = "-"
      
        self.bttn2["command"] = self.update_count_minus
        self.bttn2.grid(row = 4, column = 0, sticky = W)
        
        
        self.result_txt = Text(self, width = 30, height = 10, wrap = WORD)
        self.result_txt.grid(row = 8, column = 0, columnspan = 4)    
        
    def update_count_plus(self):
        self.bttn_clicks += 1
        counter = str(self.bttn_clicks)
        self.counter_txt.delete(0.0, END)
        self.counter_txt.insert(0.0, counter)
        
        
        if int(self.bttn_clicks) >= int(self.amount_of_people):
            
            result = "Maksymalna liczba osob w sklepie zostala przekroczona. Nie wpuszczaj ludzi!! "
        else:
            result = "Można wpuszczac ludzi!"
            
        
        #pobierz wartosci z interfejsu GUI
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, result)
        
        
    
    def update_count_minus(self):
        self.bttn_clicks -= 1
        counter = str(self.bttn_clicks)
        self.counter_txt.delete(0.0, END)
        self.counter_txt.insert(0.0, counter)
        
        
        if int(self.bttn_clicks) >= int(self.amount_of_people):
            
            result = "Maksymalna liczba osob w sklepie zostala przekroczona. Nie wpuszczaj ludzi!! "
        else:
            result = "Można wpuszczac ludzi!"
           

        
           
            
            
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
        i wyswietlenia wyników- 1 x ENTRY,  
        """
        
        #utwórz etykieteę z instrukcją
        Label(self, text ="Wprowadz maxymalna liczbe osob w sklepie:").grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        #utwórz etykietę i pole znakowe służące do wpisywania ilosci prob
        Label(self, text = "Max ilosc osob w sklepie: ").grid(row = 1, column = 0, sticky = W)
        self.trial = Entry(self)
        self.trial.grid(row = 1, column = 1, sticky = W)


        
        #utwórz przycisk akceptacji danych
        Button(self,
               text = "Kliknij aby zaakcetowac swoj wybor",
               command = self.save_variables
               ).grid(row = 2, column = 0, sticky = W)

    def save_variables(self):
        global amount_of_people


        amount_of_people = self.trial.get()
        

        root.destroy()
        root2 = Tk()
        root2.title("Wprowadzenie maksymalnej liczby osob w sklepie")
        app2 = Application_second(root2, amount_of_people)
        root2.mainloop()


#czesc głowna
root = Tk()
root.title("Sprawdzanie stanu osob w sklepie")
app = Application_start(root)
root.mainloop()      







        





