
list1 = [1,5,6,6,2,1,2,8]

uniq_list = list(set(list1))

print(uniq_list)

list2 = []

for num in list1:
    if num not in list2:
        list2.append(num)

print(list2)
list2.reverse()
print(list2)
print(list2[::-1])

