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

def get_html(url):
    req = requests.get(url, headers=HEADERS,params=None)
    return req


def parse(html):
    soup=bs(html,'html.parser')
    categories=soup.find_all('div',class_='category-container')
    for cat in categories:
        game = cat.find('span',class_='nowrap').text
        print(f' НОВЫЙ РАЗДЕЛ. СЛЕДУЮЩИЕ СТАВКИ ПО ИГРЕ: {game}')
        matches=cat.find_all('div',class_='bg coupon-row')
        for match in matches:
            commands = match.find('table',class_='member-area-content-table').find_all('span',class_='')
            a,b = commands[0].text.strip(), commands[1].text.strip()

            koefs = match.find_all('span', class_='selection-link active-selection')
            k_a = koefs[0].text.strip()
            k_b = koefs[1].text.strip()
            print(f'"{a}" VS "{b}"  koefs = {k_a}: {k_b}')
            try:
                cur.execute("""select id from all_bets where game=? and command1 = ? and command2 = ?""",(game,a,b))
                id = cur.fetchone()
                id=id[0]
                cur.execute("""update all_bets set koef1=?, koef2=?,test=1 where id = ?""",(k_a,k_b,id))
                conn.commit()
                print(f'[INFO] Строка с id: {id} обновлена')
            except TypeError:
                cur.execute("""INSERT INTO all_bets (game, command1, command2, koef1, koef2, test) VALUES (?, ?, ?, ?, ?, 1);""", (game, a, b, k_a, k_b))
                conn.commit()
                print('Добавлена новая строка')
    for bet in cur.execute('''SELECT test,id FROM all_bets''').fetchall():
        check,id=bet
        if check==0:
            cur.execute("""DELETE from all_bets where id = ?""", (id,))
            print(f'[OLD BET] Строка с id: {id} удалена из БД')



def parse_marafon():
    cur.execute(f"""CREATE TABLE IF NOT EXISTS all_bets(
        id INTEGER PRIMARY KEY,
        game TEXT,
        command1 TEXT,
        command2 TEXT,
        koef1 TEXT,
        koef2 TEXT,
        test BOOLEAN);
    """)
    conn.commit()
    html = get_html(URL)
    if html.status_code==200:
        parse(html.text)
    else:
        print('Error with website')
parse_marafon()
print(f"--- {time.time() - start_time} seconds ---")