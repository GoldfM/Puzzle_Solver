
import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool

URL = 'http://amdy.su/'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
          'accept':'*/*'}
list_hrefs=[]
def get_html(url,params=None):
    req = requests.get(url, headers=HEADERS,params=params)
    return req.text


def parse(html):
    soup = bs(html,'html.parser')
    h2 = soup.find_all('h2',class_='entry-title')
    for href in h2:
        href_cur = href.find('a',class_='').attrs['href']
        list_hrefs.append(href_cur)

def pool_def(href):
    soup = bs(get_html(href), 'html.parser')
    title = soup.find('h1', class_='entry-title').text
    p_text = soup.find('div', class_='entry-content').find('p', class_='').text
    print(title)


def parse_content_pages():
    global list_hrefs
    with Pool(6) as pool:
        pool.map(pool_def, list_hrefs)



def main():
    soup = bs(get_html(URL),'html.parser')
    count_page = soup.find('div', class_='nav-links').find_all('a')
    all_page = int(count_page[1].text)
    parse(get_html(URL))
    for i in range(2,all_page+1):
        href = f'{URL}page/{i+1}'
        parse(get_html(href))
    parse_content_pages()





if __name__ == '__main__':
    start_time = time.time()
    main()
    print(time.time()-start_time)
