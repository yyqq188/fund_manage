import pandas as pd
from tpsl.raw_parser import RawParser
import os
import sys
import numpy as np
class Process(object):
    def __init__(self,min_max_list):
        self.df = pd.DataFrame(min_max_list,columns=["id","cur_tp","max_tp","min_tp"])
        self.df["min_tp"] = self.df['min_tp'].astype("float64")
        self.df["max_tp"] = self.df["max_tp"].astype("float64")
        self.df["cur_tp"] = self.df["cur_tp"].astype("float64")
    def show(self):
        return self.df.info()

    def process_data(self):

        min_list,max_list = self.min_max_list()
        maxnum = -100000000
        kv = {}
        for min_tp_num in min_list:
            for max_tp_num in max_list:
                # print(int(min_tp_num),int(max_tp_num))

                total = self.total_tp_some(int(min_tp_num),int(max_tp_num))
                kv[total] = (int(min_tp_num),int(max_tp_num))
                if total > maxnum:
                    maxnum = total

        print("------------------------------------")
        print(maxnum,kv[maxnum])


    def min_max_list(self):
        min_tp = self.df["min_tp"].min()
        max_tp = self.df["max_tp"].max()
        time_num =10
        min_list = (np.arange(time_num) + 1) * 1/time_num * min_tp
        max_list = (np.arange(time_num) + 1) * 1/time_num * max_tp

        return min_list,max_list

    def total_tp_some(self,min_tp_num,max_tp_num):
        some_max_tp = self.df[self.df["max_tp"] > max_tp_num][["id", "cur_tp", "min_tp", "max_tp"]]
        some_min_tp = self.df[self.df["min_tp"] < min_tp_num][["id", "cur_tp", "min_tp", "max_tp"]]
        max_min_merge = pd.merge(some_min_tp, some_max_tp)["id"].values
        merge_line = self.df[self.df["id"].isin(max_min_merge)][["cur_tp", "min_tp", "max_tp"]]
        # print(merge_line)
        # print("-----")
        # #排除
        only_max_tp_id = np.setdiff1d(some_max_tp["id"].values, max_min_merge)
        only_min_tp_id = np.setdiff1d(some_min_tp["id"].values, max_min_merge)
        only_max_tp = some_max_tp[some_max_tp["id"].isin(only_max_tp_id)]["max_tp"]
        only_min_tp = some_min_tp[some_min_tp["id"].isin(only_min_tp_id)]["min_tp"]


        # print(len(only_max_tp) * 5000)
        # print(len(only_min_tp) * -1000)
        max_min_union = np.union1d(some_max_tp["id"].values, some_min_tp["id"].values)
        non_tp = self.df[self.df["id"].isin(np.setdiff1d(self.df["id"].values, max_min_union))]["cur_tp"].sum()
        # print(non_tp)
        total = len(only_max_tp) * max_tp_num + len(only_min_tp) * min_tp_num + int(non_tp)
        print("total is ", len(only_max_tp) * max_tp_num, len(only_min_tp) * min_tp_num, int(non_tp),total)
        return total
if __name__ == '__main__':
    print("EURCAD_1h")
    base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "raw_data")
    raw_file_path = os.path.join(base_dir, "EURCAD_1h")
    rp = RawParser(raw_file_path)
    min_max_list = []
    for line in rp.process_raw().split("||"):
        data = rp.max_min_profit(line)
        # print(data)
        min_max_list.append(data)
    Process(min_max_list).process_data()
