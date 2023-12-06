solutions=[]
working_list = []
mapping_dict = []
with open("example.txt", "r") as f:
    
    for line in f:
        solutions.append(line)
        line=line.replace("\n", "")
        if "seeds" in line: # seed line
            seed_line = line.split(" ")
            seed_list = seed_line[1:]
            unparsed_seed_list = [int(i) for i in seed_list]
            tuples_seed_list = [(unparsed_seed_list[i], unparsed_seed_list[i+1]) for i in range(0, len(seed_list), 2)]
            solutions.append(f"List of seeds: {tuples_seed_list} \n")
        
        elif "map" in line: # place into according destinations
            solutions.append("Mapping for previous map \n")
            new_seed_range=[]
            for place, seed_range in enumerate(seed_list):
                seed_begin, start_seed_range = seed_range
                for ranges in mapping_dict:
                    seed_destination, seed_location, seed_range = ranges
                    max_seed_location = seed_location+seed_range-1 #inclusive range
                    if seed_location<seed_begin<max_seed_location: # beginning of seed range in the mapping dict
                        if seed_location<seed_begin+start_seed_range<max_seed_location:# seed range all within mapping dict
                            new_seed_range.append((seed_destination+(seed_begin-seed_location), start_seed_range)) # part in map
                        else: # beginning still in range, seed range hangs a bit out of mapping dict
                            new_seed_range.append((seed_destination+(seed_begin-seed_location), (seed_location+seed_range)-seed_begin)) # part in map
                            new_seed_range.append((max_seed_location+1, start_seed_range-(max_seed_location-seed_begin+1))) # part outside map
                    elif seed_begin<seed_location: # beginning of seed range before seed location mapping
                        if seed_begin+start_seed_range<seed_begin: # seed range not in map
                            new_seed_range.append((seed_begin, start_seed_range))
                        elif seed_location<seed_begin+start_seed_range<max_seed_location: # end of seed range within map
                            new_seed_range.append((seed_begin, seed_location-seed_begin))# beginning part outside of map
                            new_seed_range.append((seed_destination, (seed_begin + start_seed_range + 1)-seed_location))# part inside of map
                        elif seed_location<seed_begin+start_seed_range>max_seed_location: # end of seed range outside of map
                            new_seed_range.append((seed_begin, seed_location-seed_begin))# part outside of map start
                            new_seed_range.append((seed_destination, (seed_begin + start_seed_range + 1)-seed_location))# part inside of map
                            new_seed_range.append((max_seed_location+1, seed_begin+start_seed_range-max_seed_location-1))# part outside of map end
                    else: # seed range not in map - beginning is after dictionary range
                        new_seed_range.append((seed_begin, start_seed_range))

                    # solutions.append(f"Seed dict info: {seed_destination}, {seed_location}, {seed_range} \n")
                    # solutions.append(f"max seed location {max_seed_location} \n")
                        # seed_list[place] = new_loc  
                        # solutions.append(f"Mapped {seed} to {new_loc} \n")

            solutions.append(f"Now starting to process {line}\n")
            mapping_dict=[]
        
        else: # otherwise keep putting stuff into mapping_dict
            if line:
                mapping_set = line.split(" ")
                seed_destination = int(mapping_set[0])
                seed_location = int(mapping_set[1])
                range_locations = int(mapping_set[2])
                solutions.append(f"seed location: {seed_location}, seed destination: {seed_destination}, range: {range_locations}\n")
                mapping_dict.append((seed_destination, seed_location, range_locations)) # tuple of information
                solutions.append(f"Added locations so the new mapping dict looks like {mapping_dict} \n")
    
    solutions.append(f"Final seed destinations look like {seed_list}")
    # find smallest location
    closest = seed_list[0]
    for location in seed_list:
        if closest > location:
            closest = location
    print(f"The closest location is {closest}")

with open("solutions.txt", "w") as f:
    for line in solutions:
        f.write(line)
