'''
translation module from english to french and french to english
'''

from deep_translator import MyMemoryTranslator


def englishToFrench(english_text):
    '''
    translate english text to french text
    '''
    frenchText = MyMemoryTranslator(
        source="english", target="french").translate(english_text)
    return frenchText


def frenchToEnglish(french_text):
    '''
    translate french text to english text
    '''
    englishText = MyMemoryTranslator(
        source="french", target="english").translate(french_text)
    return englishText
