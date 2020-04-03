#Turniej wiedzy
#Gra sprawdza wiedzę ogólną, odczytując dane ze zwykłego pliku tekstowego


import sys
import operator

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
    winner_list = []
    entry = [player_name, score_last]
    
    with open("winner_and_score.txt", "r+") as text_file_1:
        for line in text_file_1:
            print(line)
            entry_old = line.split(",")
            print(entry_old)
            player_name_old = entry_old[0]
            score_old = int(entry_old[1])
            winner_list.append([player_name_old, score_old])
            


        winner_list.append(entry)
        winner_list = sorted(winner_list, key=operator.itemgetter(1), reverse = True)
        del winner_list [5:]
        
        print(winner_list)
    
    with open("winner_and_score.txt", "w") as text_file_2: 
        pass
    with open("winner_and_score.txt", "w") as text_file_3: 
        for position in winner_list:
            if len(position[0]) < 5:
                value_1 = (str(position[0]) + ", \t\t"+ str(position[1])+"\n")
            else:
                value_1 = (str(position[0]) + ", \t"+ str(position[1])+"\n")
            text_file_3.write(value_1)
        
 

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