
from genericpath import exists


def first_non_repeating_char():

    word = "cababcdde"
    list1 = list(word)
    list2 = list1.copy()
    list3 = []
    for i, char1 in enumerate(list1):
        for j, char2 in enumerate(list2):
            if char1 == char2 and char1 not in list3:
                list3.append(char1)

            elif (char1 == char2 and char1 in list3):
                list3.remove(char1)
    if(len(list3))>0:
        print(list3[0])
    else:
        print([])

#first_non_repeating_char()

def first_non_repeat_char():
    word = "cababcdde"
    list1 = list(word)
    for char in list1:
        if list1.count(char) == 1:
            print(char)
            break

first_non_repeat_char()
            

