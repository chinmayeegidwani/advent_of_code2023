gears_list = []
def is_symbol(c):
    if not c.isdigit() and c != ".":
        return True
    return False

def is_gear_symbol(c):
    # Pt 2
    if c == "*":
        return True
    return False

def padding(list):
    # Pad full list to avoid bounds issues
    dots = ""
    list2 = []
    for i in range(0, len(list[0])):
        dots += "."
    list2.append(dots)

    for row in list:
        row = row.strip()
        row = "." + row
        row = row + "."
        list2.append(row)
    list2.append(dots)
    return list2

def concat(indices, row):
    # Concatenate adjacent digits into number
    cat_num = ""
    for i in range(indices[0], indices[-1]+1):
        cat_num += str(row[i])
    #print(cat_num)
    return int(cat_num)

def find_congruent_nums(row):
    # Return start and end indices of congruent numbers
    start = 0
    end = 0
    ret_list = []
    i = 0
    flag = False
    for c in row:
        if c.isdigit():
            if not flag:
                start = i
                end = i
                flag = True  
            else:
               end = i
        else:
            if flag:
                ret_list.append([start, end])
                flag = False
        i += 1

    return ret_list

def check_adjacent(num_indices, row, top, bottom):
    # Returns True if symbol detected in adjacent tiles
    start = num_indices[0] 
    end = num_indices[1]

    if is_symbol(row[start-1]) or is_symbol(row[end+1]):
        return True
    if is_symbol(top[start-1]) or is_symbol(bottom[start-1]) or is_symbol(top[end+1]) or is_symbol(bottom[end+1]):
        return True
    for i in range(start, end+1):
        if is_symbol(top[i]) or is_symbol(bottom[i]):
            return True
    return False



def check_adjacent_gears(num_indices, row, top, bottom, row_index):
    # Finds gear location and adds part numbers to list
    start = num_indices[0]
    end = num_indices[1]
 
    
    if is_gear_symbol(row[start-1]):
        add_to_gears_list([row_index, (start-1), concat(num_indices, row)])

    if is_gear_symbol(row[end+1]):
        add_to_gears_list([row_index, (end+1), concat(num_indices, row)])

    if is_gear_symbol(top[start-1]):
        add_to_gears_list([row_index-1, (start-1), concat(num_indices, row)])

    if is_gear_symbol(bottom[start-1]):

        add_to_gears_list([row_index+1, (start-1), concat(num_indices, row)])
    if is_gear_symbol(top[end+1]):

        add_to_gears_list([row_index-1, (end+1), concat(num_indices, row)])
    if is_gear_symbol(bottom[end+1]):
        add_to_gears_list([row_index+1, (end+1), concat(num_indices, row)])


    for i in range(start, end+1):
        if is_gear_symbol(top[i]):
            add_to_gears_list([row_index-1, i, concat(num_indices, row)])

        if is_gear_symbol(bottom[i]):
            add_to_gears_list([row_index+1, i, concat(num_indices, row)])

def add_to_gears_list(gear):
    for row in gears_list:
        if gear[0] == row[0] and gear[1] ==  row[1]:
            if gear[2] not in row[2:]:
                row.append(gear[2])
                return
            else:
                continue
    gears_list.append(gear)            

    return

file_list = open("input.txt").readlines()
file_list = padding(file_list)

i = 0
sum = 0

for row in file_list:
    congruent_nums = find_congruent_nums(row)
    for num in congruent_nums:
        if check_adjacent(num, row, file_list[i-1], file_list[i+1]):
            sum += concat(num, row)
        
        # Pt 2
            print(check_adjacent_gears(num, row, file_list[i-1], file_list[i+1],i))
            print(gears_list)
    i+=1

# Pt 2
sum_ratios = 0

for gear in gears_list:
    ratio = 1
    if len(gear) == 4:
        for part in gear[2:]:
            ratio *= part
        sum_ratios += ratio
print(sum_ratios)