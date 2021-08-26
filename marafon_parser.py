import requests
from bs4 import BeautifulSoup as bs
import sqlite3


HEADERS ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
          'accept':'*/*'}
URL='https://www.marathonbet.ru/su/popular/e-Sports'




def parse(html):
    soup=bs(html,'html.parser')
    categories=soup.find_all('div',class_='category-container')
    match_list=[]
    for cat in categories:
        game = cat.find('span',class_='nowrap').text
        matches=cat.find_all('div',class_='bg coupon-row')
        for match in matches:
            commands = match.find('table',class_='member-area-content-table').find_all('span',class_='')
            a,b = commands[0].text.strip(), commands[1].text.strip()
            koef_blocks = match.find_all('td', class_='height-column-with-price')
            k_a=koef_blocks[0].find('span').text
            try:
                k_b = koef_blocks[2].find('span').text
            except:
                k_b = koef_blocks[1].find('span').text
            match_list.append((game,a,b,k_a,k_b))
    conn = sqlite3.connect('bets.db')
    cur = conn.cursor()
    try:
        cur.execute('DELETE FROM all_bets;', )

    except:
        cur.execute("""CREATE TABLE IF NOT EXISTS all_bets(
                id INTEGER PRIMARY KEY,
                game TEXT,
                command1 TEXT,
                command2 TEXT,
                koef1 TEXT,
                koef2 TEXT);
            """)
    cur.executemany("""INSERT INTO all_bets (game, command1, command2, koef1, koef2) VALUES (?, ?, ?, ?, ?);""", match_list)
    conn.commit()



def parse_marafon(url):
    html = requests.get(url, headers=HEADERS)
    if html.status_code==200:
        parse(html.text)
    else:
        print('Error with website')
if __name__ == "__main__":
    parse_marafon(URL)