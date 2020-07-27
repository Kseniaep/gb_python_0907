import re

def sum_string(my_str):
    sum_str = 0
    nums = re.findall(r'\d+', my_str)
    nums = [int(i) for i in nums]
    return sum(nums)

subject = {}
with open("obj_6.txt") as f_obj:
    c = 0
    for line in f_obj:
        list = line.split(':')
        subject[list[0]] = sum_string(list[1])
    print(subject)