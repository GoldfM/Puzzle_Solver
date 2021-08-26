import requests
from bs4 import BeautifulSoup as bs
import sqlite3




URL='https://www.pizzatempo.by/menu/pizza.html'
HEADERS ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
          'accept':'*/*'}
def get_html(url):
    req = requests.get(url, headers=HEADERS,params=None)
    return req




def get_content(html):
    name_list=[]
    soup=bs(html,'html.parser')
    list_items=[]

    for item in soup.find_all('div',class_='group3'):
        name=item.find('span')
        list_items.append(name.text)
        name_list.append(name.text)
    for item in soup.find_all('div', class_='group1'):
        name = item.find('span')
        list_items.append(name.text)
        name_list.append(name.text)
    for item in soup.find_all('div',class_='group2'):
        name=item.find('span')
        list_items.append(name.text)
        name_list.append(name.text)
    conn = sqlite3.connect('pizza.db')
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM pizzas")
    except:
        cur.execute("""CREATE TABLE IF NOT EXISTS pizzas(
            id INT PRIMARY KEY,
            name TEXT);
        """)
    conn.commit()
    print(name_list)
    id=0
    for name in name_list:
        id+=1
        db = (id, name)
        cur.execute("INSERT INTO pizzas VALUES(?, ?);", db)
    conn.commit()



def parse_pizza():
    html = get_html(URL)
    if html.status_code==200:
        get_content(html.text)
    else:
        print('Error with website')

if __name__ == "__main__":
    parse_pizza()
