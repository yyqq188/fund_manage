import re
import os
class RawParser(object):
    def __init__(self,raw_file):
        self.content = []
        with open(raw_file) as f:
            for line in f:
                self.content.append(line)

    def process_raw(self):
        line_num = 0
        line_sub = []
        line_total = []
        for line in self.content:
            line_num += 1
            if "%" not in line:
                if re.search(r"\s+",line):
                    line = re.sub(r"\s+",",",line)
                line_sub.append(line)
            if line_num != 0 and line_num % 9 == 0:
                line_total.append(",".join(line_sub))
                line_sub.clear()
        min_status = "||".join(line_total).replace(",,",",").replace(",%","%")
        return min_status


    def max_min_profit(self,line_record):
        if not line_record:
            print("bb")
        records = line_record.split(",")
        index = records[0]
        in_price = records[5]
        out_price = records[15]
        cur_tp =records[7]
        max_tp = records[9]
        min_tp = "-"+records[10]
        if out_price < in_price:
            cur_tp = "-"+cur_tp

        return index,cur_tp,max_tp,min_tp

if __name__ == '__main__':
    base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"raw_data")
    raw_file_path = os.path.join(base_dir,"EURCAD_1h")
    rp = RawParser(raw_file_path)
    # print(rp.process_raw())
    for line in rp.process_raw().split("||"):
        # print(line)
        print(rp.max_min_profit(line))

