import requests
from bs4 import BeautifulSoup

url = 'http://catalog.svetlovka.ru/jirbis2/index.php?option=com_irbis&view=irbis&Itemid=115'


r1 = requests.get(url)



post = {
    'first_number:': 1,
    'req_id_client': 734996563,
    'req_static': 0,
    'selected_search_flag': 0,
    'task': 'search_broadcast',
    'title': 'Амулет+самарканда'
}

r = requests.post('http://catalog.svetlovka.ru/jirbis2/components/com_irbis/ajax_provider.php',
data=post, 
headers={'Referer': url})

soup = BeautifulSoup(r.content, 'lxml')

with open('svetlovka.txt', 'w') as f:
    f.write(soup.prettify())