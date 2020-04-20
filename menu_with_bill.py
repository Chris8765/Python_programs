# "Karta dan z rachunkiem"

from tkinter import *

class Application(Frame):
    """Aplikacja do skladania zamowien wraz z rachunkiem"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    
    def create_widgets(self):
        Label(self, text = "Wybierz pozycje z menu ktore chcesz zamowic [ceny wyrazone w zlotowkach]:"
              ).grid(row = 0, column = 0, sticky = W)
        
        
        
        Label(self, text = "Zupy:"
              ).grid(row = 1, column = 0, sticky = W)
        
        #utworz pole wyboru zupy
        self.zupa_pomidorowa = BooleanVar()
        self.zupa_pomidorowa_cena = 10
        Checkbutton(self, 
                    text = "Zupa pomidorowa \t" + str(self.zupa_pomidorowa_cena), 
                    variable = self.zupa_pomidorowa,
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W )
        
        self.zupa_grochowa = BooleanVar()
        self.zupa_grochowa_cena = 8
        Checkbutton(self, 
                    text = "Zupa grochowa \t\t" + str(self.zupa_grochowa_cena), 
                    variable = self.zupa_grochowa,
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W )
        
        self.zurek = BooleanVar()
        self.zurek_cena = 12
        Checkbutton(self, 
                    text = "Zurek \t\t\t" + str(self.zurek_cena), 
                    variable = self.zurek,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W )
        
        self.rosol = BooleanVar()
        self.rosol_cena = 11
        Checkbutton(self, 
                    text = "Rosol \t\t\t" + str(self.rosol_cena), 
                    variable = self.rosol,
                    command = self.update_text
                    ).grid(row = 5, column = 0, sticky = W )
        
        
        
        
        Label(self, text = "Dania glowne:"
              ).grid(row = 6, column = 0, sticky = W)
        
        
        
        self.pierogi_ruskie = BooleanVar()
        self.pierogi_ruskie_cena = 14
        Checkbutton(self, 
                    text = "Pierogi ruskie \t\t" + str(self.pierogi_ruskie_cena), 
                    variable = self.pierogi_ruskie,
                    command = self.update_text
                    ).grid(row = 7, column = 0, sticky = W )


        self.pierogi_z_miesem = BooleanVar()
        self.pierogi_z_miesem_cena = 25
        Checkbutton(self, 
                    text = "Pierogi z miesem \t\t" + str(self.pierogi_z_miesem_cena), 
                    variable = self.pierogi_z_miesem,
                    command = self.update_text
                    ).grid(row = 8, column = 0, sticky = W )



        self.kotlet_schabowy = BooleanVar()
        self.kotlet_schabowy_cena = 40
        Checkbutton(self, 
                    text = "Kotlet schabowy \t\t" + str(self.kotlet_schabowy_cena), 
                    variable = self.kotlet_schabowy,
                    command = self.update_text
                    ).grid(row = 9, column = 0, sticky = W )
        
        self.ziemniaki = BooleanVar()
        self.ziemniaki_cena = 9
        Checkbutton(self, 
                    text = "Ziemniaki \t\t" + str(self.ziemniaki_cena), 
                    variable = self.ziemniaki,
                    command = self.update_text
                    ).grid(row = 10, column = 0, sticky = W )




        self.ryz = BooleanVar()
        self.ryz_cena = 7
        Checkbutton(self, 
                    text = "Ryz \t\t\t" + str(self.ryz_cena), 
                    variable = self.ryz,
                    command = self.update_text
                    ).grid(row = 11, column = 0, sticky = W )
        
        
        self.surowka = BooleanVar()
        self.surowka_cena = 6
        Checkbutton(self, 
                    text = "Surowka \t\t" + str(self.surowka_cena), 
                    variable = self.surowka,
                    command = self.update_text
                    ).grid(row = 12, column = 0, sticky = W )        



        Label(self, text = "Napoje:"
              ).grid(row = 1, column = 2, sticky = W)

        
        self.herbata = BooleanVar()
        self.herbata_cena = 4
        Checkbutton(self, 
                    text = "Herbata \t\t\t" + str(self.herbata_cena), 
                    variable = self.herbata,
                    command = self.update_text
                    ).grid(row = 2, column = 2, sticky = W )  
        

        self.sok_pomaranczowy = BooleanVar()
        self.sok_pomaranczowy_cena = 5
        Checkbutton(self, 
                    text = "Sok pomaranczowy \t" + str(self.sok_pomaranczowy_cena), 
                    variable = self.sok_pomaranczowy,
                    command = self.update_text
                    ).grid(row = 3, column = 2, sticky = W )  
        
        Label(self, text = "Alkohole:"
              ).grid(row = 4, column = 2, sticky = W)

        self.piwo = BooleanVar()
        self.piwo_cena = 8
        Checkbutton(self, 
                    text = "Piwo \t\t\t" + str(self.piwo_cena), 
                    variable = self.piwo,
                    command = self.update_text
                    ).grid(row = 5, column = 2, sticky = W )  

        self.wodka = BooleanVar()
        self.wodka_cena = 12
        Checkbutton(self, 
                    text = "Wodka \t\t\t" + str(self.wodka_cena), 
                    variable = self.wodka,
                    command = self.update_text
                    ).grid(row = 6, column = 2, sticky = W )  




        
        
        
        #utwórz pole tekstowe do wyswietlenia wynikow
        self.results_txt = Text(self, width = 40 , height = 2, wrap = WORD)
        self.results_txt.grid(row=20, column = 2, columnspan = 3)
        
    def update_text(self):
        "Zaktualizuj pole tekstowe i wyswietl rachunek"
        bill = 0
        if self.zupa_pomidorowa.get():
            bill += self.zupa_pomidorowa_cena
        if self.zupa_grochowa.get():
            bill += self.zupa_grochowa_cena
        if self.zurek.get():
            bill += self.zurek_cena
        if self.rosol.get():
            bill += self.rosol_cena
        if self.pierogi_ruskie.get():
            bill += self.pierogi_ruskie_cena
        if self.pierogi_z_miesem.get():
            bill += self.pierogi_z_miesem_cena
        if self.kotlet_schabowy.get():
            bill += self.kotlet_schabowy_cena    
        if self.ziemniaki.get():
            bill += self.ziemniaki_cena             
        if self.ryz.get():
            bill += self.ryz_cena       
        if self.surowka.get():
            bill += self.surowka_cena
        if self.herbata.get():
            bill += self.herbata_cena         
        if self.sok_pomaranczowy.get():
            bill += self.sok_pomaranczowy_cena    
        if self.piwo.get():
            bill += self.piwo_cena
        if self.wodka.get():
            bill += self.wodka_cena



        
        result = "Twój rachunek wynosi " + str(bill) + " zlotych"
        
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, result)
            
            
            



#czesc głowna
root = Tk()
root.title("Restauracja: \"U Pazdziocha\": Zloz zamowienie")
app = Application(root)
root.mainloop()      