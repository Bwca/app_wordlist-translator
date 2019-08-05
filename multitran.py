from requests import get
from requests.exceptions import RequestException


def get_query_response_page(url: str, request_headers: dict) -> str:
    '''
    request multitran page and return its text
    '''
    try:
        remotePageResponse = get(url, headers=request_headers, stream=True)
        if is_good_response(remotePageResponse) is not True:
            return None

        remotePageResponse.encoding = 'utf-8'
        return remotePageResponse.text

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def generate_get_request(word: str, source_language_id=1, target_language_id=2) -> str:
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
    return "https://www.multitran.com/m.exe?l1={0}&l2={1}&s={2}".format(source_language_id, target_language_id, word)


def is_good_response(resp) -> bool:
    '''
    check if a request returned html
    '''
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e) -> None:
    """
    print out errors
    """
    print(e)
