#set merge
set1= {1,2,3}
set2= {1,2,4}
set3 = {*set1,*set2}
print(set3)

#list merge
list1= [1,2,3]
list2= [1,2,4]
list3 = [*list1,*list2]
print(list3)

#tuple merge
tuple1= (1,2,3)
tuple2= (1,2,4)
tuple3 = (*list1,*list2)
print(tuple3)


#dict merge
dict1= {"name":"nareshk"}
dict2= {"age":30}
dict3 = {**dict1,**dict2}
print(dict3)

