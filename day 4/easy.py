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
search_str = "XMAS"
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
        if val == "X":
            # go through all 8 directions
            
            # top and bottom row
            for x in [-1,1]:
                for y in [-1,0,1]:
                    if array2d[line_index+x][char_index+y] == "M" and \
                        array2d[line_index+x*2][char_index+y*2] == "A" and \
                        array2d[line_index+x*3][char_index+y*3] == "S":
                            sum += 1

            # left and right
            for x in [0]:
                for y in [-1,1]:
                    if array2d[line_index+x][char_index+y] == "M" and \
                        array2d[line_index+x*2][char_index+y*2] == "A" and \
                        array2d[line_index+x*3][char_index+y*3] == "S":
                            sum += 1

print(sum)
    