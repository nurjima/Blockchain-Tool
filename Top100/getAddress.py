import requests
from bs4 import BeautifulSoup

address = []


def get_html(url):
    r = requests.get(url, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.99 Safari/537.36',
        'accept': '*/*'})
    return r


def get_address(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('tbody').find_all('tr')

    for item in items:
        address.append(item.find('a').get_text(strip=True))


def repeat():
    for i in range(1, 5):
        url = "https://etherscan.io/accounts/" + str(i)
        html = get_html(url)
        get_address(html.text)


repeat()
