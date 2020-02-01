'''
The main module executing the programme
'''

import re
from typing import List
from bs4 import BeautifulSoup
import http_req
from constants.request_headers import REQUEST_HEADERS
from models.translation_entry import TranslationEntry


def generate_multitran_translation_query(word: str,
                                         source_language_id=1, target_language_id=2) -> str:
    '''
    generate a query to m.exe on multitran.com
    language params:
    1= English; 2= Russian
    query link: https://www.multitran.com/m.exe
    params:
        l1: source language id
        l2: target language id
        s: item to translate
    '''
    return "https://www.multitran.com/m.exe?l1={0}&l2={1}&s={2}".format(
        source_language_id, target_language_id, word)


def filter_user_subjects(zipped_html: List) -> List:
    '''
    leave out user submitted subjects
    '''
    return list(filter(
        lambda subj_trans: ';UserName=' not in str(subj_trans[0]), zipped_html))


def filter_user_translations(zipped_html: List) -> List:
    '''
    leave out user submitted translations
    '''
    return list(map(lambda i: dict(sub=i[0], trans=list(
        filter(lambda x: ';UserName=' not in x, str(i[1]).split('; ')))), zipped_html))


def parse_translations_to_dictionary(zipped_html: List) -> List:
    '''
    create a dictionary from html entries
    '''

    dictionary: List[TranslationEntry] = []

    for item in zipped_html:
        topic = re.search('(?:title=")(.*)(?:">)', str(item['sub'])).group(1)
        translation: List[str] = []

        for trans in item['trans']:
            meaning = re.search('(?:<a href=.+>)(.+)(?:<\\/a>)', str(trans))

            if meaning is not None:
                translation.append(meaning.group(1))

        dictionary.append(TranslationEntry(
            subject=topic, translations=translation))

    return list(filter(lambda x: len(x['translations']), dictionary))


def get_word_translations(word: str) -> List[TranslationEntry]:
    '''
    Get a dictionary of translation subjects and meanings
    '''

    url = generate_multitran_translation_query(word)
    multitran_response = http_req.get_query_response_page(
        url, REQUEST_HEADERS)
    parsed_page = BeautifulSoup(multitran_response, "html.parser")

    subjects = parsed_page.find_all("td", "subj")
    translations = parsed_page.find_all("td", "trans")

    subject_translations_html = list(zip(subjects, translations))

    subject_translations_html = filter_user_subjects(subject_translations_html)

    subject_translations_html = filter_user_translations(
        subject_translations_html)

    dictionary = parse_translations_to_dictionary(
        subject_translations_html)

    return dictionary
