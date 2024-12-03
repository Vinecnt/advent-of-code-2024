import math
input_txt_path = r'day 1\easy_input.txt'

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

sum = 0
for val1,val2 in zip(left_list, right_list):
    print(val1, val2)
    sum += abs(int(val1)-int(val2))
    
print(sum)

    
    