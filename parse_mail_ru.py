import requests
from bs4 import BeautifulSoup as bs

URL='https://mail.ru/'
HEADERS ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
          'accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'}
def get_html(url):
    req = requests.get(url, headers=HEADERS,params=None)
    return req

def get_content(html):
    soup=bs(html,'html.parser')
    items=soup.find_all('div',class_='news-item')
    for item in items:
        news={
            'text':item.find('a',class_='news-visited').text.replace('\xa0',' ').replace('\r',''),
            'href':item.find('a',class_='news-visited').attrs['href']
        }
        print(news)



def parse_mail():
    html = get_html(URL)
    if html.status_code==200:
        get_content(html.text)

    else:
        print('Error with website')
parse_mail()