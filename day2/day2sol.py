import re
colors = ["green", "red", "blue"]
color_limit = {
    "red": 12,
    "green": 13,
    "blue": 14
}
games_valid = 0
solutions = []
with open("input.txt", "r") as f:
    for game_num, line in enumerate(f):
        game_num+=1
        games = re.sub('[;,\n]', "", line)
        games2 = games.replace(",", "")
        game_choice = games2.split(" ")
        solutions.append(line + "\n")
        print(game_choice)

        valid = True
        for num, elem in enumerate(game_choice):
            if elem in colors:
                print(elem)
                if int(game_choice[num-1]) > color_limit.get(elem):
                    valid = False
                    print(f"{int(game_choice[num-1])} greater than {color_limit.get(elem)}")
                    solutions.append(f"{int(game_choice[num-1])} greater than {color_limit.get(elem)} \n")
                    break
        if valid:
            games_valid+=game_num
            print(f"game num {game_num} is valid")
            solutions.append(f"game num {game_num} is valid\n")
    
    print(f"The total is {games_valid}")
    
with open("sol.txt", "w") as f:
    for line in solutions:
        f.write(line)