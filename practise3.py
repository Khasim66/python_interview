# l=[2,4,5,6,12]
# l2=['GB','MB','GB','KB','MB']
# l3=[(x,y) for x,y in zip(l,l2)]
# print(l3)
# max_tuple = max(l3, key=lambda tup: tup[0])
# print(max_tuple)

# l = [2, 4, 5, 6, 12]
# l2 = ['GB', 'MB', 'GB', 'KB', 'GB']
# unit_size = {'GB': 1024 * 1024 * 1024, 'MB': 1024 * 1024, 'KB': 1024}
# p=[(x * unit_size[y],x,y)for x,y in zip(l,l2)]
# max=max(p,key=lambda x:x[0])
# print(max)

#l4= [(x * unit_size[y],x,y) for x,y in zip(l,l2)]
#l3 = [(x * unit_size[y], x,y) for x, y in zip(l, l2)]
#print("List of tuples with converted sizes:")
# for item in l3:
#     print(item)
# max_tuple = max(l3, key=lambda tup: tup[0])
# print(max_tuple)

#
# l2 = {2: 'GB', 12: 'GB', 4: 'GB', 5: 'KB', 3: 'GB'}
# size_in_bytes = {'GB': 1024 * 1024 * 1024, 'MB': 1024 * 1024, 'KB': 1024}
# def convert_to_bytes(size, unit):
#     return size * size_in_bytes[unit]
# max_key = max(l2, key=lambda k: convert_to_bytes(k, l2[k]))
#
# print("Key with maximum value based on size order:", max_key)
# print(f"{max_key}:", l2[max_key])


# l = {6:'B',4:'C',3:'A'}
# s=sorted(l.items(),key=lambda x : x[1])
# for x,y in s:
#     print(x,y)

# l=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# s=max(l,key=sorted)
# print("hal",s)
#

# l=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# s=sorted(l,key=lambda x: x[1])
# print(s)


# Import the 'collections' module, which provides specialized container data types
# import collections
# my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
# print("Original List : ", my_list)
# c= collections.Counter(my_list)
# print(c)
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# print(set(color1) & set(color2))

# num = [[1, 2, 83], [4, 15, 6], [10, 11, 12], [7, 8, 879]]
# print(max(num, key=sum))


list1 = [220, 330, 500]
list2 = [12, 17, 21]
g=[x for x in list1 if x>=200]
print(g)

k=(x >= 200 for x in list1)
print(k)
print(all(x >= 200 for x in list1))
print(all(x >= 25 for x in list2))


# list = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# c = 'c'
# result = [x for x in list if x.endswith(c)]
# print(result)



# nested_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# flattened_list = []
#
# stack = nested_list.copy()
#
# while stack:
#     item = stack.pop(0)
#     if isinstance(item, list):
#         stack = item + stack
#     else:
#         flattened_list.append(item)
#
# print(flattened_list)

# from collections import Counter
# x="python online compiler"
# count=Counter(x)
# print(count)
























