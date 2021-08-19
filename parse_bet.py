import requests
from bs4 import BeautifulSoup as bs
import sqlite3


URL='https://www.marathonbet.ru/su/popular/e-Sports/Dota+2'
HEADERS ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
          'accept':'*/*'}
INDEX='https://www.marathonbet.ru/su/popular/e-Sports'
def get_html(url):
    req = requests.get(url, headers=HEADERS,params=None)
    return req

conn = sqlite3.connect('bets.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS dota_bet(
    id INTEGER PRIMARY KEY,
    command1 TEXT,
    command2 TEXT,
    koef1 TEXT,
    koef2 TEXT,
    test BOOLEAN);
""")
for bet_id in cur.execute('''SELECT id FROM dota_bet''').fetchall():
    cur.execute("""update dota_bet set test=0 where id = ?""",(bet_id[0],))
conn.commit()



def dota_parse(html):
    soup=bs(html,'html.parser')
    matches=soup.find_all('div',class_='bg coupon-row')
    for match in matches:
        commands=match.find_all('a',class_='member-link')
        a,b = commands[0].text.strip(), commands[1].text.strip()
        koefs = match.find_all('span', class_='selection-link active-selection')
        k_a = koefs[0].text.strip()
        k_b = koefs[1].text.strip()
        try:
            cur.execute("""select id from dota_bet where command1 = ? and command2 = ?""", (a,b))
            id = cur.fetchone()
            id=id[0]
            cur.execute("""update dota_bet set koef1=?, koef2=?,test=1 where id = ?""",(k_a,k_b,id))
            conn.commit()
            print(f'Строка с id: {id} обновлена')
        except TypeError:
            cur.execute("""INSERT INTO dota_bet (command1, command2, koef1, koef2, test) VALUES (?, ?, ?, ?, 1);""", (a, b, k_a, k_b))
            conn.commit()
            print('Добавлена новая строка')
    for bet in cur.execute('''SELECT test,id FROM dota_bet''').fetchall():
        check,id=bet
        if check==1:
            print(f' Строка номер --{id}-- актуальна')
        else:
            print(f' Строка номер !!{id}!! неактуальна')


def parse_marafon():
    html = get_html(URL)
    if html.status_code==200:
        dota_parse(html.text)
    else:
        print('Error with website')
parse_marafon()