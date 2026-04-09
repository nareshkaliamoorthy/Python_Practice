#Output: [1,3,12,0,0]
def moving_zeroes():
    list_num = [0,1,0,3,12,0]
    for num in list_num.copy():
        if num ==0:
            list_num.remove(num)
            list_num.append(num)
    
    print(list_num)

moving_zeroes()