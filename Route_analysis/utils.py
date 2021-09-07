import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
# 计算两点的航向角
def get_angle(lng_a, lat_a, lng_b, lat_b):
    y = math.sin(lng_b - lng_a) * math.cos(lat_b)
    x = math.cos(lat_a) * math.sin(lat_b) - math.sin(lat_a) * math.cos(lat_b) * math.cos(lng_b - lng_a)
    angle = math.atan2(y, x)
    pi = 3.1415926
    angle= (180 * angle) / pi
    if (angle < 0):
        angle = -angle;
    else:
        angle = 360 - angle;
    return angle
# 经纬度转换为guass坐标系下坐标
def GaussToBLToGauss(longitude,latitude):

     iPI = 0.0174532925199433; #3.1415926535898/180.0;
     ZoneWide = 6; #6度带宽
    #  a=6378245.0
    #  f=1.0/298.3 #54年北京坐标系参数
     a=6378140.0
     f=1/298.257; #80年西安坐标系参数
     ProjNo = (int)(longitude / ZoneWide)
     longitude0 = ProjNo * ZoneWide + ZoneWide / 2
     longitude0 = longitude0 * iPI 
     latitude0 = 0
     longitude1 = longitude * iPI   #经度转换为弧度
     latitude1 = latitude * iPI    #纬度转换为弧度
     e2 = 2*f-f*f
     ee = e2*(1.0-e2)
     NN = a / math.sqrt(1.0-e2 * math.sin(latitude1) * math.sin(latitude1))
     T = math.tan(latitude1) * math.tan(latitude1)
     C = ee*math.cos(latitude1) * math.cos(latitude1)
     A = (longitude1-longitude0) * math.cos(latitude1)
     M = a*((1-e2/4-3*e2*e2/64-5*e2*e2*e2/256)*latitude1-(3*e2/8+3*e2*e2/32+45*e2*e2
     *e2/1024)*math.sin(2*latitude1)+(15*e2*e2/256+45*e2*e2*e2/1024)*math.sin(4*latitude1)-
            (35*e2*e2*e2/3072)*math.sin(6*latitude1))
     xval = NN*(A+(1-T+C)*A*A*A/6+(5-18*T+T*T+72*C-58*ee)*A*A*A*A*A/120)
     yval = M+NN*math.tan(latitude1)*(A*A/2+(5-T+9*C+4*C*C)*A*A*A*A/24
     +(61-58*T+T*T+600*C-330*ee)*A*A*A*A*A*A/720);
     X0 = 1000000*(ProjNo+1)+500000
     Y0 = 0
     xval = xval+X0
     yval = yval+Y0
     X = xval
     Y = yval
     return X,Y
 
# 两点确定直线：Ax + By + C =0
def get_straight_line(x1,y1,x2,y2):
    A = y2 - y1
    B = x1 - x2
    C = - A * x1 - B * y1
    return (A,B,C)

#查找处于该区间的航迹点
def search_piont_intervals(lng_a, lat_a, lng_b, lat_b,df):
    df_sp1 = df[(df['lng']==lng_a) & (df['lat']==lat_a)]
    df_sp2 = df[(df['lng']==lng_b) & (df['lat']==lat_b)]
    index1 = df_sp1.index.values
    index2 = df_sp2.index.values
    df_slice = df.iloc[index1[0]:index2[0]+1] 
    return df_slice

# set_route_piont为字典  例子：dict = [(3,4),(6,7)]
#统计每个直线区域内的航迹点
def sort_By_intervial(set_route_piont,df):
    record_dict = {}
    for i in range(len(set_route_piont)-1):
        df_slice = search_piont_intervals(set_route_piont[i][0],set_route_piont[i][1],set_route_piont[i+1][0],set_route_piont[i+1][1],df)       
        x1,y1 = GaussToBLToGauss(set_route_piont[i][0],set_route_piont[i][1])
        x2,y2 = GaussToBLToGauss(set_route_piont[i+1][0],set_route_piont[i+1][1])
        A,B,C = get_straight_line(x1,y1,x2,y2)
        record_dict[str(i)] =[]
        num = df_slice.shape[0]
        lng_list = df_slice['lng'].values 
        lat_list = df_slice['lat'].values
        for j in range(num):
            x,y = GaussToBLToGauss(lng_list[j],lat_list[j])
            dist = abs(A * x + B * y + C)/math.sqrt(A*A + B*B);  #计算点到直线的距离
            record_dict[str(i)].append((x,y,dist))
    return record_dict

def data_statistics(set_route_piont,df):
    record_dict = sort_By_intervial(set_route_piont,df)
    # set_route_piont[0][1]
    record_dict
    dist_list ={}
    f = open('data\result.txt','a')
    for key in record_dict.keys():
        dist_list[key] =[]
        f.write('区间:'+ key)
        f.write('\n')
        for item in record_dict[key]:
            dist_list[key].append(item[2])
            f.write('坐标点'+ '('+ str(item[0]) + ',' + str(item[1]) + ')'+'   ')
            f.write('坐标点到直线的距离:'+ str(item[2]))
            f.write('\n')
        print("区间:"+key)
        #求和
        arr_sum = np.sum(dist_list[key])
        #求均值
        arr_mean = np.mean(dist_list[key])
        #求方差
        arr_var = np.var(dist_list[key] )
        #求标准差
        arr_std = np.std(dist_list[key], ddof=1)
        print("误差和为：%f" % arr_sum)
        print("平均值为：%f" % arr_mean)
        print("均方差为：%f" % arr_std)
    f.close()   
    return record_dict

# 计算坐标点和航向角
def calculate_course_angle(df):
   #统计各组经纬度坐标对应的角度值与给定航向角度的误差
    iPI = 0.0174532925199433
    lng_list = df['lng'].values * iPI  
    lat_list = df['lat'].values * iPI 
    x_list = [i*0 for i in range(len(lat_list))]
    y_list =  [i*0 for i in range(len(lat_list))]
    for i in range(len(lat_list)):
        x_list[i], y_list[i] =  GaussToBLToGauss(lng_list[i],lat_list[i])

    angle = []
    for i in range(len(lat_list)-1):
        angle_near = get_angle(lat_list[i], lat_list[i+1], lng_list[i], lng_list[i+1])
        angle.append(angle_near)
    angle.append(angle_near)  #最后一个航迹点对应的航向角用上一个航向角补齐
    df['X']= x_list
    df['Y']= y_list
    df['angle'] = angle 
    return df


#画出航迹图
def plot_trajectory(df):
    # 计算航迹对应的GAUSS坐标系下坐标值
    row = df.shape[0]  #获取数据的列数
    iPI = 0.0174532925199433
    lng_list = df['lng'].values * iPI  
    lat_list = df['lat'].values * iPI 
    x_list = [i*0 for i in range(len(lat_list))]
    y_list =  [i*0 for i in range(len(lat_list))]
   
    for i in range(len(lat_list)):
       x_list[i], y_list[i] =  GaussToBLToGauss(lng[i],lat[i])
    plt.plot(x_list,y_list)

#分区间画出航迹图
def plot_trajectory_intervals(record_dict,set_route_piont):
    #画轨迹图
    xk_list = {}
    yk_list = {}
    plt.figure()
    for key in record_dict.keys():
        xk_list[key] =[]
        yk_list[key] =[]
        for i in range(len(record_dict[key])):
            if(i%10 ==0):
                xk_list[key].append(record_dict[key][i][0])
                yk_list[key].append(record_dict[key][i][1])
        plt.plot(xk_list[key],yk_list[key],color='red')
        
        xk = np.linspace(xk_list[key][0],xk_list[key][-1],200) 
        A,B,C = get_straight_line(xk_list[key][0],yk_list[key][0],xk_list[key][-1],yk_list[key][-1])
        yk = []
        for item in xk:
            yk.append(-(A*item + C) / B)
        plt.plot(xk,yk,color='green')
#     plt.show()
    frame = plt.gca()
    # y 轴不可见
    frame.axes.get_yaxis().set_visible(False)
    # x 轴不可见
    frame.axes.get_xaxis().set_visible(False)