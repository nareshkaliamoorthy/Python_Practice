from functools import reduce


list1 = [1,2,3,4,5]
str= "hello"

dict1 = dict.fromkeys(list1,"hello")
print(dict1)
dict1.pop(1)
print(dict1)

print(max(list1))

even = list(filter(lambda x: x % 2==0,list1))
print(even)

sum = reduce(lambda x,y:x+y,list1)
print(sum)

print(hash(str))

char = 65

print(chr(char))

alph = 'A'

print(ord(alph))

print("alkjf adfaP".capitalize())

s = "eat"
print(s.count("e"))
print(s.replace("e","g"))

print(s.center(25))
print(s.encode())
print(s.isspace())
