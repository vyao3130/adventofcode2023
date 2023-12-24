list1 = [10, 13, 16, 21, 30, 45]

print(f"{[list1[place+1] - num for place, num in enumerate(list1[:-1])]}")

def sequence_finder(sequence : list[int], nums_to_add : list[int]):
    if not sequence.count(0) == len(sequence): 
        nums_to_add.append(sequence[0])
        new_sequence = [sequence[place + 1] - num for place, num in enumerate(sequence[:-1])]
        print(f"{new_sequence}\n" )
        return sequence_finder(new_sequence, nums_to_add)

    first_val = nums_to_add.pop(0)
    for num in nums_to_add:
        first_val-=num
    print(f"The numbers to add all together are {nums_to_add}, which gives {first_val}")
    return sum(nums_to_add)

print(sequence_finder(list1, []))
