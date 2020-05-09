import numpy as np 
import string 
import copy 

class Solution(object):

    def convert_to_binary(self, value, n):
        str_binary = n * ['0']
        for i in reversed(range(n)):
            # print(i)
            if value >= self.exp2[i]:
                # print(i, value, self.exp2[i])
                value = value - self.exp2[i]
                str_binary[n - i - 1] = '1'
        return str_binary
            

    def dict_exp2(self, max_bit=32):
        tmp = 1
        self.exp2 = {}
        self.exp2[0] = 1 
        for i in range(1, max_bit + 1):
            self.exp2[i] = tmp*2
            tmp = tmp*2
    
def num_of_different(a, b):
    count = 0
    index = 0
    for i in range(len(a)):
        if a[i]!=b[i]: 
            count += 1
            index = i
    return count, index


def update_dict(current_list, out_dict, a, index_list, i):
    for j in current_list:
        for key in list(j.keys())[0]:
            if a[i] == key:
                out_dict.update(j) 
                index_list[i] = -2
                return out_dict, index_list
    return out_dict, index_list

# Create dictionary exp2 
def utils(n, a, checked):

    results = Solution()
    results.dict_exp2(n-1)

    list_str = []
    for i in a:
        list_str.append({(i, ):results.convert_to_binary(i, n)})
    len_list = len(list_str)
    current_list =  copy.deepcopy(list_str)
    done = False 
    step_i = 0
    message = ""

    while not done:
        done = True 
        new_list = []
        step_i += 1
        len_cur_list = len(current_list)
        flag = np.zeros_like(current_list)

        for i in range(0, len_cur_list-1):
            for j in range(i+1, len_cur_list):

                # print(list(current_list[i].keys())[0], list(current_list[i].keys())[0])
                count, index =  num_of_different(list(current_list[i].values())[0], list(current_list[j].values())[0])
                if count == 1:
                    done = False 
                    # prevent list share memory with other list 
                    value = copy.deepcopy(list(current_list[i].values())[0])
                    value[index] = '-'
                    key = list(current_list[i].keys())[0] + list(current_list[j].keys())[0]
                    new_dict ={tuple(sorted(key)):value}
                    if new_dict not in new_list:
                        new_list.append(new_dict)
                    flag[i], flag[j] = 1, 1

        # append key of dict not join with other one.
        # If nothing is True, the step before is the final step
        if True in flag:
            for i in range(len(current_list)):
                if not flag[i]:
                    new_list.append(current_list[i])

        if new_list != []:
            current_list = copy.deepcopy(new_list)
            message += f'\nStep {step_i}:\n'
            for d in current_list:
                message += f"{list(d.keys())[0]}, {''.join(list(d.values())[0])}\n"
            # print(message)


    current_len = len(current_list)

    count_results = np.zeros((current_len, len_list), dtype=int)

    for i, current_dict in enumerate(current_list):
        for key in list(current_dict.keys())[0]:
            count_results[i, a.index(key)] = 1

    # create a list save index of row if column just has 1 
    # and handle the case i = 0
    index_list = [0 if j == 1 else -1 for i, j in enumerate(count_results[0])]

    # count number 1 on column 
    for i in range(1, count_results.shape[0]):
        for j in range(count_results.shape[1]):
            if count_results[i, j] == 0:
                count_results[i, j] = count_results[i-1, j]
            else:
                count_results[i, j] = count_results[i-1, j] + count_results[i, j] 
                if count_results[i, j] == 1:
                    index_list[j] = i 
                else:
                    index_list[j] = -1

    # print(count_results)
    # print(index_list)

    out_dict = {}
    # must mask all column 
    mask_all = False 
    while not mask_all:
        mask_all = True
        for i in index_list:
            if i > -1:
                out_dict[i] = list(current_list[i].values())[0]
                for key in list(current_list[i].keys())[0]:
                    # -2 ~ used column
                    index_list[a.index(key)] = -2

        for i in range(len(index_list)):
            if index_list[i] != -2:
                mask_all = False
                out_dict, index_list = update_dict(current_list, out_dict, a, index_list, i)
                

    ascii_letters = string.ascii_letters

    if checked == 1:
        y = ''
        for key, list_char in out_dict.items():
            for i, char_i in enumerate(list_char):
                if char_i == '0':
                    list_char[i] = ascii_letters[i]
                elif char_i == '1':
                    list_char[i] = ascii_letters[i+26]
                else:
                    list_char[i] = ''
            y += ''.join(list_char) + '+'
        y = y[:-1]
    else:
        y = ''
        for key, list_char in out_dict.items():
            # print(list_char)
            for i, char_i in enumerate(list_char):
                if char_i == '0':
                    list_char[i] = ascii_letters[i+26]
                elif char_i == '1':
                    list_char[i] = ascii_letters[i]
                else:
                    list_char[i] = ''
            # drop '' value 
            tmp_list = [i for i in list_char if i!='']
            y += '(' + '+'.join(tmp_list) + ').'
        y = y[:-1]
    # print(checked)
    message += f'\nFinal Result : Y = {y}\n'
    message += '\nCheck it yourself ... ^-^ No one and Nothing is perfect'
    # print(message)

    return message




