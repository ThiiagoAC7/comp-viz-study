import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def get_nums_of_X(char_grid, num_grid):
    '''
    Gets line and col numbers of 'X' values
    for each combination of line and col, append to 
    number sequence
    '''
    char_arr = np.asarray(char_grid)
    num_arr = np.asarray(num_grid)

    _line, _col = np.where(char_arr == 'X')


    num_sequence = []
    for i in range(len(_line)):
        # print(f'{_line[i]}, {_col[i]}')
        # print(f'nums -> {num_grid[_line[i]][_col[i]]}')
        num_sequence.append(num_grid[_line[i]][_col[i]])

    return num_sequence

def check_sequence_neg_pos(num_sequence):
    '''
    Validating sequence if is +,-,+,-,+,...
    considering each number as 1 or -1, 
        if current sum is greater than 2 or less than -2
        sequence is on the wrong order
    '''
    curr_sum = 0 
    result = True

    for i in num_sequence:
        if result:
            _aux = -1
            if (i > 0):
                _aux = 1
            curr_sum = curr_sum+ _aux 
            if (curr_sum > 1 or curr_sum < -1):
                result = False

    return result


def main():
    height, width = [int(i) for i in input().split()]

    num_grid = []
    char_grid = []

    for i in range(height):
        line = input()
        num_grid.append([])
        for x in line.split(' '):
            if x != '':
                num_grid[i].append(int(x))

    for i in range(height):
        line = input()
        char_grid.append(line.replace('\r','').split(' '))


    num_sequence = get_nums_of_X(char_grid, num_grid)
    result = check_sequence_neg_pos(num_sequence)
    if result:
        print('true')
    else:
        print('false')

main()
