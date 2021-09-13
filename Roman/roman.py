def integer_to_roman(num):
    result = ""
    dict_roman = {
        1000:"M",
        900:"CM",
        500:"D",
        400:"CD",
        100:"C",
        90:"XC",
        50:"L",
        40:"XL",
        10:"X",
        9:"IX",
        5:"V",
        4:"IV",
        1:"I",
    }
#num = 29
    for k, v in dict_roman.items():
        if num >= k: # 10
            result += v * int(num/k) # XX
            num -= k * int(num/k) # 9
        
      
    
    return result