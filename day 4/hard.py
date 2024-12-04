import math
input_txt_path = r'day 4\input.txt'
# input_txt_path = r'day 4\easyinput.txt'

input_txt = ""
with open(input_txt_path) as f:
    input_txt = f.read()
    
# problem
# 2d array of text
# find all iterations of xmas going in all 8 directions
# usual trick with 2d search array is pad the edges with the length of the word to search
# hard
# in the shape of an x, and A in the center, top left and bottom need to be either M or S. Then the same for other diagonal
search_str = "MAS"
null_char = "O"

lines = input_txt.split("\n")
width = len(lines[0])
height = len(lines)
pad_len = len(search_str)-1

# build 2d array
array2d = []
for line in lines:
    arr = []
    for char in line:
        arr.append(char)
    arr = [null_char]*pad_len + arr + [null_char]*pad_len
    array2d.append(arr)
    
pad_line = [null_char]*pad_len + [null_char]*width + [null_char]*pad_len
array2d = [pad_line]*pad_len + array2d + [pad_line]*pad_len

# for line in array2d:
#     print(line)
# ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
# ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
# ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
# ['O', 'O', 'O', 'X', 'M', 'A', 'S', 'O', 'O', 'O']
# ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
# ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
# ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']


# [-1, 1] [0 ,1] [1, 1]
# [-1, 0]        [1, 0]
# [-1,-1] [0,-1] [1,-1]

sum = 0

for line_index,line in enumerate(array2d):
    for char_index,val in enumerate(line):
        if val == "A":
            # go both diagonals
            
            left_diag_bool = False
            right_diag_bool = False
            
            # left diag
            if (array2d[line_index-1][char_index+1] == "M" and\
               array2d[line_index+1][char_index-1] == "S")\
                   or\
                (array2d[line_index-1][char_index+1] == "S" and\
               array2d[line_index+1][char_index-1] == "M"):
                    left_diag_bool = True
            
            # right diag
            if (array2d[line_index+1][char_index+1] == "M" and\
               array2d[line_index-1][char_index-1] == "S")\
                   or\
                (array2d[line_index+1][char_index+1] == "S" and\
               array2d[line_index-1][char_index-1] == "M"):
                    right_diag_bool = True
            if right_diag_bool and left_diag_bool:
                sum += 1

print(sum)
    