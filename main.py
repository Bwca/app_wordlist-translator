from bs4 import BeautifulSoup
import re
import multitran
import html_page_queries
import word_frequency_webpage

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

""" 
multitran_response = html_page_queries.get_query_response_page(
    'https://www.multitran.com/', request_headers)
    
parsed_page = BeautifulSoup(multitran_response, "html.parser")
print(parsed_page)
 """

url = multitran.generate_get_request('test')
multitran_response = html_page_queries.get_query_response_page(url, request_headers)
parsed_page = BeautifulSoup(multitran_response, "html.parser")

print(url)

results = parsed_page.find_all(title=True)

for x in results:
    xmatch = (re.search("(?:title=\")(.*)(?:\">)", str(x)))
    if xmatch is not None:
        print(xmatch.group(1))
print (len(results))