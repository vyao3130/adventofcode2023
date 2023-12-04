solutions=[]
lines_num_dict=[]
symbol_dict = []
for i in range(3):
    symbol_dict.append([])

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
                if char != "." and char != "\\" and char != "n" and char != "\n":
                    # :)
                    symbol_dict[line_num-1].append((count, char))
                    symbol_dict[line_num+1].append((count, char))
                    if count != 0:
                        symbol_dict[line_num-1].append((count-1, char))
                        symbol_dict[line_num].append((count-1, char))
                        symbol_dict[line_num+1].append((count-1, char))
                    if count < len(line) - 1:
                        symbol_dict[line_num].append((count+1, char))
                        symbol_dict[line_num-1].append((count+1, char))
                        symbol_dict[line_num+1].append((count+1, char))

        symbol_dict.append([])
        # add line dictionary with numbers into list of line dictionaries
        lines_num_dict.append(line_num_dict)
        # solutions.append(f" Digit table now updated to look like: {lines_num_dict} \n")
        solutions.append(f" Symbol table now updated to look like: {symbol_dict} \n")

    solutions.append(f"Symbol table looks like {symbol_dict}")
    symbol_dict=symbol_dict[:-3]
    solutions.append(f"Updated Symbol table to look like {symbol_dict} based off of {len(symbol_dict)} \n")
    solutions.append(f"Updated numbers dictionary to look like {lines_num_dict}")
    
    total = 0
    values_added = []
    for line_num, entry in enumerate(symbol_dict):
        for location in entry: # list of symbol locations
            loc, char = location
            val = lines_num_dict[line_num].get(loc, None)
            if val:
                total+=int(val)
                # works by assuming we're still reading left to right
                possible_places = []
                solutions.append(f"Found {val} at line number {line_num},{loc} to be valid according to symbol {char}. Adding to total {total} \n")
                lines_num_dict[line_num][loc] = "0" # lol
                # this is the worst IM GOING
                total_erased=0
                add = True
                subtract = True
                lines_num_dict[line_num][loc] = "0" # lol   
                for i in range(len(val)):
                    if (not add) and (not subtract):
                        break
                    if subtract:
                        num = lines_num_dict[line_num].get(loc-i, None)
                        if num:
                            lines_num_dict[line_num][loc-i]="0"
                            solutions.append(f"Changed {num} at line num {line_num} at location {loc-i} \n")
                            total_erased+=1
                        else:
                            subtract=False
                    if add:
                        num = lines_num_dict[line_num].get(loc+i, None)
                        if num:
                            solutions.append(f"Changed {num} at line num {line_num} at location {loc+i} \n")
                            lines_num_dict[line_num][loc+i]="0"
                            total_erased+=1
                        else:
                            add=False
                    
                # values_added.append(val)
                # solutions.append(f"added {val} \n")
    print(f"final val {total}")
                
with open("solution.txt", "w") as f:
    for line in solutions:
        f.write(line)
