import json
firm_profit = {}
with open("obj_7.txt") as f_obj:
    avg_profit = 0
    c = 0
    for line in f_obj:
        list = line.split()
        firm_profit[list[0]] = int(list[-2]) - int(list[-1])
        if firm_profit[list[0]] > 0:
            avg_profit += firm_profit[list[0]]
            c += 1
    firm_profit['average_profit'] = round(avg_profit/c,2)
    print(firm_profit)
with open("my_file.json", "w") as write_f:
    json.dump(firm_profit, write_f)