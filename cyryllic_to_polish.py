
tekst = "бювар"

def cyryllic_to_polish(tekst): 
    
    result = ""
    SPECIAL = "оoAаO,. -1234567890VvidхX"
    polish ={"В":"B",
             "б":"b",
             "в":"w",
             "Г":"G",
             "г":"g",
             "Д":"d",
             "д":"d",
             "Е":"Je",
             "е":"je",
             "Ё":"Jo",
             "ё":"jo",
             "Ж":"Ż",
             "ж":"ż",
             "З":"Z",
             "з":"z",
             "И":"I",
             "и":"i",
             "Й":"J",
             "й":"j",
             "К":"K",
             "к":"k",
             "Л":"L",
             "л":"l",
             "М":"M",
             "м":"m",
             "Н":"N",
             "н":"n",
             "П":"P",
             "п":"p",
             "P":"R",
             "р":"r",
             "C":"S",
             "с":"s",
             "Т":"T",
             "т":"t",
             "У":"U",
             "у":"u",
             "Ф":"F",
             "ф":"f",
             "Х":"Ch",
             "x":"ch",
             "Ц":"C",
             "ц":"c",
             "Ч":"Cz",
             "ч":"cz",
             "Ш":"Sz",
             "ш":"sz",
             "Щ":"Szcz",
             "щ":"szcz",
             "Ы":"Y",
             "ы":"y",
             "Э":"E",
             "э":"e",
             "Ю":"Ju",
             "ю":"ju",
             "Я":"Ja",
             "я":"ja"}

    for letter in tekst:
        if letter == "ь" or letter == "ъ" or letter == "Ь" or letter == "Ъ":
            continue
        
        elif letter not in SPECIAL:
            result += polish[letter]
        
          
        else:
            result += letter
              
    return result

result_2 = cyryllic_to_polish(tekst)

print(result_2)