
def check_anagram():

    word_1 = "silentva"
    word_2 = "listen"

    list1 = list(word_1)
    list2 = list(word_2)
    list1.sort()
    list2.sort()

    print(list1)
    print(list2)

    if (list1 == list2):
        print("anagram")
    else:
        print("not an anagram")


check_anagram()
    

        


