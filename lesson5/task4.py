new_list = ["один", "два", "три", "четыре"]
with open("obj_4.txt") as f_obj, open("new_obj.txt", 'w') as n_obj:
    c = 0
    for line in f_obj:
        list = line.split()
        list[0] = new_list[c]
        c += 1
        n_obj.write(' '.join(list))
        n_obj.write(f'\n')

