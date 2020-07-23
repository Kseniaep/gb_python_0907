my_list = [10, 35, 30, 15, 50]
print(my_list)
new_list = [my_list[el] for el in range(1,len(my_list)) if my_list[el-1] < my_list[el]]
print(new_list)