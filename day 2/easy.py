import math
input_txt_path = r'day 2\input.txt'

input_txt = ""
with open(input_txt_path) as f:
    input_txt = f.read()
    
# problem
# input is a list of lines seperated by numbers
# return a line if
#   line is all increasing or decreasing
#   AND the increases/decreases between each number is >= 1 and <= 3
# give number of passing lines
ret_lines = []

lines = input_txt.split("\n")
for line in lines:
    nums = list(map(int, line.split(" ")))
    # increasing or decreasing
    if nums == sorted(nums) or nums == sorted(nums, reverse= True):
        is_proper_inc = True
        for index,val in enumerate(nums[:-1]):
            diff = abs(nums[index+1]-nums[index])
            # line fails if outside the bounds 
            if diff < 1 or diff > 3:
                is_proper_inc = False
        if is_proper_inc:
            ret_lines.append(line)
            
print(len(ret_lines))