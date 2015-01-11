from constants import *


class Utils(object):

    def __init__(self):
        pass

    # char: A
    # return: '2'
    @staticmethod
    def get_digit_by_char(char):
        char_digit_map = {}
        for digit, char_list in DIGIT_CHAR_LIST_MAP.iteritems():
            for c in char_list:
                char_digit_map[c] = digit
        return char_digit_map.get(char)

    # digit = 1
    # return = 'ABC'
    @staticmethod
    def get_char_list_by_digit(digit):
        return DIGIT_CHAR_LIST_MAP.get(digit)

    # word to digit list: (['3278227', '3278', '227', '8474833'...],
    # digit to word map: {'3278227': 'FASTCAR', '63836': 'OFTEN'...})
    @staticmethod
    def word_list2digit_list():
        digital_words_list = []
        digits_words_map = {}
        for word in DICT:
            word_number = ''
            for char in word:
                word_number += Utils.get_digit_by_char(char)
            digital_words_list.append(word_number)
            digits_words_map[word_number] = word
        return digital_words_list, digits_words_map

