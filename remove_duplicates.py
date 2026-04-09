

def remove_duplicates():
    num_list = [1,2,2,3,1]
    uniq_list=[]
    for num in num_list:
        if (num not in uniq_list):
            uniq_list.append(num)
    print(uniq_list)    


remove_duplicates()