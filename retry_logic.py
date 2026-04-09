
def retry_logic(retry_count):
    count = 1
    while (count <= retry_count):
        if (count < retry_count):
            print(f"Attemp {count}: Login Failed")
        elif (count==retry_count):
            print(f"Attemp {count}: Login Success")
        count = count+1

retry_logic(5)