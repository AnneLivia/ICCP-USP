def maiusculas(str):
    res = ""
    for i in str:
        if(ord(i) >= 65 and ord(i) <= 90):
            res+=i
    return res
