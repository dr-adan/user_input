my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After append:",my_list)
my_list.insert(1, 15)
# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extend:",my_list)
my_list.pop()
print(my_list)
my_list.sort()
index_of_30 = my_list.index(30)
print("Index of 30 in my_list:", index_of_30)
print("Modified my_list:", my_list)