list = [str(el) for el in range(20, 101) if el % 10 == 0]
with open("obj_5.txt", "w+") as n_obj:
    n_obj.write(' '.join(list))
    n_obj.seek(0)
    content = n_obj.read()
    print(content)
    new_list = content.split()
    print(sum(map(int,new_list)))

