solutions=[]
lines_num_dict=[]
symbol_dict = {}
gear_no = 0
with open("input.txt", "r") as f:
    for line_num, line in enumerate(f):
        line_num_dict = {}
        part_number = ""
        numbers_loc = []

        # handle single line
        solutions.append(line+"\n")
        for count, char in enumerate(line):
            if char.isnumeric():
                part_number+=char
                numbers_loc.append(count)
            else:
                if numbers_loc:
                    for place, loc in enumerate(numbers_loc):
                        line_num_dict[loc]=part_number
                    solutions.append(f"Added {part_number} to {line_num_dict}"+"\n")
                    part_number=""
                    numbers_loc=[]
                if char == "*": # gear time, list of tuples (line_no,loc)
                    # :)
                    gear_ref = "gear"+str(gear_no)
                    symbol_dict[gear_ref]=[]
                    symbol_dict[gear_ref].append((line_num-1,count))
                    symbol_dict[gear_ref].append((line_num+1,count))
                    if count != 0:
                        symbol_dict[gear_ref].append((line_num-1,count-1))
                        symbol_dict[gear_ref].append((line_num,count-1))
                        symbol_dict[gear_ref].append((line_num+1,count-1))
                    if count < len(line) - 1:
                        symbol_dict[gear_ref].append((line_num,count+1))
                        symbol_dict[gear_ref].append((line_num-1,count+1))
                        symbol_dict[gear_ref].append((line_num+1,count+1))
                    gear_no+=1

        # add line dictionary with numbers into list of line dictionaries
        lines_num_dict.append(line_num_dict)
        # solutions.append(f" Digit table now updated to look like: {lines_num_dict} \n")
        solutions.append(f" Symbol table now updated to look like: {symbol_dict} \n")

    solutions.append(f"Updated numbers dictionary to look like {lines_num_dict}\n")
    
    total = 0
    values_added = []
    for gear, locations in symbol_dict.items():
        # assume only 2 part numbers are involved...
        gear1 = False
        gear1Val=0
        gear2Val=0
        part_seen = []
        for location in locations: # list of valid locations - spans
            solutions.append(f"Working on gear {gear} \n")
            line_num, place = location
            val = lines_num_dict[line_num].get(place, None)
            if val:
                solutions.append(f"Found val {val} at {line_num}, {place} \n")
                if gear1 and ((line_num, place) not in part_seen):
                    gear2Val=val
                    solutions.append(f"Found val {gear2Val} as gear 2 val \n")
                    total+=int(gear1Val)*int(gear2Val)
                    solutions.append(f"Adding the multiplied value of {gear1Val} and {gear2Val}\n")
                    break #again assuming only 2 part numbers are involved.
                # found first gear
                gear1 = True
                gear1Val = val
                part_seen.append((line_num, place-1))    
                part_seen.append((line_num, place+1)) 
                solutions.append(f"Found val {gear1Val} as gear 1 val \n")
                # values_added.append(val)
                # solutions.append(f"added {val} \n")
    print(f"final val {total}")
                
with open("solution.txt", "w") as f:
    for line in solutions:
        f.write(line)
