# coding=utf-8
import numpy as np
import pandas as pd
import sys

def order_percent_grid(input_path,output_path):
    dfs = pd.read_csv("%s"%(input_path),sep=",")
    dfs["trace_id_cnt_jiaquan"] = dfs["trace_id_cnt"]*dfs["ecr_trans"]
    #dfs.head()
    sum_order = sum(list(dfs.trace_id_cnt))
    sum_order_jiaquan = sum(list(dfs.trace_id_cnt_jiaquan))
    sum_gmv = sum(list(dfs.predict_gmv_sum))
    data = dfs.sort_values(["distance","ecr_trans"],ascending=True)
    data["trace_id_percent"] = 0
    data["sum_order_jiaquan"] = 0
    data["gmv_percent"] = 0
    datass = pd.DataFrame(columns=['distance', 'ecr_trans', 'order_percent',"order_percent_jiaquan","gmv_percent"])
    tmp =0

    #获取相应百分比
    for i in range(0,22):
        for j in [x/100.0 for x in range(100) if x % 5 == 0]:
            temp = data [(data["distance"]<=i)|(data["ecr_trans"]>=j)]
            order_cnt = sum(list(temp.trace_id_cnt))
            order_jiaquan_cnt = sum(list(temp.trace_id_cnt_jiaquan))
            gmv_sum = sum(list(temp.predict_gmv_sum))
            datass.loc[tmp,["distance"]]= i
            datass.loc[tmp,["ecr_trans"]]= j
            datass.loc[tmp,["order_percent"]]= float(order_cnt)/ sum_order
            datass.loc[tmp,["order_percent_jiaquan"]]= float(order_jiaquan_cnt)/ sum_order_jiaquan
            datass.loc[tmp,["gmv_percent"]]= float(gmv_sum) / sum_gmv
            tmp=tmp+1
    datass.tail()
    data_reorigin = datass.sort_values(["distance","ecr_trans"],ascending=True)
    # data_reorigin.head()

    cols= [str(x/100.0) for x in range(100) if x % 5 == 0]
    data_order = pd.DataFrame(columns=cols)
    data_order_jiaquan = pd.DataFrame(columns=cols)
    data_gmv = pd.DataFrame(columns=cols)

    #生成样表，并对其进行赋值
    for i in range(0,22):
        data_order.loc[i]=0
        data_gmv.loc[i]=0
        data_order_jiaquan.loc[i]=0

    for i in range(0,22):
        for j in [x/100.0 for x in range(100) if x % 5 == 0]:
            ds_tmp = data_reorigin[(data_reorigin["distance"] == i)&(data_reorigin["ecr_trans"] == j)]
            data_order.loc[i,[str(j)]] = ds_tmp["order_percent"].values

    data_order.to_csv("%s"%(output_path),sep="\t")

    for i in range(0,22):
        for j in [x/100.0 for x in range(100) if x % 5 == 0]:
            ds_tmp = data_reorigin[(data_reorigin["distance"] == i)&(data_reorigin["ecr_trans"] == j)]
            data_order_jiaquan.loc[i,[str(j)]] = ds_tmp["order_percent_jiaquan"].values

    print data_order_jiaquan.head()

    for i in range(0,22):
        for j in [x/100.0 for x in range(100) if x % 5 == 0]:
            ds_tmp = data_reorigin[(data_reorigin["distance"] == i)&(data_reorigin["ecr_trans"] == j)]
            data_gmv.loc[i,[str(j)]] = ds_tmp["gmv_percent"].values


    print data_gmv.head()

    #data_reorigin["gmv_percent_int"]=data_reorigin["gmv_percent"].apply(lambda x: round(x,2))
    # data_gmv_new = data_reorigin[data_reorigin["gmv_percent_int"]==0.45]
    # data_gmv_new.head()
    menkan = 0.2

if __name__ == '__main__':
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    order_percent_grid(input_path,output_path)

