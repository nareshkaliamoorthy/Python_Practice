set_1 = {2,37,78,9,4,45,11}
set_2 = {2,37,78,9,4,45,11, 9,65,77}
set_1.remove(37) # Throws Key error when the given is not found
set_1.discard(370) # doesn't throw Key error when the given is not found
set_1.discard(78)

print(set_1.union(set_2))
print(set_1.intersection(set_2))

set_1.pop()
print(set_1)
set_2.add("hello")
print(set_2)
set_2.add((0,8))
print(set_2)


