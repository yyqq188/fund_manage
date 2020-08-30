import redis
from conf.redisconf import redisconf
import os
from tpsl.raw_parser import RawParser
from tpsl.process import Process

pool = redis.ConnectionPool(host=redisconf['host'], port=redisconf['port'], db=10,password=redisconf['password'])
my_redis = redis.Redis(connection_pool=pool)

symbol = "EURCAD_1h" #这是文件的文件名
print(symbol)
base_dir = os.path.dirname(os.path.abspath(__file__))
raw_file_path = os.path.join(base_dir, "raw_data",symbol)
rp = RawParser(raw_file_path)
min_max_list = []
for line in rp.process_raw().split("||"):
    data = rp.max_min_profit(line)
    # print(data)
    min_max_list.append(data)
total_profit,sl,tp = Process(min_max_list).process_data()
my_redis.set(symbol,",".join([str(total_profit),str(sl),str(tp)]))

