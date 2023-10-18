def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    
    if len(str(zip_code)) == 5:
        if zip_code.isdigit() == True:
            return True
        else:
            return False
    return False
    


    #檢查有五個字
    #每個字都是數字 
    
print(is_valid_zip("12345"))
print(is_valid_zip("ABCDE"))
print(is_valid_zip("12CDE"))
#可不可不論輸入什麼自動轉成string?