# Дана строка (возможно, пустая), состоящая из букв A-Z:  
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB 
 
# Нужно написать функцию RLE,  которая на выходе даст строку вида:  
# A4B3C2XYZD4E3F3A6B28  
 
# И сгенерирует ошибку, если на вход пришла невалидная строка.  
 
# Пояснения: Если символ встречается 1 раз, он остается без изменений; 
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.



str_1 = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'

def RLE(str):
    str += " "  # кастыль чтобы последний элемент добавлялся 
    count = 1
    res_str = ''
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            count += 1
        elif str[i] != str[i+1]:
            if count > 1:
                res_str  = res_str + (str[i] +f'{count}' )
            else:
                 res_str  = res_str + str[i]
            count = 1
    return res_str   


print(RLE(str_1))     
 
