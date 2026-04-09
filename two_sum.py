


def find_two_sum():
    nums_1=[2,7,11,15,2,3,8,6,1]
    
    target=9
    nums_2=nums_1
    result = []

    for i, a_num in enumerate(nums_1):
        for j, b_num in enumerate(nums_2):
            if ( j<len(nums_1)-1):
                if (nums_1[i]+nums_2[j+1] == target):
                    result.append((i,j+1))
        
    print(result)


find_two_sum()



