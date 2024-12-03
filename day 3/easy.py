import math
input_txt_path = r'day 3\input.txt'
# input_txt_path = r'day 3\easyinput.txt'

input_txt = ""
with open(input_txt_path) as f:
    input_txt = f.read()
    
# problem
# need to build a parser to build 
# specify the grammar
# mul(\d+,\d+)

sum = 0

def find_mul(input_str:str) -> str:
    global sum
    # mul(123,123)
    mul_search_str = "mul"
    mul_index = input_str.find("mul")
    if mul_index == -1:
        print("no more mul")
    else:
        input_str = input_str[len(mul_search_str)+mul_index:]
        #(123,123)
        
        if input_str[0] != "(":
            return find_mul(input_str)
        input_str = input_str[1:]
        #123,123)
        
        right_paren_index = input_str.find(")")
        if right_paren_index == -1:
            return find_mul(input_str)
        
        nums_txt = input_str[:right_paren_index]
        #123,123
        
        if len(nums_txt.split(",")) != 2:
            return find_mul(input_str)
        
        left_num_str = nums_txt.split(",")[0]
        right_num_str = nums_txt.split(",")[1]
        if str.isdigit(left_num_str) is False or str.isdigit(right_num_str) is False:
            return find_mul(input_str)
        
        sum += int(left_num_str) * int(right_num_str)
        
        return find_mul(input_str[right_paren_index+1:])


find_mul(input_txt)
print(sum)