import re
file_list = open("input.txt").readlines()

# 12 red cubes, 13 green cubes, and 14 blue cubes
max_blues = 14
max_reds = 12
max_greens = 13
red = "red"
blue = "blue"
green = "green"

line_num = 1
sum = 0
for line in file_list:
    #print(line)
    line_flag = True
    for index in re.finditer(blue, line):
        num_blues = int((line[index.start()-3]+line[index.start()-2]).strip())
        if num_blues > max_blues:
             line_flag = False
             break
    for index in re.finditer(red, line):
        num_reds = int((line[index.start()-3]+line[index.start()-2]).strip())

        if int(num_reds) > max_reds:
            line_flag = False
            break
        
    for index in re.finditer(green, line):
        num_greens = int((line[index.start()-3]+line[index.start()-2]).strip())
        if int(num_greens) > max_greens:
            line_flag = False
            break
    if line_flag:
        sum += line_num
        #print(line_num)
    line_num += 1        
print(sum)
