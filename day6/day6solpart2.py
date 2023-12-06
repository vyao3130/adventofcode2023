solutions = []

file="input.txt"

with open(file, "r") as f:
    times=[]
    distance=[]
    races=[]
    for line in f:
        line = line.replace("\n", "")
        if "Time" in line:
            line=line.split(" ")[1:]
            times=[i for i in line if i.isnumeric()]
        if "Distance" in line:
            line=line.split(" ")[1:]
            distance=[i for i in line if i.isnumeric()]
    
    races=[("".join(times), "".join(distance))]
    solutions.append(f"{races} \n")
    # calculate times
    button_ranges = []
    for race in races:
        t, w = race
        time = int(t)
        win_distance = int(w)
        solutions.append(f"Finding winning times for time {time} and distance to beat is {win_distance} \n")
        # check the range
        button_range = 0
        found_min = False
        min_press = 0
        found_max = False
        max_press = 0
        for button_press in range(time): # find minimum 
            min_speed = button_press
            max_speed = time-button_press
            min_remaining_time = time-min_speed
            max_remaining_time = time-max_speed
            if found_min and found_max:
                button_range = max_press - min_press + 1
                break
            if not found_min and win_distance<min_remaining_time*min_speed:
                min_press=button_press
                solutions.append(f"The minimum button press is {min_press} \n")
                found_min=True
            if not found_max and (win_distance<max_remaining_time*max_speed and win_distance<(max_remaining_time+1)*(max_speed-1)):
                max_press=max_speed
                solutions.append(f"The maximum button press is {max_press} \n")
                found_max=True
        solutions.append(f"The number of ways to win is {button_range}\n")
        button_ranges.append(button_range)
    beat_records = 1
    for num in button_ranges:
        beat_records*=num
    print(f"The multiplication total is {beat_records}")


    


with open("solutions.txt", "w") as f:
    for line in solutions:
        f.write(line)