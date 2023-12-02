file_list = open("input_0.txt").readlines()

line_digits = []

global_sum = 0
for word in file_list:
    word = word.replace("one", "one1one").replace("two","two2two").replace("three", "three3three").replace("four", "four4four").replace("five","five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight","eight8eight").replace("nine", "nine9nine").replace("ten", "ten10ten").replace("eleven", "eleven11eleven").replace("twelve", "twelve12twelve").replace("thirteen", "thirteen13thirteen").replace("fourteen", "fourteen14fourteen").replace("fifteen", "fifteen15fifteen").replace("sixteen", "sixteen16sixteen").replace("seventeen", "seventeen17seventeen").replace("eighteen", "eighteen18eighteen").replace("nineteen", "nineteen19nineteen")
    print(word)
    line_digits = []

    for character in word:
        if character.isdigit():
            line_digits.append(int(character))
    line_cal_val = str(line_digits[0]) + str(line_digits[-1]) # '27'
    global_sum += int(line_cal_val)

print(global_sum)


            
