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

    print(url)

    results = parsed_page.find_all(title=True)

    for x in results:
        xmatch = (re.search("(?:title=\")(.*)(?:\">)", str(x)))
        if xmatch is not None:
            print(xmatch.group(1))
    print(len(results))


if __name__ == '__main__':
    main()
