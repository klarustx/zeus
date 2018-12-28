import json
import sys
import matplotlib
matplotlib.use('Agg')
from util import  describe_figure
from markdown_report import MarkdownReport
import yaml
import pandas as pd
import numpy as np

report = MarkdownReport()
def figure_report(inputpath_hour,inputpath_distance,inputpath_rprate,inputpath_NDSDI,params_path,outputpath, report_name):
    global_conf_hour =pd.read_csv("%s"%(inputpath_hour),sep="\t", header=None)
    global_conf_distance =pd.read_csv("%s"%(inputpath_distance),sep="\t", header=None)
    global_conf_rprate =pd.read_csv("%s"%(inputpath_rprate),sep="\t", header=None)
    global_conf_NDSDI =pd.read_csv("%s"%(inputpath_NDSDI),sep="\t", header=None)
    #global_conf_hour =pd.read_csv("/home/luban/xuelijiao/scala_simulation/plot_data/11_182292_20181203183206_hour.csv",sep="\t", header=None)
    #global_conf_distance =pd.read_csv("/home/luban/xuelijiao/scala_simulation/plot_data/11_182292_20181203183206_distance.csv",sep="\t", header=None)
    #global_conf = yaml.load(f)
    global_conf_hour.columns = ['hour','gmv','subsidy','ecr','discount_ecr','alldiscount_ecr']
    global_conf_distance.columns = ['distance','gmv','subsidy','ecr','discount_ecr','alldiscount_ecr']
    global_conf_rprate.columns = ['rprate','bubble','percent']
    global_conf_NDSDI.columns = ['NDSDI','bubble','percent']
    global_conf_hour=global_conf_hour.sort_values(by='hour')
    global_conf_distance=global_conf_distance.sort_values(by="distance")
    global_conf_distance_special=global_conf_distance[global_conf_distance['distance']>20]
    global_conf_distance_normal=global_conf_distance[global_conf_distance['distance']<=20]
    global_conf_distance_special.loc['Row_sum'] = global_conf_distance_special.apply(lambda x: x.sum())
    #print global_conf_distance_special.loc['Row_sum'].values
    #print global_conf_distance_special
    global_conf_distance_normal.loc['Row_sum'] = global_conf_distance_special.loc['Row_sum'].values
    global_conf_distance_normal.loc['Row_sum']['distance']=21
    global_conf_distance = global_conf_distance_normal
    #print global_conf_distance_special2
    #print (global_conf)
    global_conf_hour_dict={'hour':[],'gmv':[],'subsidy':[],'ecr':[],'discount_ecr':[],'alldiscount_ecr':[]}
    global_conf_hour_dict['hour']=list(global_conf_hour['hour'].values)
    global_conf_hour_dict['gmv']=list(global_conf_hour['gmv'].values)
    global_conf_hour_dict['subsidy']=list(global_conf_hour['subsidy'].values)
    global_conf_hour_dict['ecr']=list(global_conf_hour['ecr'].values)
    global_conf_hour_dict['discount_ecr']=list(global_conf_hour['discount_ecr'].values)
    global_conf_hour_dict['alldiscount_ecr']=list(global_conf_hour['alldiscount_ecr'].values)
    
    global_conf_distance_dict={'distance':[],'gmv':[],'subsidy':[],'ecr':[],'discount_ecr':[],'alldiscount_ecr':[]}
    global_conf_distance_dict['distance']=list(global_conf_distance['distance'].values)
    global_conf_distance_dict['gmv']=list(global_conf_distance['gmv'].values)
    global_conf_distance_dict['subsidy']=list(global_conf_distance['subsidy'].values)
    global_conf_distance_dict['ecr']=list(global_conf_distance['ecr'].values)
    global_conf_distance_dict['discount_ecr']=list(global_conf_distance['discount_ecr'].values)
    global_conf_distance_dict['alldiscount_ecr']=list(global_conf_distance['alldiscount_ecr'].values)
    
    
    global_conf_rprate_dict={'rprate':[],'percent':[]}
    global_conf_rprate_dict['rprate']=list(global_conf_rprate['rprate'].values)
    global_conf_rprate_dict['percent']=list(global_conf_rprate['percent'].values)
    
    global_conf_NDSDI_dict={'NDSDI':[],'percent':[]}
    global_conf_NDSDI_dict['NDSDI']=list(global_conf_NDSDI['NDSDI'].values)
    global_conf_NDSDI_dict['percent']=list(global_conf_NDSDI['percent'].values)
    
    
    #print global_conf_hour_dict
    #report.write_h1("{0}模拟结果".format(global_conf['city_name']))
    #report.write_line("城市: {0}\n".format(global_conf['city_name']))
    #report.write_line("City ID: {0}\n".format(global_conf['city_id']))
   # report.write_line("实验周期: {0}\n".format(str(global_conf['start_date']) + " - " + str(global_conf['end_date'])))
    report.write_line("实验折扣: 0.8 - 0.95， 步长：0.05\n")
    describe_figure(global_conf_hour_dict, global_conf_distance_dict,global_conf_rprate_dict,global_conf_NDSDI_dict,params_path,report)
    #describe_figure(global_conf_distance_dict, report)
    report.save_html("%s/%s_report.html"%(outputpath, report_name))
    #report.save_markdown("%s/report.mk"%(outputpath))
    
def main():
    inputpath_hour=sys.argv[1]
    inputpath_distance=sys.argv[2]
    inputpath_rprate=sys.argv[3]
    inputpath_NDSDI=sys.argv[4] 
    params_path=sys.argv[5] 
    outputpath=sys.argv[6]
    report_name = sys.argv[7]
    figure_report(inputpath_hour,inputpath_distance,inputpath_rprate,inputpath_NDSDI,params_path,outputpath, report_name)
if __name__ == "__main__":
    main()


