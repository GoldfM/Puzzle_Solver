import requests
from bs4 import BeautifulSoup as bs
import sqlite3


URL='https://smolensk.jsprav.ru/'
HEADERS ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
          'accept':'*/*'}
INDEX='https://smolensk.jsprav.ru'
def get_html(url):
    req = requests.get(url, headers=HEADERS,params=None)
    return req
dev_id=0


conn = sqlite3.connect('../Разные проги/company_smolensk.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS company(
    id INTEGER PRIMARY KEY,
    name TEXT,
    time TEXT,
    address TEXT,
    site TEXT);
""")
conn.commit()

def get_content(html):
    list_href = []
    soup=bs(html,'html.parser')
    items=soup.find_all('div',class_='col-xs-12 col-sm-6 col-md-6 col-lg-4')
    for item in items:
        a = item.find('a',class_='').attrs['href']
        list_href.append(a)
    return list_href

def get_content_2(html):
    list_href2=[]
    soup=bs(html,'html.parser')
    items=soup.find_all('div',class_='cat-item')
    for item in items:
        a = item.find('a',class_='').attrs['href']
        list_href2.append(a)
    return list_href2

def get_content_3(html):
    global dev_id
    names = []
    soup=bs(html,'html.parser')
    items=soup.find_all('div',class_='org')
    for item in items:
        dev_id += 1
        address = ''
        time_work = ''
        name=''
        url=''
        name = item.find('a',class_='lnk')
        url = INDEX + name.attrs['href']
        name = name.text

        try:
            address= item.find('span', class_='address').text
        except:
            pass
        try:
            time_work = item.find('span', class_='time').text
        except:
            pass
        if address == '':
            address = 'Не указано'
        if time_work=='':
            time_work='Не указано'
        print(f'{name } ---- {url} ---- {address} --- {time_work}')
        sqlite_insert_with_param = """INSERT INTO company
                                      (id, name, time, address, site)
                                      VALUES (?, ?, ?, ?, ?);"""
        data_tuple = (dev_id, name, time_work, address, url)
        cur.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()

    return names

def parse_company():
    html = get_html(URL)
    if html.status_code==200:
        hrefs = get_content(html.text)
        for href in hrefs:
            html2 = get_html(INDEX+href)
            hrefs2 = get_content_2(html2.text)
            for href2 in hrefs2:
                html3=get_html((INDEX + href2))
                x = get_content_3(html3.text)

    else:
        print('Error with website')
parse_company()