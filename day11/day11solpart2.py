sols = []
DISTANCE = 1000000
# FILE = "example.txt"
FILE = "input.txt"
def expand_space(galaxy : [list[list[chr]]]) -> list[tuple]:
    galaxy_index = []
    seen_galaxies = set()
    line_num = 0

    for line in galaxy:
        if line.count('.') == len(line):
            # print(f"{line_num} is empty")
            line_num+=DISTANCE # expand row
        else:
            for column, space in enumerate(line):
                if space == "#":
                    # print(f"Found galaxy in {line_num} column {column}")
                    seen_galaxies.add(column)
                    galaxy_index.append((line_num, column))
            line_num+=1

    col_dict = {}
    unseen_columns = [column for column in range(len(line)) if column not in seen_galaxies]
    # print(f" Seen galaxies in column : {seen_galaxies}")
    # print(f" Unseen galaxies in columns : {unseen_columns}")
    expanded_num = -1
    for num in range(len(line)): # map old columns to new expanded cols
        if num in unseen_columns:
            expanded_num+=DISTANCE
        else:
            expanded_num+=1
        col_dict[num]=expanded_num
    # print(f"Mapping dictionary: {col_dict}")
    f_galaxy_index = []
    for g_row, g_col in galaxy_index:
        # print(f"{g_row},{g_col}" )
        new_col = col_dict.get(g_col)
        f_galaxy_index.append((g_row, new_col))
    # print(f"New Galaxy Index:{f_galaxy_index}")
    return f_galaxy_index

def find_distances(galaxy_indexes : list[tuple]) -> int:
    distance = 0
    other_index = galaxy_indexes.copy()
    for galaxy in galaxy_indexes:
        og_row, og_col = galaxy
        other_index.remove(galaxy)
        # print(f"Working on galaxy {galaxy}")
        for g_row, g_col in other_index:
            shortest_path = abs(g_row-og_row) + abs(g_col-og_col)
            # print(f"Adding value {shortest_path} to total distance from {g_row} and {g_col}")
            distance+=shortest_path
    # print(f"Total distance is {distance}")

    return distance

with open(FILE, "r") as f:
    galaxy = []
    for line in f:
        cline = line.replace("\n", "")
        space_line = [i for i in cline]
        galaxy.append(space_line)
    index_galaxies = expand_space(galaxy)
    total_distance = find_distances(index_galaxies)
    print(f"The total distance is {total_distance}")

with open("solutions.txt", "w") as f:
    for line in sols:
        f.write(line)