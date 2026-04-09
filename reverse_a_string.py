

def reverse_a_string():
    text = "automation"
    reverse_text = text[::-1]
    print(reverse_text)
    text_list = list(reversed(text))
    print(text_list)
   # text_list.reverse()
   # reverse_lst = text_list
    print(text_list)
    word = ""
    for char in text_list:
        word = word + "".join(char)
    print(word)
    

reverse_a_string()