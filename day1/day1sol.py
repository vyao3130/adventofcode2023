solutions = []
with open('input.txt', 'r') as f:
    final_num = 0
    for line in f:
        solutions.append(line)
        print(line)
        line_len = len(line)-1

        for i in range(line_len):
            if line[i].isnumeric():
                final_num+=int(line[i])*10
                print(line[i])
                solutions.append(line[i]+'\n')
                break

        for i in range(line_len+1):
            if line[line_len-i].isnumeric():
                final_num+=int(line[line_len-i])
                solutions.append(line[line_len-i]+'\n')
                print(line[line_len-i])
                break

        print(f"final num: {final_num}")

print(solutions)
with open('sol.txt', 'w') as f:
    for line in solutions:
        f.write(line)

