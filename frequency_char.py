def frequency_of_char():
    text = "automation"

    text_list = list(text)

    uniq_list = []

    char_count_map = {}
    for char in text_list:
        count = 0
        if char not in uniq_list:
            uniq_list.append(char)
            count = count+1
            char_count_map.update({char:count})
            
        else:
            count = char_count_map.get(char)
            count = count + 1
            char_count_map.update({char:count})
    print (uniq_list)
    print(char_count_map)

frequency_of_char()

