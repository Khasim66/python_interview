# s="abcbadbcefg"
# d=[]
# u=[]
# for x in s:
#     if x not in d:
#         d.append(x)
#     else:
#         u.append(x)
#
# print("".join(d))
# print("".join(u))



 #pattern
"""

1
11
111
1111

1
12
123
1234
12345
"""
# for x in range(6):
#     print('1'* x)
# print()
#
# for x in range(6):
#     for y in range(1,x+1):
#         print(y,end="")
#     print()


# a='khasim@gmail.com'
# s=a.split(".")
# print(s[-1])


# from functools import reduce
# l=[2,3,4,5,6]
# m=reduce(lambda x,y : x+y,l)
# print(m)


# n=[2,3,4,5,6]
# m=[x+y for x,y in zip(l,n)]
# print(m)


# b=map(lambda x,y: x+y , l,n)
# print(list(b))


#
# L = ['abc', 'xyz', 'aba', '1221']
# a=[]
# n=[]
# c=0
# cn=0
# for x in L:
#     if x.isalpha():
#         a.append(x)
#         c+=1
#     else:
#         n.append(x)
#         cn+=1
# print(a)
# print(c)
# print(n)
# print(cn)


# l=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# s=sorted(l,key=lambda x:x[1])
# print(s)


#
# a=[2,3,2,3,4,5,6]
# b=a.copy()
# print(b)
# for x in a:
#     if x not in b:
#         b.append(x)
# print(b)


# 1
# 22
# 333
# 4444
# for x in range(5):
#     for y in range(x):
#         print(x,end="")
#     print()


# 1
# 12
# 123
# 1234
# for x in range(5):
#     for y in range(1,x+1):
#         print(y,end="")
#     print()

# for x in range(10,1,-1):
#     for y in range(1,x-1):
#         print(y,end="")
#     print()

#
# from datetime import datetime
# print("Current date and time:", datetime.now())
# formatted_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
# print("Formatted date and time:", formatted_datetime)


# a, b = 0, 1
# for x in range(10):
#     print(a, end=' ')
#     a, b = b, a + b
#




# List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # #removing the 0th, 4th and 5th elements
# r=[0,4,5]
# l=[List[x] for x in range(len(List)) if x not in r]
# #l=[List[x] for x in range(len(List)) if x not in r]
# print(l)


# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
#
# l=[x for x in list1 if x not in list2]
# print(l)


# list1 = [1, 2, 3, 4, 5]
# print(list1.index(3))

#Write a Python program to select an item randomly from a list.
import random

# l=[2,3,4,5,6]
# print(random.choice(l))
#
l=[2,5,2,9,5,23]
s=list(set(l))
s.sort()
print(l)

# main_list = [3, 4, 5, 6, 7, 8, 9]
# sublist = [4, 5, 6]
#
# if any(main_list[i:i+len(sublist)] == sublist for i in range(len(main_list) - len(sublist) + 1)):
#     print("main_list contains sublist")
# else:
#     print("main_list does not contain sublist")


# from datetime import datetime
# now=datetime.now()
# t12h = now.strftime("%I:%M%p") #24 ("%H : %M")
# t24hr = now.strftime("%H:%M")   #12 ("%I : %M%p")
# print(t12h)
# print(t24hr)
#

