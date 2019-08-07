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
