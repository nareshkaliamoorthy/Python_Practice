

def find_duplicate_in_list():

    list_1 = [1,2,2,5,5,8,8]
    new_list = []
    dup_list=[]
    for num in list_1:
        if num in new_list:
            dup_list.append(num)
            continue
        else:
            new_list.append(num)
    print(dup_list)

    
    

find_duplicate_in_list()
        
        
        