nest_1 = [1, 2]
nest_2 = [3, 4]

#nest_1.extend(nest_2)
#print(nest_1)

#flatten

nest_4 = [[1, 2],[3, 4]]
nest_5=[]
for x in nest_4:
    nest_5 = nest_5 + x

print(nest_5)