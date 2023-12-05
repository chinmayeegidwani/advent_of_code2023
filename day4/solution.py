import re
def find_common_cards(winning, owned):
    return set(winning) & set(owned)

def get_points(num_matches):
    sum = 0
    for i in range(num_matches):
        if i == 0:
            sum += 1
        else:
            sum = sum*2
    return sum

file_list = open("input.txt").readlines()
pattern = r'\b\d+\s*:\s*([^|]+)\s*\|\s*([^|]+)\b'
winning_cards = []
owned_cards = []
scratchcards = [1]*len(file_list)


for i, line in enumerate(file_list):
    cards = re.search(pattern, line)
    winning_cards.append(cards.group(1).split())
    owned_cards.append(cards.group(2).split())


matches = 1
sum = 0
for i, card in enumerate(owned_cards):
    matches = len(find_common_cards(winning_cards[i], card))
    sum += get_points(matches)
    #  Pt 2
    for k in range(scratchcards[i]):
        for j in range(matches):
            scratchcards[i+j+1] += 1
        
# Pt 2
scratch_sum  = 0
for i, val in enumerate(scratchcards):
    scratch_sum += val


# Pt 1
print(sum)
# Pt 2
print(scratch_sum)

        


