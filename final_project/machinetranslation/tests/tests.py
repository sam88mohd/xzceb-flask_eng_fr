from translator import englishToFrench, frenchToEnglish
import unittest


class TestTranslation(unittest.TestCase):
    def test_english_to_french_function(self):
        self.assertEqual(englishToFrench("hello"), "bonjour")

    def test_french_to_english(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")


if __name__ == "__main__":
    unittest.main()
