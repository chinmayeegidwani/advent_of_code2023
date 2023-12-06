from collections import defaultdict
import sys

def get_mapping(map_name, seed):
    curr_map = M[map_name]
    for range in curr_map:
        dest = range[0]
        source = range[1]
        size = range[2]
        if source <= seed < source + size:
            return dest-source+seed
    return seed

with open("input.txt") as fd:
    file_list = fd.readlines()

seed_s = file_list[0][7:]
seeds = map(int, seed_s.split(' '))

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

min_loc = sys.maxsize

for seed in seeds:
    seed_to_soil = get_mapping("seed-to-soil", seed)
    print(str(seed_to_soil))
    soil_to_fert = get_mapping("soil-to-fertilizer", seed_to_soil)
    print(str(soil_to_fert))
    fert_to_water = get_mapping("fertilizer-to-water", soil_to_fert)
    water_to_light = get_mapping("water-to-light", fert_to_water)
    light_to_temp = get_mapping("light-to-temperature", water_to_light)
    temp_to_humidity = get_mapping("temperature-to-humidity", light_to_temp)
    humidity_to_loc = get_mapping("humidity-to-location", temp_to_humidity)
    print(str(humidity_to_loc) + "\n")
    if humidity_to_loc < min_loc:
        min_loc = humidity_to_loc

print(min_loc)


