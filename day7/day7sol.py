card_type = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_values = {card:str(22-num) for num, card in enumerate(card_type)}
# assign ?numeric value? to every card hand
# smallest value at beginning
# assuming no repeated hands..
sols = []

with open("example.txt", "r") as f:
    values = [] # list of all hand values, weakest to strongest
    for line in f:
        line=line.split(" ")
        hand = line[0]
        winnings = line[1]
        sols.append(f"Working on hand {hand} \n")
        card_hash = {}
        total_hand_value = 0
        for card in hand: # work on every card
            card_val = card_values.get(card)
            card_hash[card_val] = card_hash.get(card_val, 0) +1
            sols.append(f"{card_hash}\n")
        sols.append(f"The list of cards in sorted order looks like {card_hash} \n")

        if 5 in card_hash.values():
            total_hand_value=""
            for item in card_hash.keys():
                pair = item
            total_hand_value = int([pair for i in range(5)].join(""))*100000
        elif 4 in card_hash.values():
            for card, count in card_hash.items():
                if count == 4:
                    pair = card
                else:
                    othercard = card
            total_hand_value = int(([pair for i in range(4)].append(othercard)).join(""))*10000
        elif 3 in card_hash.values():
            if 2 in card_hash.values():
                for card, count in card_hash.items():
                    if count == 3:
                        pair = card
                    else:
                        othercard = card
                total_hand_value = int(([pair for i in range(3)].extend(othercard for i in range(2))).join(""))*1000
            else:
                othercard = []
                for card, count in card_hash.items():
                    if count == 3:
                        pair = card
                    else:
                        othercard.append(card)
                othercard.sort(reverse=False)
                total_hand_value = int(([pair for i in range(3)].extend(othercard)).join(""))*100
        elif 2 in card_hash.values() and 3 not in card_hash.values():
            othercard = []
            for card, count in card_hash.items():
                if count == 2:
                    pair = card
                else:
                    othercard.append(card)
            othercard.sort(reverse=False)
            listOne = [pair for i in range(2)]
            listOne.extend(othercard)
            print(f"ffffffffff {listOne}")
            total_hand_value = int("".join(listOne))*10
            
        else:
            card_list = [int(card) for card in card_hash]
            card_list.sort(reverse=True)
            total_hand_value = int([str(card) for card in card_list].join(""))*1
        
        sols.append(f"The total card value is {total_hand_value} \n")
        # sort card hash to give string with biggest combination at the beginning
        
        
with open("solutions.txt", "w") as f:
    for line in sols:
        f.write(line)

