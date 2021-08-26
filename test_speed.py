import marafon_parser
import time
time_list=[]
last=0
for i in range(20):
    start_time = time.time()
    x = marafon_parser.parse_marafon()
    print(f"--- {time.time() - start_time} seconds ---")