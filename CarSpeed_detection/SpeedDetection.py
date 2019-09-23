import numpy as np
import pandas as pd
from utils import *
#数据预处理
def data_preconditon(df):
    df["time"]=df["time"].apply(time_split)
    df["month"]=df["time"].apply(lambda x:x.month)
    df["day"]=df["time"].apply(lambda x:x.day)
    df["hour"]=df["time"].apply(lambda x:x.hour)
    df["minute"]=df["time"].apply(lambda x:x.minute)
    df["second"]=df["time"].apply(lambda x:x.second)
    # df["num"]=df["hour"]*60*df["minute"]*60*df["second"]   
    return df

#获取时间序列中缺少时间间隔小于180s的序列
def filter_timeseries(data_df):
    data=data_df[data_df["time"]!="00:00:01"]
    data["month"]=data["month"].astype(float)
    data["day"]=data["day"].astype(float)
    data["minute"]=data["minute"].astype(float)
    #获取时间间隔小于180s的序列
    data_filter=data[(data['month']==0)&(data['day']==0)&(data['hour']==0)&((data['minute']>-3)&(data['minute']<3))]
    # data_filter['num']=data_filter['minute']*60 +data_filter['second']
    data_filter['num'] = data_filter.apply(lambda x: x[17] * 60 + x[18], axis=1)
    return data_filter

#求时间片段缺少的索引值和需要补全的时间点数
def get_timeindex_num(data,time_list):
    index_drop=list(data.index.values)
    num_list=list(data.num.values)
    timeindex_num=[]
    for i in range(len(index_drop)):
        #插入片段的位置
        location=(index_drop[i]-1)
        time_spot = time_list[location]
        timeindex_num.append([location,time_spot,num_list[i]])
    
    return timeindex_num
#补全缺失时间
def completion_misstime(df_dict,timeindex_num):
    final_dict={}
    final_dict['time']=[]
    final_dict['GPS_speed']=[]

    for i in range(len(df_dict["time"])):
        #插入片段的位置
        final_dict['time'].append(df_dict["time"][i])
        final_dict['GPS_speed'].append(df_dict["GPS_speed"][i])
        for m in range(len(timeindex_num)):

            if (i==timeindex_num[m][0]):
                new_time_series=date_range_series(timeindex_num[m][1],timeindex_num[m][2]+1)
    #             print(data_dict["GPS_speed"][i])
    #             print(data_dict["GPS_speed"][int(i+timeindex_num[m][2])])
    #             print(timeindex_num[m][2])
                new_speed_series=linear_fit(df_dict["GPS_speed"][i],df_dict["GPS_speed"][int(i+timeindex_num[m][2]-1)],timeindex_num[m][2])
                for j in range(len(new_time_series)):
                    final_dict['time'].append(new_time_series[j])
                    final_dict['GPS_speed'].append(new_speed_series[j])
            
    return final_dict


#获取汽车行驶的每个时间片段
def speed_detection(final_dataframe):
    df_new=final_dataframe[final_dataframe["GPS_speed"]!=0]
    index=df_new.index.values
    # df_new["index"]=list(range(df_new.shape[0]))

    # print(df_new.head(500))
    final_data_dict={}
    final_data_dict["time"]=list(final_dataframe['time'].values)
    final_data_dict["GPS_speed"]=list(final_dataframe['GPS_speed'].values)

    tmp1 =0  # 标记片段开始
    indice=[]
    record = []

    for i in range(len(index)-1):
        if (index[i+1]==(index[i]+1)):
            tmp1=tmp1+1
        else:   
            tmp1=tmp1+1
            indice.append(tmp1)
    index[indice[0]-1]
    #查找每个片段
    record.append([final_data_dict["time"][0:index[indice[0]-1]+1],final_data_dict["GPS_speed"][0:index[indice[0]-1]+1]])
    for i in range(len(indice)-1):       
        record.append([final_data_dict["time"][index[indice[i]-1]+1:index[indice[i+1]-1]+1],final_data_dict["GPS_speed"][index[indice[i]-1]+1:index[indice[i+1]-1]+1]])
    return record


#求每个片段的瞬时加速度
def instantaneous_acceleration(record):
    #求每个片段的瞬时加速度
    accelerationtime_indice=[]
    for i in range(len(record)): 
        tmp=[]
        for j in range(len(record[i][1])-1):
            tmp.append(record[i][1][j+1]-record[i][1][j])
        accelerationtime_indice.append(count_num(tmp,0.36))
    return accelerationtime_indice

#画出第num个时间片段的轨迹
def plot1(record,num):
    fig = plt.figure(figsize=(15, 4))
    ax11 = fig.add_subplot(111)
    #这里14代表第十四个片段，需要画那个片段图，只需修改此值即可
    ax11.plot(record[num][1])
    ax11.set_ylabel('v km/h')
    ax11.set_xlabel('time/s')
    fig.savefig('./data/'+'%s'%(str(num))+'.png')

#处理流程
def caculate_process(df,output_path):
    data_dict={}

    #stepl：数据格式转化
    df=data_preconditon(df)
    df_new=df.shift(axis=0) #将dataframe数据下移一行
    data_new=df-df_new

    #step2：查找时间缺失小于180s的位置
    df_filter=filter_timeseries(data_new)
    data_dict["time"]=list(df['time'].values)
    timeindex_num=get_timeindex_num(df_filter,data_dict["time"])
    data_dict["GPS_speed"]=list(df['GPS_speed'].values)

    # step3：补全时间缺失小于180s的值
    completion_timeseries=completion_misstime(data_dict,timeindex_num)
    final_data=pd.DataFrame.from_dict(completion_timeseries,orient="index").T
    final_data.to_csv('%s'%(output_path)) # 保存补全后的数据

    # step4：获取汽车行驶的每个时间片段
    time_indice=speed_detection(final_data)
    
    # step5：计算汽车行驶的每个时间片段加速时间
    accelerationtime_indice=instantaneous_acceleration(time_indice)
    file_path='./data/accelerationtime_indice.txt'
    write_data(file_path,accelerationtime_indice)
    plot1(time_indice,2)
