import re
sols = []

direction_dict = {}
with open("input.txt", "r") as f:
    for num, line in enumerate(f):
        line = line.replace("\n", "")
        if num == 0: # direction line
            directions_list = [char for char in line]
        elif line: # map line
            directions = line.split(" ")
            line_mapdict = {}
            find_locations = re.compile(r'(\w\w\w)')
            location_list = find_locations.findall(line)
            sols.append(f"{location_list}\n")
            direction_dict[location_list[0]+'R']=location_list[2]
            direction_dict[location_list[0]+'L']=location_list[1]
    
    sols.append(f"The location dictionary looks like: {direction_dict}\n")
    starting_location = 'AAA'
    found_destination = False
    steps = 0
    while not found_destination:
        for direction in directions_list:
            if steps == 0:
                sols.append(f"Starting at location {starting_location}\n")
                new_location = direction_dict[starting_location+direction]
                sols.append(f"Going {direction} toward {new_location}\n")
            else:
                new_location = direction_dict[new_location+direction]
                sols.append(f"Going {direction} toward {new_location}\n")
            steps+=1
        if new_location == "ZZZ":
            found_destination=True
    sols.append(f"The total number of steps is {steps}")




with open("sols.txt", "w") as f:
    for line in sols:
        f.write(line)