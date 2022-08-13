import cv2
import numpy as np


def basic_position_filter(previous_position, current_position, line):
    """
    Input : previouse position , current position [X,Y] and line (Thredhold)
            Position data form is array
    Output : How many objects pass the line 

    Idea : compare the both of position values and make pairs with cloest value by using abs value 
    """

    prev_position = np.array(previous_position)
    curr_position = np.array(current_position)
    line = line

    if len(curr_position) != len(previous_position):
        return 0
    elif curr_position.size == 0 or prev_position.size == 0:
        return 0
    sum_pre = np.sum(prev_position, axis=1)
    sum_cur = np.sum(curr_position, axis=1)
    pair = []
    for i in range(len(sum_pre)):
        ii, zz = 0, 0
        v = 10000
        pre_v = sum_pre[i]
        for z in range(len(sum_cur)):
            cur_v = sum_cur[z]
            distance = abs(pre_v - cur_v)
            if distance < v:
                v = distance
                ii = i
                zz = z
        pair.append([prev_position[ii][1], curr_position[zz][1]])

    count = 0
    # pair => y position of each person
    for i in range(len(pair)):
        y_prev = pair[i][0]
        y_cur = pair[i][1]

        if y_prev > line and y_cur < line:
            count += 1

    return count

    # line = 360
    # invisible_line = 340

    # if prev_position.size > 0 and len(current_position) > 0:

    #     prev_position_b = prev_position < line
    #     curr_position_b = curr_position < invisible_line

    #     num_pre = prev_position_b[prev_position_b == False].shape[0]
    #     num_cur = curr_position_b[curr_position_b == False].shape[0]
    #     count = curr_position_b[curr_position_b == True].shape[0]

    #     return count
    # elif len(curr_position) > len(prev_position):
    #     return 0
    # else:
    #     return 0
