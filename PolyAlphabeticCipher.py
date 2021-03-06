""" Este programa implementa un cifrado polialfabético """

import string

ALPHABET = string.ascii_lowercase
CHARACTERS_THAT_MUST_REMAIN_THE_SAME = string.digits + string.punctuation + string.whitespace

class PolyAlphabeticCipher:



    def cycle_get(lst, index):
        """
        si la lista finaliza volver al inicio.
        >>> cycle_get(["lorem","ipsum","dolor","sit"],8)
        "lorem"
        """
        new_index = index % len(lst)
        return (lst[new_index])


    def cycle_increment_index(index, lst):
        """
        Si es el final: volver al principio
        sino: incrementar.
        >>> cycle_increment_index(0,["a","b","c"])
        1
        >>> cycle_increment_index(2,["a","b","c"])
        0
        """
        if index == len(lst) - 1:
            index = 0
        else:
            index += 1
        return (index)


    def shift(letter, value):
        """
        Cambia una letra del alfabeto por el valor,
        si el alfabeto termina, vuelve al principio.
        >>> shift('a',5)
        f
        >>> "".join([shift(i,20) for i in "hello"])
        'byffi'
        """
        current_letter_value = ALPHABET.find(letter)
        end_value = current_letter_value + value
        return (PolyAlphabeticCipher.cycle_get(ALPHABET, end_value))


    def convert_key_to_numbers(key):
        """
        Utiliza el valor alfabético de las letras para convertir una palabra
        a una lista de numeros.
        >>> convert_key_to_numbers("abcde")
        [0,1,2,3,4]
        >>> convert_key_to_numbers("example")
        [4, 23, 0, 12, 15, 11, 4]
        """
        return ([ALPHABET.find(i) for i in key])


    def encrypt(self, text, key, reverse_operation=False):
        """
        Encripta el texto con un cifrado polialfabetico.
        >>> encrypt("lorem ipsum dolor sit amet, consectetur adipiscing elit","latine")
        'wokmz masnu qswok avx lmxb, psysxkgieuk iqmailkvrr eeqg'
        >>> encrypt("the quick brown fox jumps over the lazy dog","gvufigfwiufw")
        'zcy vcohg jltst aic rarla iaax obj tgeu lil'
        """
        text = text.lower()
        key = PolyAlphabeticCipher.convert_key_to_numbers(key)
        index_of_key = 0
        result = ""
        for char in text:
            if char in CHARACTERS_THAT_MUST_REMAIN_THE_SAME:
                result += char
            else:
                if not reverse_operation:
                    result += PolyAlphabeticCipher.shift(char, key[index_of_key])
                else:
                    result += PolyAlphabeticCipher.shift(char, - key[index_of_key])
                index_of_key = PolyAlphabeticCipher.cycle_increment_index(index_of_key, key)
        return (result)


    def decrypt(self,text, key):
        """
        desencripta el texto previamente desencriptado con un cifrado polialfabetico.
        >>> decript('wokmz masnu qswok avx lmxb, psysxkgieuk iqmailkvrr eeqg',"latine")
        'lorem ipsum dolor sit amet, consectetur adipiscing elit'
        >>> decrypt("zcy vcohg jltst aic rarla iaax obj tgeu lil","gvufigfwiufw")
        'the quick brown fox jumps over the lazy dog'
        """
        return (PolyAlphabeticCipher.encrypt(self, text, key, reverse_operation=True))
