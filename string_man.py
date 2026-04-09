from asyncio import print_call_graph


str = "automation"

#Reverse a string without slicing
list_str = list(str)
list_str.reverse()
new_str = ""
for char in list_str:
    new_str = new_str +"".join(char) 
print(new_str)

#Find second largest number
list_num = [2,5,6, 10,8,3]
list_num.sort(reverse=True)
print(list_num[1])

#Find missing number in list
numbers = [1, 2, 3, 55, 6, 70]
max_value = max(numbers)
missing_numbers=[]
for x in range(1,max_value):
    if x not in numbers:
        missing_numbers.append(x)
print(missing_numbers)

#Merge two sorted lists
list_1 = [[1,2,3], [4,5]]

merged_list = []
merged_list.extend(list_1)
print(merged_list)

#Find intersection of two lists

int_list_1 = [1,2,3]
int_list_2 = [1,2,5]

list_3 = list(set (int_list_1).intersection(set(int_list_2)))
print(list_3)
