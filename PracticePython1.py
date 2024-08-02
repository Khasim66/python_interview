# s='403900'
# l=[]
# z=[x for x in s if x=='0']
# nz=[x for x in s if x!='0']
# print("".join(z+nz))
#
# for x in range(len(s)):
#     if s[x] == '0':
#         l.append(s[x-1])
# print(l)


# s = "ertytuintg"
# i=[]
#
# for x in range(len(s)):
#     if s[x] =='t':
#         i.append(s[x-1])
# print("".join(i))

a = {1: "khasim", 2: "shaik", 3: "akhil"}
#
# for x in a.values():
#     if 's' in x:
#         print(x)
for x,y in a.items():
    if 's' in y:
        print(y)

s = "ertytuintg"
a=[]
for x in range(len(s)):
    if s[x]=='t':
        print(s[x-1],end="")

