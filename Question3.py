grocery_items = 'Grated Cheese, Coffee Powder, Pickles, White Chocolate, Dark Chocolate, Eggs, Breads, Milk, Sugar, Salt, Cat Food, Fries'
my_list=grocery_items.split(', ')
my_list.sort()
n=', '.join(sorted(my_list))
print(n)