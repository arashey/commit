numbers = [12, 34, 82, 12, 66, 34]
mx_num = 0
list = []
dic = {}
for i in numbers:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1


mx_num = max(dic.values())
for i in dic.keys():
    if dic[i] == mx_num:
        list.append(i)
print(list)