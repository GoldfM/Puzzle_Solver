import requests
from bs4 import BeautifulSoup as bs
import sqlite3
import time
start_time = time.time()




HEADERS ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
          'accept':'*/*'}
URL='https://www.marathonbet.ru/su/popular/e-Sports'
conn = sqlite3.connect('bets.db')
cur = conn.cursor()
cur.execute('DELETE FROM all_bets;',)
conn.commit()

def get_html(url):
    req = requests.get(url, headers=HEADERS,params=None)
    return req


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
            koefs = match.find_all('span', class_='selection-link active-selection')
            k_a = koefs[0].text.strip()
            try:
                k_b = koefs[2].text.strip()
            except:
                k_b = koefs[1].text.strip()
            match_list.append((game,a,b,k_a,k_b))
    cur.executemany("""INSERT INTO all_bets (game, command1, command2, koef1, koef2) VALUES (?, ?, ?, ?, ?);""", match_list)
    conn.commit()


def parse_marafon():
    html = get_html(URL)
    if html.status_code==200:
        parse(html.text)
    else:
        print('Error with website')
parse_marafon()
print(f"--- {time.time() - start_time} seconds ---")