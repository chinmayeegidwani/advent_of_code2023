def func(distances, times):
    res = 1
    for j, game in enumerate(times):
        count = 0
        for i in range(0, game):
            speed = i
            time_moving = game - i
            game_dist = time_moving * speed
            if game_dist > distances[j]:
                count +=1
        print(count)
        res *= count
    return res


with open("input.txt") as fd:
    file_list = fd.readlines()

times = list(map(int, file_list[0][5:-1].strip().split()))
distances = list(map(int, file_list[1][9:].strip().split()))

# Pt 1
res = func(distances, times)
print(res)

# Pt 2
times_ = int(file_list[0][5:].strip("\n").replace(" ", ""))
times_2 = []
times_2.append(times_)
dists_ = int(file_list[1][9:].strip("\n").replace(" ", ""))
distances_2 = []
distances_2.append(dists_)

res2 = func(distances_2,times_2)
print(res2)