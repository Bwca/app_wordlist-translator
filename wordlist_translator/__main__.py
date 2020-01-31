'''
The main module executing the programme
'''

import re
from typing import List
from bs4 import BeautifulSoup
from data_access import http_req
from data_access.multitran_query_generator import generate_multitran_translation_query
from constants.request_headers import REQUEST_HEADERS
from models.translation_entry import TranslationEntry


def main():
    '''
    The one and only main function of the module
    '''

  #  print(dictionary)

    url = generate_multitran_translation_query('test')
    multitran_response = http_req.get_query_response_page(
        url, REQUEST_HEADERS)
    parsed_page = BeautifulSoup(multitran_response, "html.parser")

    subjects = parsed_page.find_all("td", "subj")
    translations = parsed_page.find_all("td", "trans")

    zipped_subjects_and_translations = list(zip(subjects, translations))

    subjects_and_translations_without_user_subjects = list(filter(
        lambda x: ';UserName=' not in str(x[0]), zipped_subjects_and_translations))

    subject_translations_dictionaries_list_without_user_translations = list(
        map(lambda i: dict(sub=i[0], trans=list(filter(lambda x: ';UserName=' not in x, str(
            i[1]).split('; ')))), subjects_and_translations_without_user_subjects)
    )

    dictionary: List[TranslationEntry] = []

    for item in subject_translations_dictionaries_list_without_user_translations:
        topic = re.search('(?:title=")(.*)(?:">)', str(item['sub'])).group(1)
        translation: List[str] = []
        for trans in item['trans']:
            meaning = re.search('(?:<a href=.+>)(.+)(?:<\/a>)', str(trans))
            if meaning is not None:
                translation.append(meaning.group(1))
        dictionary.append(TranslationEntry(
            subject=topic, translations=translation))

    dictionary = list(filter(lambda x: len(x['translations']), dictionary))

    print(dictionary)
    print(len(dictionary))


if __name__ == '__main__':
    main()
