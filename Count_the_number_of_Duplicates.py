#Count the number of Duplicates
#Write a function that will return the count of distinct case-insensitive
#alphabetic characters and numeric digits that occur more than once in the input string.
#The input string can be assumed to contain only 
#alphabets (both uppercase and lowercase) and numeric digits. 

text = str(input("Give me text: "))

def duplicate_count(text):
    length = int(len(text))
    counter = 0
    text = text.lower()
    
    for letter in text:
        count = text.count(letter, 0, length)
        text = text.replace(letter,"")
        if count > 1:
            counter += 1
          
    
    print (counter)
    print (length)
    return()
    
duplicate_count(text)