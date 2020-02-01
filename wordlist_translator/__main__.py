'''
The main module executing the programme
'''

import json
from typing import List
import os.path
from multitran import get_word_translations


def load_words_from_file() -> None:
    '''
    translated a file from give path
    '''
    print('Enter a path to the files with words to be translated:')
    path = str(input())
    words = open(path, 'r').read().split('\n')
    return [word for word in words if len(word)]


def translate_word_list(words: List) -> List:
    '''
    translate given list of words
    '''
    translations = []
    for word in words:
        dictionary_entries = get_word_translations(word)
        translations.append(dict(word=word, translations=dictionary_entries))
    return translations


def save_translations(translations: List) -> None:
    '''
    store obtained translations
    '''
    with open(os.path.join('results', 'translations.json'), 'w', encoding='utf-8') as file:
        json.dump(translations, file, ensure_ascii=False, indent=4)


def translate_from_file() -> None:
    '''
    read a file and save translations
    '''
    words = load_words_from_file()
    translations = translate_word_list(words)
    save_translations(translations)


if __name__ == '__main__':
    translate_from_file()
