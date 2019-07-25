# coding=utf-8
import numpy as np
import pandas as pd

def datastyle_transform(df):
    # df = pd.read_csv(open(r'%s'%(input_path)),encoding='utf-8')
    data = df[["课程编号","课程名称","学号","姓名","总成绩","导师","专业名称"]]
    # datas= data[data["课程名称"]=='学术道德与论文写作（理）']
    # print(datas)
    new_cols = list(set(data['课程名称'].values))
    new_cols.insert(0,'学号')
    new_cols.insert(1,'姓名')
    new_cols.insert(2,'专业名称')
    new_cols.insert(3, '导师')
    # new_cols.remove(np.nan)
    sno = list(set(data['学号'].values))
    data_new = pd.DataFrame(columns=new_cols)
    dict_new = {col:data_new[col].tolist() for col in data_new.columns}

    #将课程信息存到字典中
    for i in sno:
        tmp = data[data["学号"]==i]
        sname=list(tmp['姓名'].values)[0]
        sclass=list(tmp['专业名称'].values)[0]
        teacher = list(tmp['导师'].values)[0]
        dict_new["学号"].append(i)
        dict_new["姓名"].append(sname)
        dict_new["专业名称"].append(sclass)
        dict_new["导师"].append(teacher)
        cname = list(tmp["课程名称"].values)
        score = list(tmp["总成绩"].values)
        for j in range(len(cname)):
            dict_new["%s"%(cname[j])].append(score[j])
        for key in dict_new:
            if key not in cname:
                if (key!='学号')&(key!="姓名")&(key!="专业名称")&(key!="导师"):
                    dict_new["%s"%(key)].append(0)

     #将字典变成dataframe
    dfs= pd.DataFrame.from_dict(dict_new, orient='index').T
    dfs_new = dfs.dropna(axis = 0)
    return dfs_new

    # dfs_final.to_csv('%s'%(output_path), index=False,sep=' ', header=True,encoding="utf_8_sig")#把数据导出成.CSV格式


def rank_score(df):
    key = list(df.columns)
    key1 = ('学号', '姓名', '专业名称', '导师')
    for item1 in key1:
        key.remove(item1)
    dict_new = {"学号": [], "总分": [], "百分比": []}
    sno = list(df['学号'].values)
    for item2 in sno:
        tmp = df[df["学号"] == item2]
        score = 0;
        dict_new["学号"].append(item2)
        for item3 in key:
            score = score + tmp[item3].values[0]
        #         print(tmp[item3].values)
        dict_new["总分"].append(score)

    total_score = sum(dict_new["总分"])

    # dict_new["百分比"] = list(dict_new["总分"] / total_score)
    for item3 in list(dict_new["总分"]):
        dict_new["百分比"].append(item3/total_score)

    data_new = pd.DataFrame.from_dict(dict_new, orient='index').T
    data_final = data_new.sort_values(by=["总分"], ascending=(False))
    data_final["学号"] = data_final["学号"].astype('int')
    num_list = list(range(len(dict_new["学号"])))
    rank_list = [item + 1 for item in num_list]
    data_final["排名"] = rank_list
    # df["学号"]=df["学号"].astype('int')
    data_finish = pd.merge(data_final, df, on=["学号"], how='inner')
    dfs_final = data_finish.replace(0, np.nan)
    return dfs_final