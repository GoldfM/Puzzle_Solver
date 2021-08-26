import marafon_parser, parse_company, parse_mail_ru, parse_pizza
import time
time_list=[]
last=0
parse=int(input('Какой парсер проверить?\n"1" -- marafon_parser \n"2" -- parse_company\n"3" -- parse_mail_ru\n"4" -- parse_pizza\n'))
kolvo=int(input('Сколько раз запускать парсер?\n'))

for i in range(kolvo):
    start_time = time.time()
    if parse==1:
        marafon_parser.parse_marafon()
    elif parse==2:
        parse_company.parse_company()
    elif parse==3:
        parse_mail_ru.parse_mail()
    elif parse==4:
        parse_pizza.parse_pizza()
    print(f"--- {time.time() - start_time} seconds ---")
