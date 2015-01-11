import unittest
from digits_words_map import Main


class DigitsWordsMapTests(unittest.TestCase):
    m = None

    def setUp(self):
        self.m = Main()

    def test_none_split_words(self):
        self.assertEqual(['CAR', 'FAST', 'FASTCAR'], self.m.foo('3278227'))
        self.assertEqual(['VISITED'], self.m.foo('8474833'))

    def test_short_word(self):
        # '63' => 'OF', we should throw it away because its length is 2 which is smaller than 3
        self.assertEqual(['OFTEN'], self.m.foo('63836'))

if __name__ == '__main__':
    unittest.main()
