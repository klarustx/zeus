import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
#转换时间序列格式
def time_split(str):
    real_str = str[0:19]
    date = datetime.datetime.strptime(real_str,'%Y/%m/%d %H:%M:%S')
    return date
#按秒生成时间序列
def date_range_series(start_time,interal):
    ss=pd.to_datetime(start_time)
    time_series=pd.date_range(start=ss,periods=interal,freq='1s')
    real_time_serise=time_series.values[1:-1]
    return real_time_serise
#线性插值
def linear_fit(start_spot,end_spot,num):
#      print(start_spot)
#      print(end_spot)
#      print(num)
     data_list = [(start_spot+(end_spot-start_spot)/num*i) for i in range(int(num)+1)]
     real_data_list=data_list[1:-1]
     return real_data_list

#统计list中大于label的个数
def count_num(data,label):
    count=0
    for item in data:
        if (item>label):
            count=count+1
    return count
#记录数据
def write_data(path,data):
    f=open(path,"w+")
    for i in range(len(data)):
        f.write("第%s片段的加速时间："%(i+1))
        f.write(str(data[i]))
        f.write('\n')
    f.close()
