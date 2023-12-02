import re
colors = ["green", "red", "blue"]
total_powers = 0
solutions = []

with open("input.txt", "r") as f:
    for game_num, line in enumerate(f):
        color_limit = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
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
                    color_limit[elem] = int(game_choice[num-1])
                    print(f"{int(game_choice[num-1])} greater than {color_limit.get(elem)}")
                    solutions.append(f"{int(game_choice[num-1])} greater than {color_limit.get(elem)} \n")
        
        # finished with game
        total = 1
        for elem in colors:
            print(f"The largest num of {elem} is {color_limit.get(elem)}")
            total = total*color_limit.get(elem)
        
        total_powers+=total
    print(f"The total is {total_powers}")
    
with open("sol.txt", "w") as f:
    for line in solutions:
        f.write(line)