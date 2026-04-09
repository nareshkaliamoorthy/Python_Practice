
import string


def string_rotation():
    text1="abcde"
    text2="cdeaab"
    
    if len(text1) == len(text2):
        merged_text = text1 + text2

        if text2 in merged_text:
            return True
        else:
            return False
    else:
        print("invalid string")
        
   
   
    
string_rotation()
