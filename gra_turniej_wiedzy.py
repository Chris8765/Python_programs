#Turniej wiedzy
#Gra sprawdza wiedzę ogólną, odczytując dane ze zwykłego pliku tekstowego


import sys

def p_name():
    
    player_name = input ("Jak się nazywasz?  ")
    return player_name

def open_file(file_name,mode):
    """Otwórz plik."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print ("Nie można otworzyć pliku", file_name, "Program zostanie zakończony.\n", e)
        input("\n\n Aby zakończyć program, nacisnij klawisz Enter.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    "Zwróc kolejny wiersz pliku kwiz po sformatowaniu go."
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Zwróć kolejny blok danych z pliku kwiz."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    
    explanation = next_line(the_file)
    
    points = next_line(the_file)
    
    return category, question, answers, correct, explanation, points

def welcome(title):
    """Przywitaj gracza."""
    print("\t\t Witaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")
    
def save_winner_and_score(player_name, score_last):
    
    text_file = open("winner_and_score.txt", "a+")
    text_file.write(player_name + " ---- " +str(score_last)+"\n")
    text_file.close()

def main():
    
    player_name = p_name()
    points_sum = 0
    trivia_file = open_file("kwiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    
    #pobierz pierwszy blok
    category, question, answers, correct, explanation, points = next_block(trivia_file)
    while category:
        #zadaj pytanie
        print(category)
        print(question)
        for i in range(4):
            print("\t", i+1, "-", answers[i])
        #uzyskaj odpowiedz
        answer = input("Jaka jest Twoja odpowiedź?: ")
       
        #sprawdź odpowiedź
        if answer == correct:
            print("\nOdpowiedź prawidłowa!", end=" ")
            print("Punkty za tą poprawną odpowiedź to:", points)
            score += int(points)
            points_sum += int(points)
            print("Twoje wszystkie punkty zdobyte do tej pory to: ", score)
        else:
            print("\nOdpowiedz niepoprawna.", end=" ")
            print(explanation)
            print("Twoje wszystkie punkty zdobyte do tej pory to:", score, "\n\n")
            points_sum += int(points)
        #pobierz kolejny blok
        category, question, answers, correct, explanation, points = next_block(trivia_file)
        
    trivia_file.close()
    
    print("To było ostatnie pytanie!")
    print(player_name ,"twój końcowy wynik wynosi", score , "na:", points_sum)
    score_last = score 
    save_winner_and_score(player_name, score_last)
main() 
input("\n\nAby zakończyć program, nacisnij klawisz Enter.")  