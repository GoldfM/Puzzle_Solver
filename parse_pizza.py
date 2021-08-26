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
    conn = sqlite3.connect('pizza.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS pizzas(
        id INT PRIMARY KEY,
        name TEXT);
    """)
    conn.commit()
    soup=bs(html,'html.parser')
    items=soup.find_all('div',class_='group3')

    list_items=[]
    id=1
    for item in soup.find_all('div',class_='group3'):
        name=item.find('span')
        list_items.append(name.text)
        name=str(name.text)
        db=(id,name)
        cur.execute("INSERT INTO pizzas VALUES(?, ?);", db)
        conn.commit()
        id += 1
    for item in soup.find_all('div', class_='group1'):
        name = item.find('span')
        list_items.append(name.text)
        name = str(name.text)
        db = (id, name)
        cur.execute("INSERT INTO pizzas VALUES(?, ?);", db)
        conn.commit()
        id += 1
    for item in soup.find_all('div',class_='group2'):
        name=item.find('span')
        list_items.append(name.text)
        name = str(name.text)
        db = (id, name)
        cur.execute("INSERT INTO pizzas VALUES(?, ?);", db)
        conn.commit()
        id += 1


    print(len(list_items))



def parse_pizza():
    html = get_html(URL)
    if html.status_code==200:
        get_content(html.text)
    else:
        print('Error with website')

if __name__ == "__main__":
    parse_pizza()
