solutions = []
match_array = []
with open("input.txt", "r") as f:
    card_pile_total = 0
    for card in f:
        num_matches = 0
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
                if num in given_nums: # found match
                    num_matches+=1
        
        match_array.append(num_matches)
        solutions.append(f"Found {num_matches}\n")

    solutions.append(f"The match array is {match_array} \n")
    # parse the match array to find the total number of card copies
    card_copies = 1
    first_copy = True
    print("Start parsing match array")
    print(f"{match_array}")
    card_total_array = [1 for i in range(len(match_array))]
    for card_num, num_matches in enumerate(match_array):
        if num_matches>0:
            copy_num = card_num+1
            card_total = card_total_array[card_num]
            # handle the copies for each row
            for i in range(copy_num,copy_num+num_matches):
                card_total_array[i]=card_total_array[i]+card_total
    solutions.append(f"The card total pile looks like {card_total_array}")
    for num in card_total_array:
        card_pile_total+=num
    print(f"There are {card_pile_total} cards in total \n")
    


with open("solutions.txt", "w") as f:
    for line in solutions:
        f.write(line)