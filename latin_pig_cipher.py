# -*- coding: utf-8 -*-

import re
import string

piglatin_cipher_words = {"football415": "ootball415gāŷ", "Pittsburgh": "Ittsburghrāŷ",
                           "Y2ellow": "Y2ellowŵāŷ", "yellow": "ellowaāŷ", "yttrium":"iumavvtāŷ"}

Test_word = 'Pittsburgh'
vowels = 'aeiou'
digits = '0123456789'
cipher_list = []
A_str = string.ascii_lowercase

def caesar_encrypt(Letter, shift):

    Shifting = lambda A_str, shift: Letter.maketrans(A_str, A_str[shift:] + A_str[:shift])
    return(Letter.translate(Shifting(A_str, shift)))


def LP_cipher(Test_word, step):

    first = Test_word[0]
    second = Test_word[1]
    text, sub_str, ciphered_text, piglatin = None, None, None, None
    is_capital = False

    if first.lower() == 'y' and second.isdigit():
   

        piglatin = Test_word +'ŵāŷ'

    elif any(char.isdigit() for char in Test_word) and first.lower() not in vowels:
        num = re.search(r'\d+', Test_word)
        low = min([int(n) for n in num.group()])
        numeric = num.group()
        d_pos = Test_word.find(numeric)
        if first == first.upper():
            is_capital = True
        for l in Test_word[:d_pos]:
            if l in vowels:
                l_pos = Test_word.find(l)
                sub_str = Test_word[l_pos:d_pos]
                text = Test_word[:l_pos]
                break

        if low < step:
            ciphered_text = caesar_encrypt(text, low)
        else:
            ciphered_text = caesar_encrypt(text, step)
        if is_capital:
            piglatin = sub_str.capitalize()+numeric+ciphered_text+ "āŷ"
        else:
            piglatin = sub_str + numeric + ciphered_text + "āŷ"
    elif first.lower() not in vowels and any(char.isdigit() for char in Test_word) == False:
        text = None
        for l in Test_word:
            if l.lower() in vowels:
                l_pos = Test_word.find(l)
                sub_str = Test_word[l_pos:]
                if first == first.upper():
                    is_capital = True
                text = Test_word[:l_pos].lower()
                break
        ciphered_text = caesar_encrypt(text, step)
   
        if is_capital:
            piglatin = sub_str.capitalize()+ciphered_text+"āŷ"
        else:
            piglatin = sub_str + ciphered_text + "āŷ"

    print(f'\nThe word is {Test_word} and is equal to piglatin word is {piglatin}. '
          f'The mapping dictionary is {piglatin_cipher_words[Test_word] == piglatin}')

LP_cipher(Test_word, 2)