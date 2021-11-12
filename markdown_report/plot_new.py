#!/usr/bin/env python
# coding=utf-8
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

gmv = 0
cost = 0
order = 0

def LoadSimulationParams(param_file):
    """
    读取参数空间文件，并判断是否需要过滤掉(0, 0, 0)的情况
    """
    param_dict = {}
    with open(param_file) as f:
        for line in f.readlines():
            #print(line)
            [key, gmv, order, cost] = line.strip().split('\t')
            value = (float(gmv), float(order), float(cost))
#             key, value = eval(line)
            #print(cost)
            #param_dict[key] = value
            if float(cost) > 1.0:
                param_dict[key] = value
            
#     if (is_remove_zeros):
#         print(param_dict.items())
#         param_dict = dict((lambda x: sum(x[1]), param_dict.items()))
    #print (param_dict)
    return param_dict


def PrepareParams(param_file):
    """
    从文件读取评估结论样本(eval_file)；从文件读取参数列表(params_file)并找到更优参数
    """
    global gmv, cost, order
    '''
    with open(eval_file) as f:
        for line in f.readlines():
            if (line.find('PREDICTION = ') == 0):
                gmv, cost, order = eval(line.replace('PREDICTION =', ''))
    '''
    params = LoadSimulationParams(param_file)
    
    better_params = zip(*filter(lambda x: all((x[0] > gmv, x[1] < cost, x[2] > order)), params.values()))
    print(better_params)
    if not better_params:
        better_params = [[], [], []]
    
    return zip(*params.values()), better_params
def check(pd_data, start, end, stepsize):
        # Generate checkpoints
    checkpoint_num = int((end - start) / stepsize + 1)
    checkpoint = np.linspace(start, end, checkpoint_num)
    xx=[]
    yy=[]
        
    for ck in checkpoint:
        pd_dataset = pd_data[(pd_data["Cost"]< ck + checkpoint_num) && (pd_data["Cost"] > ck - checkpoint_num)] ## index in [ck-checkpoint_num,ck+checkpoint_num]
        xx.append(ck)
        yy.append(max(list(pd_dataset["GMV"].values)))
    return (xx,yy)


def Plot(params, better_params):
    """
    画三个指标的散点图
    +: 参数空间结果
    o: 比当前结果更优的结果
    d: 当前结果
    """
    plt.switch_backend('agg')
    plt.figure(figsize=(21, 7), dpi=64)
    mpl.rcParams['agg.path.chunksize'] = 10000
    params = list(params)
    better_params = list(better_params)
    print(len(params),len(better_params))
    p_cost_gmv = plt.subplot(131)
    print('better_params:',better_params)
    '''
    params_dict={}
    params_dict['GMV']=list(map(int,np.array(params[0])/10000))
    params_dict['Order']=list(map(int,np.array(params[1])/10000))
    params_dict['Cost']=list(map(int,np.array(params[2])/10000))
   # print(type(params))
    
    params_dataframe=pd.DataFrame(params_dict)
    #params_dataframe.columns=['GMV','Order','Cost']
    
    print(params_dataframe.head(5))
   
   # params_data = pd.pivot_table(params_dataframe,index=["Cost"])
    params_datagroup = params_dataframe.groupby(["Cost"],as_index=False).max()
    
    print(params_datagroup.head(5))
    print(type(params_datagroup))
    params[2]= list(np.array(params_datagroup["Cost"])*10000)
    params[0]= list(np.array(params_datagroup["GMV"])*10000)
    params[1]= list(np.array(params_datagroup["Order"])*10000)
    '''
    params_dict={}
    params_dict['GMV']=list(map(int,params[0]))
    params_dict['Order']=list(map(int,params[1]))
    params_dict['Cost']=list(map(int,params[2]))
   # print(type(params))
    params_dataframe = pd.DataFrame(params_dict)
    (xx,yy)=check(params_dataframe, 1000,300000,1000)


    params_dataframe_cost = params_dataframe.sort_values(by="Cost")
    x = range(1000,300000,1000)
    y = [1.5 * i for i in x]
    cost_gmv=list(zip(list(params_dataframe_cost.cost.values),list(params_dataframe_cost.gmv.values))
    yy=[]                      
    
    p_cost_gmv = plt.plot(xx, yy, '+',color='red',alpha=0.1,label='gmv')
   # p_cost_gmv = plt.plot(params[2], params[0], '+',color='red',alpha=0.1,label='gmv')
    plt.legend()                        #显示图例。
    plt.show()
    #p_cost_gmv = plt.plot(params[2], params[0])
    plt.xlabel('Cost')
    plt.ylabel('GMV')

    p_order_gmv = plt.subplot(132)
    p_order_gmv = plt.plot(params[1], params[0], '+',color='red',alpha=0.1,label='gmv')
    plt.legend()                        #显示图例。
    plt.show()
    print(min(params[0]), max(params[0]))
    #p_order_gmv = plt.plot(params[1], params[0])
#         p_order_gmv = plt.plot(params[0], params[2], '+', 'o', gmv, order, 'rd')
    plt.xlabel('Order')
    plt.ylabel('GMV')

    p_cost_order = plt.subplot(133)
    x = range(1000,300000,1000)
    y = [1.5 * i for i in x]
    #p_cost_order = plt.plot(params[2], params[1])
    p_cost_order = plt.plot(params[2], params[1], '+',color='red',alpha=0.1,label='gmv') 
                            #, y, x, 'rd') #, 'o', order, cost, 'rd')
    # p_cost_order = plt.plot(params[1], params[2], '+', 'o', order, cost, 'rd')
    plt.legend()                        #显示图例。
    plt.show()
    plt.xlabel('Cost')
    plt.ylabel('Order')

    #plt.legend(p_cost_gmv, ['parameter space simulation', 'better than current', 'current prediction'], loc = 'best')
    plt.savefig("/nfs/private/tangxu/democode/distribution.png")

def main():
    #eval_file, figure_file = GetInputPaths(param_file)
    #figure_file = GetInputPaths(param_file)
    #params, better_params = PrepareParams(param_file, eval_file, is_remove_zeros)
    param_file=sys.argv[1]
    #params_dict=LoadSimulationParams(param_file)
    params, better_params = PrepareParams(param_file)
    Plot(params, better_params)
    
#    print type(params), len(params)#, len(params[0])
#    print type(better_params), len(better_params)#, len(better_params[0])
    print("GMV=%.2f, Cost=%.2f, Order=%.2f" % (gmv, cost, order))

if __name__ == '__main__':
    main()
