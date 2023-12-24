# find next num

sols = []
final_numlist = []

# sequence, return final value
def sequence_finder(sequence : list[int], nums_to_add : list[int]):
    if not sequence.count(0) == len(sequence): 
        nums_to_add.append(sequence[-1])
        new_sequence = [sequence[place + 1] - num for place, num in enumerate(sequence[:-1])]
        return sequence_finder(new_sequence, nums_to_add)

    x = sum(nums_to_add)
    sols.append(f"The numbers to add all together are {nums_to_add}, which gives {x}")
    return sum(nums_to_add)

with open("input.txt", 'r') as f:
    for line in f:
        cline = line.replace("\n", "")
        num_list = [int(num) for num in cline.split(' ')]
        sols.append(f"{num_list} \n")
        final_num = sequence_finder(num_list, [])
        sols.append(f"Final number in sequence: {final_num} \n")
        final_numlist.append(final_num)

    sols.append(f"Final number list is {final_numlist} \n")
    sols.append(f"Final result is {sum(final_numlist)} \n")
    print(f"Final value is {sum(final_numlist)} \n")

with open("solutions.txt", "w") as f:
    for line in sols:
        f.write(line)