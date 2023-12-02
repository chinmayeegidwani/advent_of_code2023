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
    highest_blue = 0
    highest_red = 0
    highest_green = 0
    for index in re.finditer(blue, line):
        num_blues = int((line[index.start()-3]+line[index.start()-2]).strip())
        if num_blues > highest_blue:
            highest_blue = num_blues
        # if num_blues > max_blues:
        #      line_flag = False
        #      break
    for index in re.finditer(red, line):
        num_reds = int((line[index.start()-3]+line[index.start()-2]).strip())
        if num_reds > highest_red:
            highest_red = num_reds
        # if int(num_reds) > max_reds:
        #     line_flag = False
        #     break
        
    for index in re.finditer(green, line):
        num_greens = int((line[index.start()-3]+line[index.start()-2]).strip())
        if num_greens > highest_green:
            highest_green = num_greens        
        # if int(num_greens) > max_greens:
        #     line_flag = False
        #     break

    prod = highest_green * highest_blue * highest_red
    sum += prod
    #if line_flag:
        #sum += line_num
    
    line_num += 1        
print(sum)
