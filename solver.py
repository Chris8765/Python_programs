class Solver(object):

    def process(self, line: str) -> str:

        global card_strength, straight_superiority, card_strength_reverse

        # card_strength = {card : strength}
        card_strength = {"2" : "1.0", "3":"2.0", "4":"3.0", "5":"4.0", "6":"5.0", "7":"6.0",
            "8":"7.0","9":"8.0", "T":"9.0", "J":"10.0", "Q":"11.0", "K":"12.0", "A":"13.0"}

        straight_superiority = "A23456789TJQKA"

        card_strength_reverse = {"1.0" : "2", "2.0":"3", "3.0":"4", "4.0":"5", "5.0":"6", "6.0":"7",
                 "7.0":"8","8.0":"9", "9.0":"T", "10.0":"J", "11.0":"Q", "12.0":"K", "13.0" :"A"}






        #identifying the type of game:
        line_list = line.split(" ")
        if line_list[0] == "texas-holdem":
            return self.texas_holdem(line_list[1:])
        elif line_list[0] == "omaha-holdem":
            return self.omaha_holdem(line_list[1:])
        elif line_list[0] == "five-card-draw":
            return self.five_card_draw(line_list[1:])



#"*********************************************************************************************************************************"

#"*********************************************************************************************************************************"

#"*********************************************************************************************************************************"


    def texas_holdem(self, line_list):

        dic_hand_with_rank = {}
        values_to_control_only_rank_th ={}

        players_cards_th =[]
        table_cards_th = line_list[0]
        table_cards_list_th = [table_cards_th[0:2],table_cards_th[2:4], table_cards_th[4:6], table_cards_th[6:8], table_cards_th[8:10]]
        cards_from_the_table_and_cards_from_the_hand = table_cards_list_th
        for position in line_list[1:]:
            players_cards_th = (position[0:2],position[2:4])

            # board cards first, then hand cards
            cards_from_the_table_and_cards_from_the_hand.append(players_cards_th[0])
            cards_from_the_table_and_cards_from_the_hand.append(players_cards_th[1])


            max_value, rank_1 = self.hand_evaluation_th(cards_from_the_table_and_cards_from_the_hand)
            values_to_sort = (max_value, rank_1)

            values_to_control_only_rank_th[position] = rank_1

            dic_hand_with_rank[position] = values_to_sort


            sort_dict = dict(sorted(dic_hand_with_rank.items(), key=lambda item: item[1]))


            cards_from_the_table_and_cards_from_the_hand.remove(players_cards_th[0])
            cards_from_the_table_and_cards_from_the_hand.remove(players_cards_th[1])


        note, string_the_same_values, cards_to_remove = self.the_same_values_in_list_th(values_to_control_only_rank_th)   #assign the three values that the function returns:
                                                                                                                            #note, string_the_same_values, cards_to_remove


        list_of_sort_hands = sort_dict.keys()




        solution = ""

        for hand in list_of_sort_hands:
            solution += hand + " "
        final_solution = solution[:-1]


        if note == True:            #No hand of cards of exactly the same strength

            return final_solution

        else:
            #there are hands of exactly the same strength:
            final_solution_with_equal = final_solution.replace(cards_to_remove[0], "temp_value")        #momentary introduction of a substitute value

            for hands in cards_to_remove:                                                               #removing unnecessary card layouts
                final_solution_with_equal = final_solution_with_equal.replace(hands + " ", "")
                final_solution_with_equal = final_solution_with_equal.replace(hands, "")


            final_solution_with_equal = final_solution_with_equal.replace("temp_value", string_the_same_values)     #to introduce a text string with a set of card hands of the same strength to solve



            return(final_solution_with_equal)


    #Determine if the set of cards contains cards of exactly the same strength:
    def the_same_values_in_list_th(self, values_to_control_only_rank_th):

        values_dic = {}
        string_the_same_values =""

        for value in values_to_control_only_rank_th:

            if values_to_control_only_rank_th[value] in values_dic:

                values_dic[values_to_control_only_rank_th[value]] += 1 #counter that sums up the hands of cards of the same value
            else:
                values_dic.update({values_to_control_only_rank_th[value]:1})



        if max(values_dic.values()) == 1:
            return True, None, None # no hand of cards of the same strength
        else:

            for value in values_dic.values():
                if value != 1:
                    card_value = [k for k, v in values_dic.items() if v > 1]                                #defining a set of cards of the same strength
                    card_name = [k for k, v in values_to_control_only_rank_th.items() if v == card_value[0]]

                    card_name.sort()
                    cards_to_remove = card_name                                 #Card sets that will have to be removed, because they will be replaced by a text string of card sets with the same strength
                    for card in card_name:
                        string_the_same_values += card +"="                     #Create a text string containing card layouts with the same strength along with the "=" sign

                    return(False, string_the_same_values[:-1], cards_to_remove)










    # Finding the highest card layout and assigning the appropriate rank to it:
    def hand_evaluation_th(self, cards_from_the_table_and_cards_from_the_hand):
        hand_ranking = {"1.0" : "2", "2.0":"3", "3.0":"4", "4.0":"5", "5.0":"6", "6.0":"7",
                    "7.0":"8","8.0":"9", "9.0":"T", "10.0":"J", "11.0":"Q", "12.0":"K",
                    "13.0" :"A", "14.0":"One_pair", "15.0":"Two_pair", "16.0":"Three_of_a_kind",
                    "17.0":"Straight", "18.0":"Flush", "19.0":"Full_house", "20.0":"Four_of_kind", "21.0":"Straight_flush"}





        rank_1 = self.high_card_th(cards_from_the_table_and_cards_from_the_hand)



        if self.flush_check_th(cards_from_the_table_and_cards_from_the_hand) != 0:

            rank_2 = 18.0 + self.flush_check_th(cards_from_the_table_and_cards_from_the_hand)

        else:
            rank_2 = 0


        if self.straight_th(cards_from_the_table_and_cards_from_the_hand) != 0:

            rank_3 = 17 + self.straight_th(cards_from_the_table_and_cards_from_the_hand)

        else:
            rank_3 = 0



        if self.flush_check_th(cards_from_the_table_and_cards_from_the_hand)== self.straight_th(cards_from_the_table_and_cards_from_the_hand) and rank_2 !=0:

            rank_4 = 21.0 + self.flush_check_th(cards_from_the_table_and_cards_from_the_hand)

        else:
            rank_4 = 0

        rank_5 = self.kit_th(cards_from_the_table_and_cards_from_the_hand)



        max_value = max(rank_1, rank_2, rank_3, rank_4, rank_5)


        return max_value, rank_1


    def high_card_th(self, cards_from_the_table_and_cards_from_the_hand):

        counter = 0
        rank = 0
        max_number_of_card = 0


        cards =("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")


        for card in cards:
            for card_th in cards_from_the_table_and_cards_from_the_hand:
                if card == card_th[0] and max_number_of_card <=4:
                    counter += 2
                    decimal_place_th = 10 ** counter
                    card_strength.get(card)
                    rank += (float(card_strength.get(card)) / decimal_place_th)

                    max_number_of_card += 1



        return rank


    def straight_th(self, cards_from_the_table_and_cards_from_the_hand):

        list_straight_control_th =[]

        for card in cards_from_the_table_and_cards_from_the_hand:
            list_straight_control_th.append(card[0])

        list_strength_th = []

        #assigning strength to individual cards:
        for card in list_straight_control_th:
            strength_th = card_strength.get(card)
            list_strength_th.append(float(strength_th))

        list_strength_th = list(set(list_strength_th))

        list_strength_th.sort()     #sorting cards by their strength

        sort_card_string_th =""

        #returning the sorted cards:
        for position in list_strength_th:
            sort_card_string_th += card_strength_reverse.get(str(position))







        #checking if the sorted layout is really straight:
        if straight_superiority.find(sort_card_string_th[0:5]) != -1:
            return self.high_card_th(sort_card_string_th[0:5])

        elif straight_superiority.find(sort_card_string_th[1:6]) != -1:
            return self.high_card_th(sort_card_string_th[1:6])

        elif straight_superiority.find(sort_card_string_th[2:7]) != -1:
            return self.high_card_th(sort_card_string_th[2:7])


        elif "A" in sort_card_string_th:
            second_string_th = "A" + sort_card_string_th[:-1]

            if straight_superiority.find(second_string_th) != -1:

                return self.high_card_th(second_string_th[0:5])
            else:
                return 0



        else:
            return 0











    def flush_check_th(self, cards_from_the_table_and_cards_from_the_hand):

        colors_dic_th = {}

        for card in cards_from_the_table_and_cards_from_the_hand:
            if card[1] in colors_dic_th:
                colors_dic_th[card[1]] += 1

            else:
                colors_dic_th.update({card[1]:1})




        list_of_five_cards_the_same_color = []


        for suit, value in colors_dic_th.items():
            if value >= 5:

                for card in cards_from_the_table_and_cards_from_the_hand:
                    if card[1] == suit:
                        list_of_five_cards_the_same_color.append(card)

                card_value = self.high_card_th(list_of_five_cards_the_same_color)



                return card_value
            else:
                continue
        return 0



    #determining the repetition (number of cards) that have the same strength:
    def repetition_of_cards(self, cards_from_the_table_and_cards_from_the_hand):
        cards_dic_th = {}
        for card in cards_from_the_table_and_cards_from_the_hand:
            if card[0] in cards_dic_th:
                cards_dic_th[card[0]] += 1
            else:
                cards_dic_th.update({card[0]:1})

        return cards_dic_th



    # The function "kit" checks the occurrence of:
    # - one_pair, two-pair, three_of_a_kind, full_house, four_of_kind
    # along with their strength for possible comparison

    def kit_th(self, cards_from_the_table_and_cards_from_the_hand):
        cards_dic_th = self.repetition_of_cards(cards_from_the_table_and_cards_from_the_hand)

        list_of_rep = list(cards_dic_th.values())

        rank = 0
        one_pair = False
        three_of_a_kind = False


        if list_of_rep.count(2) ==1: #checking the existence of one_pair
            one_pair = True

            name_of_pair_card_th = [k for k, v in cards_dic_th.items() if v == 2]
            value_of_pair_card_th = float(card_strength[name_of_pair_card_th[0]])

            rank = 14.0 + 0.01 * value_of_pair_card_th


        if list_of_rep.count(2) == 2:   #checking the existence of two_pair
            two_pairs = True

            names_of_two_pair_card_th = [k for k, v in cards_dic_th.items() if v == 2]

            names_of_two_pair_card_th.sort(reverse=True)


            value_of_first_pair_card_th = float(card_strength[names_of_two_pair_card_th[0]])
            value_of_second_pair_card_th = float(card_strength[names_of_two_pair_card_th[1]])

            rank = 15.0 + 0.01 * value_of_first_pair_card_th + 0.0001 * value_of_second_pair_card_th

        if list_of_rep.count(3) == 1:   #checking the existence of three_of_a_kind
            three_of_a_kind = True
            name_of_three_of_a_kind_card_th = [k for k, v in cards_dic_th.items() if v == 3]
            value_of_three_of_a_kind_card_th = float(card_strength[name_of_three_of_a_kind_card_th[0]])

            rank = 16.0 + 0.01 *value_of_three_of_a_kind_card_th

        if list_of_rep.count(4) == 1:   #checking the existence of four_of_a_kind
            four_of_a_kind = True
            name_of_four_of_a_kind_card_th = [k for k, v in cards_dic_th.items() if v == 4]
            value_of_name_of_four_fo_a_kind_card_th = float(card_strength[name_of_four_of_a_kind_card_th[0]])

            rank = 20.0 + 0.01 * value_of_name_of_four_fo_a_kind_card_th


        if one_pair == True and three_of_a_kind == True:    #checking the existence of full_hause


            rank = 19.0 + 0.01 * value_of_three_of_a_kind_card_th

        return rank







#"*********************************************************************************************************************************"

#"*********************************************************************************************************************************"

#"*********************************************************************************************************************************"



    def omaha_holdem(self, line_list):

        values_to_control_only_rank_oh = {}
        dic_hand_with_rank_oh = {}

        table_cards_oh = line_list[0]
        board_oh = [table_cards_oh[0:2], table_cards_oh[2:4], table_cards_oh[4:6], table_cards_oh[6:8], table_cards_oh[8:10]]
        cards_from_the_table_and_cards_from_the_hand = board_oh

        for position in line_list[1:]:
            players_cards_oh =[position[0:2], position[2:4], position[4:6], position[6:8]]

            max_value_oh, rank_1_oh = self.hand_evaluation_oh(board_oh, players_cards_oh)

   







    def hand_evaluation_oh(self, board_oh, players_cards_oh):

        hand_ranking = {"1.0" : "2", "2.0":"3", "3.0":"4", "4.0":"5", "5.0":"6", "6.0":"7",
                    "7.0":"8","8.0":"9", "9.0":"T", "10.0":"J", "11.0":"Q", "12.0":"K",
                    "13.0" :"A", "14.0":"One_pair", "15.0":"Two_pair", "16.0":"Three_of_a_kind",
                    "17.0":"Straight", "18.0":"Flush", "19.0":"Full_house", "20.0":"Four_of_kind", "21.0":"Straight_flush"}


        rank_1_oh = self.high_card_oh(board_oh, players_cards_oh)

        if self.flush_check_oh(board_oh, players_cards_oh) != 0:

            rank_2_oh = 18.0 + self.flush_check_oh(board_oh, players_cards_oh)

        else:
            rank_2_oh = 0




        if self.straight_and_straight_flush_oh(board_oh, players_cards_oh) != 0:

            rank_3_oh = self.straight_and_straight_flush_oh(board_oh, players_cards_oh)

        else:
            rank_3_oh = 0



        if self.kit_oh(board_oh, players_cards_oh) !=0:

             rank_4_oh = self.kit_oh(board_oh, players_cards_oh)
        else:
            rank_4_oh = 0

        max_value_oh = max (rank_1_oh, rank_2_oh, rank_3_oh, rank_4_oh)

        print(max_value_oh, rank_1_oh)
        return max_value_oh, rank_1_oh









    def high_card_oh(self, board_oh, players_cards_oh):



        list_of_high_card = []
        counter_board_oh = 0
        counter_players_cards_oh = 0
        counter_decimal_place = -2
        rank = 0

        cards =("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")

        for card in cards:
            for board_card_oh in board_oh:
                if card == board_card_oh[0] and counter_board_oh < 3:
                    counter_board_oh += 1
                    list_of_high_card.append(card)


        for card in cards:
            for player_card_oh in players_cards_oh:
                if card == player_card_oh[0] and counter_players_cards_oh < 2:
                    counter_players_cards_oh += 1
                    list_of_high_card.append(card)



        temp_list_of_values =[]

        for card in list_of_high_card:
            temp_list_of_values.append(float(card_strength.get(card)))
        temp_list_of_values.sort(reverse=True)



        for value in temp_list_of_values:
            counter_decimal_place += 2
            decimal_place = 10 ** counter_decimal_place
            rank += float(value / decimal_place)


        return 0.01 * rank

    def flush_check_oh(self, board_oh, players_cards_oh):

        colors_dic_oh_board = {}
        colors_dic_oh_players_cards = {}

        for card in board_oh:
            if card[1] in colors_dic_oh_board:
                colors_dic_oh_board[card[1]] += 1
            else:
                colors_dic_oh_board.update({card[1]:1})

        for card in players_cards_oh:
            if card[1] in colors_dic_oh_players_cards:
                colors_dic_oh_players_cards[card[1]] += 1
            else:
                colors_dic_oh_players_cards.update({card[1]:1})

        list_of_five_cards_the_same_color_oh =[]
        list_of_board_cards_the_same_color_oh =[]
        list_of_hand_cards_the_same_color_oh =[]




        for suit, value in colors_dic_oh_board.items():
            if value >= 3:
                for card in board_oh:
                    if card[1] == suit:
                        list_of_five_cards_the_same_color_oh.append(card)
                        list_of_board_cards_the_same_color_oh.append(card)




                for suit, value in colors_dic_oh_players_cards.items():
                    if value >= 2:
                        for card in players_cards_oh:
                            if card[1] == list_of_board_cards_the_same_color_oh[1][1]:
                                list_of_five_cards_the_same_color_oh.append(card)
                                list_of_hand_cards_the_same_color_oh.append(card)



                        if len(list_of_five_cards_the_same_color_oh) == 5:
                            card_value = self.high_card_oh(list_of_board_cards_the_same_color_oh, list_of_hand_cards_the_same_color_oh)
                        else:
                            card_value = 0


                        return card_value
                    else:
                        continue

            else:
                continue

        return 0

    def check_streight_flush(self, sort_card_string_oh, list_of_nine_cards_oh):

        color_of_5_cards = []

        for position in sort_card_string_oh:
            for card in list_of_nine_cards_oh:
                if position == card[0]:
                    color_of_5_cards.append(card[1])


        # set - removes repetition, if the number of repetitions equals exactly 1 - 4 removed colors were the same, which means that we have a color

        if len(set(color_of_5_cards)) == 1:
            return True
        else:
            return False


    def straight_and_straight_flush_oh(self, board_oh, players_cards_oh):
        list_of_nine_cards_oh = []

        for x in range(0,len(board_oh)):
            list_of_nine_cards_oh.append(board_oh[x])
        for x in range(0,len(players_cards_oh)):
            list_of_nine_cards_oh.append(players_cards_oh[x])






        list_strength_oh = []

        #assigning strength to individual cards:
        for card in list_of_nine_cards_oh:
            strength_oh = card_strength.get(card[0])
            list_strength_oh.append(float(strength_oh))

        list_strength_oh = list(set(list_strength_oh))



        list_strength_oh.sort()     #sorting cards by their strength


        sort_card_string_oh =""

        #returning the sorted cards:
        for position in list_strength_oh:
            sort_card_string_oh += card_strength_reverse.get(str(position))






        #checking if the sorted layout is really straight:
        if straight_superiority.find(sort_card_string_oh[0:5]) != -1 and self.check_2_from_hand(sort_card_string_oh[0:5], players_cards_oh) == True:

            if self.check_streight_flush(sort_card_string_oh[0:5],  list_of_nine_cards_oh) == True:
                return 21 + self.high_card_oh(sort_card_string_oh[0:5], players_cards_oh)
            else:
                return 17 + self.high_card_oh(sort_card_string_oh[0:5], players_cards_oh)

        elif straight_superiority.find(sort_card_string_oh[1:6]) != -1 and self.check_2_from_hand(sort_card_string_oh[1:6], players_cards_oh) == True:
            if self.check_streight_flush(sort_card_string_oh[1:6], list_of_nine_cards_oh) == True:
                return 21 + self.high_card_oh(sort_card_string_oh[1:6], players_cards_oh)
            else:
                return 17 + self.high_card_oh(sort_card_string_oh[1:6], players_cards_oh)

        elif straight_superiority.find(sort_card_string_oh[2:7]) != -1 and self.check_2_from_hand(sort_card_string_oh[2:7], players_cards_oh) == True:
            if self.check_streight_flush(sort_card_string_oh[2:7], list_of_nine_cards_oh) == True:
                return 21 + self.high_card_oh(sort_card_string_oh[2:7], players_cards_oh)
            else:
                return 17 + self.high_card_oh(sort_card_string_oh[2:7], players_cards_oh)

        elif straight_superiority.find(sort_card_string_oh[3:8]) != -1 and self.check_2_from_hand(sort_card_string_oh[3:8], players_cards_oh) == True:
            if self.check_streight_flush(sort_card_string_oh[3:8], list_of_nine_cards_oh) == True:
                return 21 + self.high_card_oh(sort_card_string_oh[3:8], players_cards_oh)
            else:
                return 17 + self.high_card_oh(sort_card_string_oh[3:8], players_cards_oh)

        elif straight_superiority.find(sort_card_string_oh[4:9]) != -1 and self.check_2_from_hand(sort_card_string_oh[4:9], players_cards_oh) == True:
            if self.check_streight_flush(sort_card_string_oh[4:9], list_of_nine_cards_oh) == True:
                return 21 + self.high_card_oh(sort_card_string_oh[4:9], players_cards_oh)
            else:
                return 17 + self.high_card_oh(sort_card_string_oh[4:9], players_cards_oh)

        elif straight_superiority.find(sort_card_string_oh[5:10]) != -1 and self.check_2_from_hand(sort_card_string_oh[5:10], players_cards_oh) == True:
            if self.check_streight_flush(sort_card_string_oh[5:10], list_of_nine_cards_oh) == True:
                return 21 + self.high_card_oh(sort_card_string_oh[5:10], players_cards_oh)
            else:
                return 17 + self.high_card_oh(sort_card_string_oh[5:10], players_cards_oh)

        elif "A" in sort_card_string_oh:
            second_sting_oh = "A" + sort_card_string_oh[:-1]
            if straight_superiority.find(second_sting_oh) != -1 and self.check_2_from_hand(second_sting_oh, players_cards_oh) == True:
                if check_streight_flush(self, second_sting_oh, list_of_nine_cards_oh) == True:
                    return 21 + self.high_card_oh(second_sting_oh)
                else:
                    return 17 + self.high_card_oh(second_sting_oh)
            else:
                return 0

        else:
            return 0


    #it checks if exactly two cards are from the hand, i.e. 3 are from the table(straight)
    def check_2_from_hand(self, sort_card_string_oh, players_cards_oh):
        counter = 0

        players_cards_oh_without_colour = []
        for card in players_cards_oh:
            players_cards_oh_without_colour.append(card[0])

        for card in sort_card_string_oh:
            if card[0] in players_cards_oh_without_colour:
                counter +=1

        if counter == 2:
            return True
        else:
            return False

    #it checks if exactly two cards are from the hand, i.e. 3 are from the table(full_house)
    def check_2_from_hand_full_house(self, repeating_cards, players_cards_oh):
        counter = 0

        players_cards_oh_without_colour = []
        for card in players_cards_oh:
            players_cards_oh_without_colour.append(card[0])


        for card in players_cards_oh_without_colour:
            if card[0] in repeating_cards:
                counter +=1

        if counter == 2:
            return True
        else:
            return False








    def repetition_of_cards_oh(self, board_oh, players_cards_oh):

        cards_dic_oh = {}
        for card in board_oh:
            if card[0] in cards_dic_oh:
                cards_dic_oh[card[0]] += 1
            else:
                cards_dic_oh.update({card[0]:1})

        for card in players_cards_oh:
            if card[0] in cards_dic_oh:
                cards_dic_oh[card[0]] += 1
            else:
                cards_dic_oh.update({card[0]:1})

        return cards_dic_oh




    #case check: two pairs, four of a kind
    def check_two_cards_from_hand(self, repeating_cards, players_cards_oh):

        players_cards_oh_without_colour = []
        for card in players_cards_oh:
            players_cards_oh_without_colour.append(card[0])


        counter = 0


        for card in players_cards_oh_without_colour:
            if card in repeating_cards:
                counter += 1

        if counter == 1 or counter == 2:

            return True
        else:
            return False

    def check_three_of_kind(self, repeating_cards, players_cards_oh):
        counter = 0

        players_cards_oh_without_colour = []
        for card in players_cards_oh:
            players_cards_oh_without_colour.append(card[0])



        for card in players_cards_oh_without_colour:
            if card in repeating_cards:

                counter += 1

        if counter <= 2:

            return True
        else:

            return False






    def kit_oh(self, board_oh, players_cards_oh):
        cards_dic_oh = self.repetition_of_cards_oh(board_oh, players_cards_oh)

        list_of_rep_oh = list(cards_dic_oh.values())

        repeating_cards = ""
        repeating_cards_three = ""
        repeating_cards_four = ""

        for card, amount in cards_dic_oh.items():
            if amount == 2:
                repeating_cards += card * 2

        for card, amount in cards_dic_oh.items():
            if amount == 3:
                repeating_cards_three += card * 3

        for card, amount in cards_dic_oh.items():
            if amount == 4:
                repeating_cards_four += card * 4

        repeating_cards_full_house = repeating_cards + repeating_cards_three







        rank = 0
        one_pair_oh = False

        three_of_a_kind_oh = False

        # checking the existence of one_pair
        if list_of_rep_oh.count(2) == 1: #checking the existence of one_pair
            one_pair_oh = True

            name_of_pair_card_oh = [k for k, v in cards_dic_oh.items() if v == 2]
            value_of_pair_card_oh = float(card_strength[name_of_pair_card_oh[0]])


            rank = 14.0 + 0.01 * value_of_pair_card_oh

        # checking the existence of two_pair
        if list_of_rep_oh.count(2) >= 2 and self.check_two_cards_from_hand(repeating_cards, players_cards_oh) == True: #checking the existence of two_pair


            names_of_two_pair_card_oh = [k for k, v in cards_dic_oh.items() if v == 2]

            names_of_two_pair_card_oh.sort(reverse=True)

            value_of_first_pair_card_oh = float(card_strength[names_of_two_pair_card_oh[0]])
            value_of_second_pair_card_oh = float(card_strength[names_of_two_pair_card_oh[1]])

            rank = 15.0 + 0.01 * value_of_first_pair_card_oh + 0.0001 * value_of_second_pair_card_oh

        if list_of_rep_oh.count(3) >=1 and self.check_three_of_kind(repeating_cards_three, players_cards_oh) == True: #checking the existence of three_of_a_kind
            three_of_a_kind_oh = True

            name_of_three_of_a_kind_card_oh = [k for k, v in cards_dic_oh.items() if v == 3]
            value_of_three_of_a_kind_card_oh = float(card_strength[name_of_three_of_a_kind_card_oh[0]])

            rank = 16.0 + 0.01 *value_of_three_of_a_kind_card_oh

        if list_of_rep_oh.count(4) >= 1 and self.check_two_cards_from_hand(repeating_cards_four, players_cards_oh) == True: #checking the existence of four_of_a_kind
            four_of_kind = True

            name_of_four_of_a_kind_card_oh = [k for k, v in cards_dic_oh.items() if v == 4]
            value_of_name_of_four_fo_a_kind_card_oh = float(card_strength[name_of_four_of_a_kind_card_oh[0]])

            rank = 20.0 + 0.01 * value_of_name_of_four_fo_a_kind_card_oh

        if one_pair_oh == True and three_of_a_kind_oh == True and self.check_2_from_hand_full_house(repeating_cards_full_house, players_cards_oh) == True: #checking the existence of full_house


            rank = 19.0 + 0.01 * value_of_three_of_a_kind_card_oh


        return rank

#"*********************************************************************************************************************************"

#"*********************************************************************************************************************************"

#"*********************************************************************************************************************************"

    #final sorting of the cards according to their strength
    #(according to two parameters: strength of the hand and
    #additionally in case of the same cards - strength of additional cards):

    def five_card_draw(self, line_list):
        dic_hand_with_rank = {}
        values_to_control_only_rank ={}


        for position in line_list:
            players_cards =[position[0:2], position[2:4], position[4:6], position[6:8], position[8:10]]     #breaking up the hand into individual cards
            max_value, rank_1 = self.hand_evaluation(players_cards)                                         #assigning the returned values - the maximum value of the card layout
            values_to_sort = (max_value, rank_1)                                                            #(parameters max_value - strength due to a specific card layout,
                                                                                                            #rank_1 - strength due to individual cards)
            values_to_control_only_rank[position] = rank_1




            dic_hand_with_rank[position] = values_to_sort                                                   #dictionary ={individual card: (max_value, rank_1)}

            sort_dict = dict(sorted(dic_hand_with_rank.items(), key=lambda item: item[1]))                  #Sorting the dictionary



        note, string_the_same_values, cards_to_remove = self.the_same_values_in_list(values_to_control_only_rank)   #assign the three values that the function returns:
                                                                                                                    #note, string_the_same_values, cards_to_remove

        list_of_sort_hands = sort_dict.keys()

        solution =""
        for hand in list_of_sort_hands:
            solution += hand +" "
        final_solution = solution[:-1]

        if note == True:            #No hand of cards of exactly the same strength

            return final_solution

        else:
            #there are hands of exactly the same strength:
            final_solution_with_equal = final_solution.replace(cards_to_remove[0], "temp_value")        #momentary introduction of a substitute value


            for hands in cards_to_remove:                                                               #removing unnecessary card layouts
                final_solution_with_equal = final_solution_with_equal.replace(hands + " ", "")
                final_solution_with_equal = final_solution_with_equal.replace(hands, "")


            final_solution_with_equal = final_solution_with_equal.replace("temp_value", string_the_same_values)     #to introduce a text string with a set of card hands of the same strength to solve



            return(final_solution_with_equal)


    #Determine if the set of cards contains cards of exactly the same strength:
    def the_same_values_in_list(self, values_to_control_only_rank):

        values_dic = {}
        string_the_same_values =""

        for value in values_to_control_only_rank:

            if values_to_control_only_rank[value] in values_dic:

                values_dic[values_to_control_only_rank[value]] += 1 #counter that sums up the hands of cards of the same value
            else:
                values_dic.update({values_to_control_only_rank[value]:1})



        if max(values_dic.values()) == 1:
            return True, None, None # no hand of cards of the same strength
        else:

            for value in values_dic.values():
                if value != 1:
                    card_value = [k for k, v in values_dic.items() if v > 1]                                #defining a set of cards of the same strength
                    card_name = [k for k, v in values_to_control_only_rank.items() if v == card_value[0]]

                    card_name.sort()
                    cards_to_remove = card_name                                 #Card sets that will have to be removed, because they will be replaced by a text string of card sets with the same strength
                    for card in card_name:
                        string_the_same_values += card +"="                     #Create a text string containing card layouts with the same strength along with the "=" sign

                    return(False, string_the_same_values[:-1], cards_to_remove)




    # Finding the highest card layout and assigning the appropriate rank to it:
    def hand_evaluation(self, players_cards):
        hand_ranking = {"1.0" : "2", "2.0":"3", "3.0":"4", "4.0":"5", "5.0":"6", "6.0":"7",
                    "7.0":"8","8.0":"9", "9.0":"T", "10.0":"J", "11.0":"Q", "12.0":"K",
                    "13.0" :"A", "14.0":"One_pair", "15.0":"Two_pair", "16.0":"Three_of_a_kind",
                    "17.0":"Straight", "18.0":"Flush", "19.0":"Full_house", "20.0":"Four_of_kind", "21.0":"Straight_flush"}

        rank_1 = self.high_card(players_cards)


        rank_5 = self.kit(players_cards)


        if self.flush_check(players_cards) == True:
            rank_2 = 18.0
        else:
            rank_2 = 0

        if self.straight(players_cards) == True:
            rank_3 = 17.0
        else:
            rank_3 = 0


        #If "Straight_flush" is present, it is assigned a rank of 21(straight_flush = flush + straight):
        if self.flush_check(players_cards) == True and self.straight(players_cards) == True:
            rank_4 = 21.0
        else:
            rank_4 = 0



        max_value = max(rank_1, rank_2, rank_3, rank_4, rank_5)

        return max_value, rank_1

    #determining the repetition (number of cards) that have the same strength:
    def repetition_of_cards(self, players_cards):
        cards_dic = {}
        for card in players_cards:
            if card[0] in cards_dic:
                cards_dic[card[0]] += 1
            else:
                cards_dic.update({card[0]:1})

        return cards_dic


    # The function "kit" checks the occurrence of:
    # - one_pair, two-pair, three_of_a_kind, full_house, four_of_kind
    # along with their strength for possible comparison
    def kit(self, players_cards):
        cards_dic = self.repetition_of_cards(players_cards)




        list_of_rep = list(cards_dic.values())


        rank = 0
        one_pair = False
        three_of_a_kind = False

        if list_of_rep.count(2) == 1:   #checking the existence of one_pair
            one_pair = True
            name_of_pair_card = [k for k, v in cards_dic.items() if v == 2]
            value_of_pair_card = float(card_strength[name_of_pair_card[0]])



            rank = 14.0 + 0.01 * value_of_pair_card



        if list_of_rep.count(2) == 2:   #checking the existence of two_pair
            two_pairs = True

            names_of_two_pair_card = [k for k, v in cards_dic.items() if v == 2]

            names_of_two_pair_card.sort(reverse=True)


            value_of_first_pair_card = float(card_strength[names_of_two_pair_card[0]])
            value_of_second_pair_card = float(card_strength[names_of_two_pair_card[1]])



            rank = 15.0 + 0.01 * value_of_first_pair_card + 0.0001 * value_of_second_pair_card


        if list_of_rep.count(3) == 1:   #checking the existence of three_of_a_kind
            three_of_a_kind = True
            name_of_three_of_a_kind_card = [k for k, v in cards_dic.items() if v == 3]
            value_of_three_of_a_kind_card = float(card_strength[name_of_three_of_a_kind_card[0]])



            rank = 16.0 + 0.01 *value_of_three_of_a_kind_card


        if list_of_rep.count(4) == 1:   #checking the existence of four_of_a_kind
            four_of_a_kind = True
            name_of_four_of_a_kind_card = [k for k, v in cards_dic.items() if v == 4]
            value_of_name_of_four_fo_a_kind_card = float(card_strength[name_of_four_of_a_kind_card[0]])


            rank = 20.0 + 0.01 * value_of_name_of_four_fo_a_kind_card

        if one_pair == True and three_of_a_kind == True:    #checking the existence of full_hause


            rank = 19.0 + 0.01 * value_of_three_of_a_kind_card


        return rank


    #checking the existence of straight:

    def straight(self, players_cards):


        list_straight_control =[]
        for card in players_cards:
            list_straight_control.append(card[0])




        list_strength =[]


        #assigning strength to individual cards:
        for card in list_straight_control:
            strength = card_strength.get(card)
            list_strength.append(float(strength))

        list_strength.sort()    #sorting cards by their strength

        sort_card_string =""

        #returning the sorted cards:
        for position in list_strength:
            sort_card_string += card_strength_reverse.get(str(position))



        #checking if the sorted layout is really straight:
        if straight_superiority.find(sort_card_string) != -1:
            return True
        else:
            return False




        if "A" in sort_card_string: #"Ace" at the beginning(beneath) of straight

            second_string ="A" + sort_card_string[:-1]

            if straight_superiority.find(second_string) != -1:
                return True
        return False



    #determining the strength of the hand only according to the strength of
    #the individual cards starting with the highest card:

    def high_card(self, players_cards):

        counter = -2
        rank = 0

        cards =("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
        for card in cards:
            for player_card in players_cards:
                if card == player_card[0]:
                    counter += 2
                    decimal_place = 10 ** counter
                    card_strength.get(card)
                    rank += (float(card_strength.get(card)) / decimal_place)

        return rank

    #Checking if all the cards in the hand are of the same suit - flush:
    def flush_check(self, players_cards):

        colors_dic = {}
        for card in players_cards:
            if card[1] in colors_dic:
                colors_dic[card[1]] += 1
            else:
                colors_dic.update({card[1]:1})
        for suit in colors_dic:
            if colors_dic[suit] == 5:
                return True
            else:
                return False


