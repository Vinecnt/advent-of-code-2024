import math
input_txt_path = r'day 1\input.txt'

input_txt = ""
with open(input_txt_path) as f:
    input_txt = f.read()
    
left_list = []
right_list = []    
for line in input_txt.split("\n"):
    left_list.append(line.split("   ")[0])
    right_list.append(line.split("   ")[1])
    
left_list.sort()
right_list.sort()


population_dict = dict.fromkeys(range(0,10**6), 0)

# create a dict where key is the number, and value is how many times 
for elem in right_list:
    population_dict[int(elem)] += 1
    
sum = 0
for elem in left_list:
    sum += int(elem) * population_dict[int(elem)] 
    
print(sum)

    
    