import numpy as np
import pandas as pd
from utils import * 
def main():
    df = pd.read_csv("data\GPS2-2021-07-31.csv")
    #step1：数据统计   
    # set_route_piont为输入经纬度坐标，作为航迹必过点
    set_route_piont = [(119.668571,39.860154),(119.686392,39.832062),(119.647934,39.898554)]
    df_new = calculate_course_angle(df)
    df_new["course_angle_error"] = df_new["HeadingAngle"] - df_new["angle"]
    record_dict = data_statistics(set_route_piont,df)
    #step2：画图
    plot_trajectory_intervals(record_dict,set_route_piont)   
    
if __name__ == '__main__':
	main()