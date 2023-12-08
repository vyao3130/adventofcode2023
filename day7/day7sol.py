card_type = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_values = {card:str(22-num) for num, card in enumerate(card_type)}
# assign ?numeric value? to every card hand
# smallest value at beginning
# assuming no repeated hands..
hand_values_list = []
hand_to_pile = {}
sols = []

with open("input.txt", "r") as f:
    values = [] # list of all hand values, weakest to strongest
    for line in f:
        line=line.split(" ")
        hand = line[0]
        winnings = int(line[1].replace("\n",""))
        sols.append(f"Working on hand {hand} \n")
        card_hash = {}
        total_hand_value = 0
        for card in hand: # work on every card
            card_val = card_values.get(card)
            card_hash[card_val] = card_hash.get(card_val, 0)+1
            sols.append(f"{card_hash}\n")
        # sols.append(f"The list of cards in sorted order looks like {card_hash} \n")

        main_pairs = []
        othercards = []
        doubles_list = []
        doubles = []
        ranking_num = 0
        cases345 = False
        for card, num in card_hash.items():
            if  num > 3: # cases 4 and 5
                main_pair=card
                ranking_num = num+1
                count = num
                cases345 = True
            elif num == 3:
                main_pair=card
                count = num
                ranking_num = num
                cases345 = True
            elif num == 2:
                doubles.append(card)
            else:
                othercards.append(card)
        
        othercards.sort(reverse=True)
        if len(doubles) == 2: # 2 pairs of 2
            doubles_list = [doubles[0] for i in range(2)]
            doubles_list.extend(doubles[1] for i in range(2))
            doubles_list.sort(reverse=True)
            ranking_num = 2
        elif doubles and ranking_num != 3: # 1 pair of 2
            doubles_list = [doubles[0] for i in range(2)]
            ranking_num = 1

        if ranking_num == 3 and doubles: # full house
            doubles_list = [doubles[0] for i in range(2)]
            ranking_num = 4
            main_pairs = [main_pair for i in range(3)]
        
        if cases345:
            main_pairs = [main_pair for i in range(count)]

        types_hands = {0:"Highest num", 1:"One pair", 2:"Two pair", 3:"Three of a kind", 4:"Full house", 5:"Four of a kind", 6:"Five of a kind"}
        sols.append(f"The ranking num is {types_hands.get(ranking_num)} with {ranking_num} zeroes\n")
        compiled_list = main_pairs + doubles_list + othercards
        sols.append(f"The total list of nums is {compiled_list}\n")
        total_hand_value = int("".join(compiled_list))*10**ranking_num
        sols.append(f"The total hand value is {total_hand_value} associated with {winnings}\n")
        hand_values_list.append(total_hand_value)
        if total_hand_value in hand_to_pile.keys():
            print(f"doubled up on {total_hand_value}")
        hand_to_pile[total_hand_value]=winnings
    
    sols.append(f"Hand to pile dict looks like {hand_to_pile}\n")
    hand_values_list.sort()
    sols.append(f"The hand values pile looks like: {hand_values_list}\n")
    total_winnings = 0
    rank = 1
    for hand in hand_values_list:
        total_winnings+=hand_to_pile.get(hand)*rank
        rank+=1

    print(f"The grand total is {total_winnings}")
        
        
with open("solutions.txt", "w") as f:
    for line in sols:
        f.write(line)

