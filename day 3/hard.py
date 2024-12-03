import math
# input_txt_path = r'day 3\hardtestinput.txt'
input_txt_path = r'day 3\input.txt'
# input_txt_path = r'day 3\easyinput.txt'

input_txt = ""
with open(input_txt_path) as f:
    input_txt = f.read()
    
# problem
# need to build a parser to build 
# specify the grammar
# mul(\d+,\d+)
# hard problem
# same as before but also search for do() and don't() to enable disable parsing
# if enable_mul == True
#   look for both next mul and don't()
#   if mul index less than don't index, then proceed
#   else 
#       enable_mul = False
#       find_mul(input_str[index of don't()+1:])
# if enable_mul == False:
#   look for the next do()
#   if next_do != -1:
#       find_mul(input_str[index of do()+1:])
#   else:
#       no more muls
#    

sum = 0

def find_mul(input_str:str, enable_mul: bool) -> str:
    global sum
    mul_search_str = "mul"
    dont_search_str = "don't()"
    if enable_mul == True:
        mul_index = input_str.find(mul_search_str)
        dont_index = input_str.find(dont_search_str)
        if mul_index < dont_index or dont_index == -1:
            pass
        else:
            enable_mul = False
            return find_mul(input_str[dont_index+len(dont_search_str):],enable_mul)
    elif enable_mul == False:
        do_search_str = "do()"
        do_index = input_str.find(do_search_str)
        if do_index == -1:
            return ("no more mul")
        else:
            enable_mul = True
            return find_mul(input_str[do_index+len(do_search_str):], enable_mul)
    
    # mul(123,123)
    mul_index = input_str.find(mul_search_str)
    if mul_index == -1:
        return ("no more mul")
    else:
        input_str = input_str[len(mul_search_str)+mul_index:]
        #(123,123)
        
        if input_str[0] != "(":
            return find_mul(input_str,enable_mul)
        input_str = input_str[1:]
        #123,123)
        
        right_paren_index = input_str.find(")")
        if right_paren_index == -1:
            return find_mul(input_str,enable_mul)
        
        nums_txt = input_str[:right_paren_index]
        #123,123
        
        if len(nums_txt.split(",")) != 2:
            return find_mul(input_str,enable_mul)
        
        left_num_str = nums_txt.split(",")[0]
        right_num_str = nums_txt.split(",")[1]
        if str.isdigit(left_num_str) is False or str.isdigit(right_num_str) is False:
            return find_mul(input_str,enable_mul)
        
        sum += int(left_num_str) * int(right_num_str)
        
        return find_mul(input_str[right_paren_index+1:],enable_mul)


find_mul(input_txt,enable_mul=True)
print(sum)