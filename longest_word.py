

from warnings import catch_warnings


def find_longest_word():
    input = "I love automation testing"
    try:
        list1 = input.split()
        word_mx = min(list1, key=len)
        max_size = 0
        longest_word = ""
        for word in list1:
            size = len(word)
            if (size > max_size):
                max_size = size
                longest_word = word
        print(longest_word)
        print(word_mx)
    except Exception as e:
        print("Error", e)
        raise ValueError("Error")
    finally:
        print("finally")

find_longest_word()


