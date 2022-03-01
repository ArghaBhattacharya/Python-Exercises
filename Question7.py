stock_market = {'AXIS BANK':7, 'BHARTI AIRTEL':5, 'COAL INDIA':10, 'ITC':1, 'TCS':3, 'L&T':2, 'RELIANCE':9, 'KOTAK BANK':8, 'AMERICAN EXPRESS':11}
my_dict_key=[]
my_dict_value=[]
value_list=sorted(stock_market.values())
for i in range(len(value_list)):
    for key,value in stock_market.items():
        if value==value_list[i]:
            my_dict_key.append(key)
            my_dict_value.append(value)
my_dict=list(zip(my_dict_key,my_dict_value))
print(my_dict[0])
print(my_dict[len(my_dict)-1])
print(my_dict)