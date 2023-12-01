numbers = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
}

def find_num(check_num):
    for num in list(numbers.keys()):
        print(num)
        if num in check_num:
            found_num = numbers.get(num)
            break
        else:
            found_num = 0
    return found_num

solutions = []

with open('input.txt', 'r') as f:
    final_num = 0
    for line in f:
        solutions.append(line)
        print(line)
        line_len = len(line)-1

        check_num=""
        for i in range(line_len):
            if line[i].isnumeric():
                final_num+=int(line[i])*10
                print(line[i])
                solutions.append(line[i]+'\n')
                break
            check_num=check_num + line[i]
            num = find_num(check_num)
            print(check_num)
            print(num)
            if num != 0:
                final_num+=num*10
                solutions.append(str(num)+'\n')
                break

        check_num=""
        for i in range(line_len+1):
            if line[line_len-i].isnumeric():
                final_num+=int(line[line_len-i])
                solutions.append(line[line_len-i]+'\n')
                print(line[line_len-i])
                break
            check_num =line[line_len-i]+check_num
            num = find_num(check_num)
            if num != 0:
                final_num+=num
                solutions.append(str(num)+'\n')
                break
   
        print(f"final num: {final_num}")



print(solutions)
with open('sol.txt', 'w') as f:
    for line in solutions:
        f.write(line)

print(find_num("sixteen"))