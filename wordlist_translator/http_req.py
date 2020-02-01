'''
Functions for handling requests
'''

from requests import get
from requests.exceptions import RequestException


def get_query_response_page(url: str, request_headers: dict) -> str:
    '''
    request multitran page and return its text
    '''
    try:
        remote_page_response = get(url, headers=request_headers, stream=True)
        if is_good_response(remote_page_response) is not True:
            return None

        remote_page_response.encoding = 'utf-8'
        return remote_page_response.text

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp) -> bool:
    '''
    check if a request returned html
    '''
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(error) -> None:
    '''
    print out errors
    '''
    print(error)
