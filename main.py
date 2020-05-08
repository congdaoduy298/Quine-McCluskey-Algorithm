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

print("How many variables you want to use ?")
n = int(input())

# Create dictionary exp2 
results = Solution()
results.dict_exp2(n-1)
print(results.exp2)
print("List number ... ")
a = list(map(int, input().split()))

list_str = []
for i in a:
    list_str.append({(i, ):results.convert_to_binary(i, n)})

len_list = len(list_str)
current_list =  copy.deepcopy(list_str)
done = False 
step_i = 0

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
    for i in range(len(current_list)):
        if not flag[i]:
            new_list.append(current_list[i])

    if new_list != []:
        current_list = copy.deepcopy(new_list)
        print(f'Step {step_i}:')
        for d in current_list:
            print(list(d.keys())[0], ''.join(list(d.values())[0]))


current_len = len(current_list)

count_results = np.zeros((current_len, len_list), dtype=int)

for i, current_dict in enumerate(current_list):
    for key in list(current_dict.keys())[0]:
        count_results[i, a.index(key)] = 1

# create a list save index of row if column just has 1 
# and handle the case i = 0
index_list = [0 if j == 1 else -1 for i, j in enumerate(count_results[0])]

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


out_dict = {}
for i in index_list:
    if i != -1:
        out_dict[i] = list(current_list[i].values())[0]

# print(out_dict)

ascii_letters = string.ascii_letters

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

print(f' Final Result : Y = {y}')





