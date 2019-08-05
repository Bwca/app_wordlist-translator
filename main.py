from bs4 import BeautifulSoup
import re
import multitran

request_headers = {
    'Host': 'www.multitran.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.multitran.com/',
    'Cookie': 'langs=5 1; h=1080; w=1920; w1=1918; h1=928',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

multitran_response = multitran.get_query_response_page(
    'https://www.multitran.com/', request_headers)
parsed_page = BeautifulSoup(multitran_response, "html.parser")
print(parsed_page)

print(multitran.generate_get_request('test'))
