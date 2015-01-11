from utils import Utils
from tree import Leaf


class Main(object):
    root = Leaf('root')
    digital_words = None
    digits_words_map = None

    def __init__(self):
        # init digit and word map
        self.digital_words, self.digits_words_map = Utils.word_list2digit_list()
        # build tree
        for digit_word in self.digital_words:
            current = self.root
            for digit in digit_word:
                digit_leaf = Leaf(digit)
                current = current.append_child(digit_leaf)
            current.end = True

    def foo(self, input_digit):
        current = self.root
        separator_list = []
        result_words_list = []
        last_separator_index = 0
        # this loop is to search digits in the tree.
        # when current digit meet the leaf value, we will do it again
        # in the deeper leaf
        for i in range(0, len(input_digit)):
            digit = input_digit[i]
            if current.has_child(digit):
                current = current.get_children(digit)
                # handle things like "FAST" and "CAR" in "FASTCAR"
                if current.is_word_end() and i-last_separator_index >= 3:
                    separator_list.append(i)
                    last_separator_index = i
                continue
        # if to_find_digits' last digit is the last leaf of the tree or the end of a word,
        # that is to say, we find a word.
        # e.g, "FASTCAR" will get a list [3, 6], which means, the fisrt 4 digits mean a word
        # and the next 3 digits mean another word
        if current.is_last() or current.is_word_end():
            last_separator_index = 0
            for separator_index in separator_list:
                result_words_list.append(self.digits_words_map[input_digit[last_separator_index:separator_index+1]])
                result_words_list.append(self.digits_words_map[input_digit[0:separator_index+1]])
                last_separator_index = separator_index + 1
        return list(set(result_words_list))
