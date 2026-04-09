x = (1,[2,3],{"hello","world"},7)

#Tuples are Immutable and so data cannot be changed - However, we can still modify objects that are mutable in nature
x[1].append("Hello")
print(x)
x[1].append([2,3])
print(x)
x[2].add("new set")
print(x)
