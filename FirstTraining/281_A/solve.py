#Word Capitalization
inputword  = input()
print(inputword if (inputword[0].isupper()) else (inputword[0].upper()+inputword[1::]))