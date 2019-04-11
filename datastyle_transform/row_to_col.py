# coding=utf-8
import numpy as np
import pandas as pd
import sys

def datastyle_transform(input_path,output_path):
    df = pd.read_csv(open(r'%s'%(input_path)),encoding='utf-8')
    data = df[["课程编号","课程名称","学号","姓名","总成绩","班级编号"]]
    new_cols = list(set(data['课程名称'].values))
    new_cols.insert(0,'学号')
    new_cols.insert(1,'姓名')
    new_cols.insert(2,'班级编号')
    new_cols.remove(np.nan)
    sno = list(set(data['学号'].values))
    data_new = pd.DataFrame(columns=new_cols)
    dict_new = {col:data_new[col].tolist() for col in data_new.columns}

    #将课程信息存到字典中
    for i in sno:
        tmp = data[data["学号"]==i]
        sname=list(tmp['姓名'].values)[0]
        sclass=list(tmp['班级编号'].values)[0]
        dict_new["学号"].append(i)
        dict_new["姓名"].append(sname)
        dict_new["班级编号"].append(sclass)
        cname = list(tmp["课程名称"].values)
        score = list(tmp["总成绩"].values)
        for j in range(len(cname)):
            dict_new["%s"%(cname[j])].append(score[j])
        for key in dict_new:
            if key not in cname:
                if (key!='学号')&(key!="姓名")&(key!="班级编号"):
                    dict_new["%s"%(key)].append(1)

     #将字典变成dataframe
    dfs= pd.DataFrame.from_dict(dict_new, orient='index').T
    dfs_new = dfs.dropna(axis = 0)
    dfs_final = dfs_new.replace(1, np.nan)
    dfs_final.to_csv('%s'%(output_path), index=True, header=True,encoding="utf_8_sig")#把数据导出成.CSV格式 

if __name__ == '__main__':
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    datastyle_transform(input_path,output_path)
