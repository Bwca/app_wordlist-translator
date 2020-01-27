'''
The main module executing the programme
'''

import re
from bs4 import BeautifulSoup
from data_access import http_req
from data_access.multitran_query_generator import generate_multitran_translation_query
from constants.request_headers import REQUEST_HEADERS


def main():
    '''
    The one and only main function of the module
    '''
    url = generate_multitran_translation_query('test')
    multitran_response = http_req.get_query_response_page(
        url, REQUEST_HEADERS)
    parsed_page = BeautifulSoup(multitran_response, "html.parser")

    subjects = parsed_page.find_all("td", "subj")
    translations = parsed_page.find_all("td", "trans")

    subj_trans_list = list(zip(subjects, translations))

    no_user_subjects_list = list(filter(
        lambda x: ';UserName=' not in x, subj_trans_list))

    sub_trans_list = list(
        map(lambda i: dict(sub=i[0], trans=list(filter(lambda x: ';UserName=' not in x, str(
            i[1]).split('; ')))), no_user_subjects_list)
    )

    print(len(sub_trans_list))
    print(sub_trans_list[0]['trans'])


if __name__ == '__main__':
    main()

'''

   print(subjects[0])

    t = filter(lambda x: ';UserName=' not in x,
               str(translations[0]).split('; '))

    for x in t:
        print(x)

'''
