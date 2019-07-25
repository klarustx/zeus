import numpy as np
import pandas as pd
import sys
import utils

def statistic_major(input_path):
    df = pd.read_csv(open(r'%s'%(input_path)),encoding='utf-8')
    major_name = list(set(df['专业名称'].values))
    for item in major_name:
        data_major = df[df["专业名称"]==item]
        output_path = './data2/%s.csv'%(item)
        data_mid = utils.datastyle_transform(data_major)
        data_final = utils.rank_score(data_mid)
        data_final.to_csv('%s'%(output_path),index=False, encoding="utf_8_sig")#把数据导出成
if __name__ == '__main__':
    input_path = sys.argv[1]
    statistic_major(input_path)
