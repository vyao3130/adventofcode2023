solutions = []

with open("input.txt", "r") as f:
    card_pile_total = 0
    for card in f:
        card_total = 1
        found_match = False
        winning_nums = []
        given_nums = []
        without_card_num = card.split(":")[1].replace("\n", "")
        winning_nums = ((without_card_num.split("|")[0]).split(" "))
        given_nums = ((without_card_num.split("|")[1]).split(" "))
        solutions.append(f"{without_card_num}\n")
        solutions.append(f"{winning_nums}\n")
        solutions.append(f"{given_nums}\n")

        for num in winning_nums:
            if num.isnumeric():
                if num in given_nums and found_match:
                    card_total=card_total*2
                    solutions.append(f"Found {num} in given numbers set. Card value is {card_total}\n")
                if num in given_nums and not found_match:
                    found_match = True
                    solutions.append(f"Found {num} in given numbers set.\n")
        
        if found_match:
            card_pile_total+=card_total
            solutions.append(f"Added {card_total}\n")

    print(f"The card pile total is {card_pile_total}")
    solutions.append(f"The card pile total is {card_pile_total}")

with open("solutions.txt", "w") as f:
    for line in solutions:
        f.write(line)