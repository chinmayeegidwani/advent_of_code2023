from collections import defaultdict
import sys

def get_mapping(map_name, seed):
    curr_map = M[map_name]
    for range in curr_map:
        dest = range[0]
        source = range[1]
        size = range[2]
        if dest <= seed < dest + size:
            return source + seed - dest
    return seed

def transform_seeds(seeds):
    min_loc = sys.maxsize
    for seed in seeds:
        seed_to_soil = get_mapping("seed-to-soil", seed)
        soil_to_fert = get_mapping("soil-to-fertilizer", seed_to_soil)
        fert_to_water = get_mapping("fertilizer-to-water", soil_to_fert)
        water_to_light = get_mapping("water-to-light", fert_to_water)
        light_to_temp = get_mapping("light-to-temperature", water_to_light)
        temp_to_humidity = get_mapping("temperature-to-humidity", light_to_temp)
        humidity_to_loc = get_mapping("humidity-to-location", temp_to_humidity)
        if humidity_to_loc < min_loc:
            min_loc = humidity_to_loc
    return min_loc

def check_valid_seed(target_seed, seeds):
    for i in range(len(seeds)-1):
        if i%2 == 1:
            continue
        start = seeds[i]
        end = seeds[i+1] + start
        if start <= target_seed < end:
            return True
    return False

def transform_backwards(seeds):
    for i in range(0, sys.maxsize):
        humidity_to_loc = get_mapping("humidity-to-location", i)
        temp_to_humidity = get_mapping("temperature-to-humidity", humidity_to_loc)
        light_to_temp = get_mapping("light-to-temperature", temp_to_humidity)
        water_to_light = get_mapping("water-to-light", light_to_temp)
        fert_to_water = get_mapping("fertilizer-to-water", water_to_light)
        soil_to_fert = get_mapping("soil-to-fertilizer", fert_to_water)
        seed = get_mapping("seed-to-soil", soil_to_fert)
        if check_valid_seed(seed, seeds):
            return i

with open("input.txt") as fd:
    file_list = fd.readlines()

seed_s = file_list[0][7:]
seeds = list(map(int, seed_s.split(' ')))

M = defaultdict() # dict of map_name: [values]

flag = True
map_name = ""
for c in file_list[2:]:
    if c == "\n":
        flag = True
        continue
    if flag:
        map_name = c[:-6]
        M[map_name] = []
        flag = False
        continue 

    source, dest, size = c.split()
    M[map_name].append([int(source), int(dest), int(size)])


# Pt 1
min_loc = transform_seeds(seeds)
print(min_loc)

#Pt 2
min_loc_2 = transform_backwards(seeds)
print(min_loc_2)





