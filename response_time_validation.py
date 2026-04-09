#response_time=450ms, threshold=500ms

def response_validation():
    response_time=450
    threshold=500

    if (response_time < threshold):
        return True
    else:
        return False
        
print(response_validation())