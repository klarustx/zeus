import  sys
import io
from optparse import OptionParser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import matplotlib as mpl
def get_plot_binary(fig):
    canvas = fig.canvas
    buffer = io.BytesIO()
    canvas.print_png(buffer)
    data=buffer.getvalue()
    buffer.close()
    return data

def describe_figure(df_hour,df_distance,percent_rprate,percent_ndsdi,params_path,report):
    
    #分时补贴率
    fig1 = plt.figure(figsize=(15, 4))
    #plt.style.use('seaborn-white')
    plt.style.use('seaborn-whitegrid')
    # 正常显示中文字体
    mpl.rcParams[u'font.sans-serif'] = ['simhei']
    mpl.rcParams['axes.unicode_minus'] = False
    font = {'fontsize': 7, }
    font2 = {'fontsize': 6, }    
    ax11 = fig1.add_subplot(131)
    plt.xticks([x for x in range(25) if x % 2 == 0])  # x标记step设置为2
    roi_hour=list(np.array(df_hour['subsidy'])/np.array(df_hour['gmv']))
#    xnew = np.linspace(0,24,300)  #300 represents number of points to make between T.min and T.max
#    power_smooth = spline(df_hour['hour'],roi_hour,xnew)
#    ax11.plot(xnew, power_smooth)
    ax11.plot(df_hour['hour'], roi_hour,color='blue', marker='o', linestyle='solid')
    ax11.set_ylabel('subsidy_rate')
    ax11.set_xlabel('hour(h)')
    ax11.set_title("Subsidy rate for hour",color="black")
    #ax11.legend(loc="upper right", facecolor='white')    
  #  ax11.grid(axis='y', alpha=0.5)
    #ax111 = ax11.twinx()
   # ax111.scatter(df_hour['hour'],roi_hour, color='black')
    #total_fig1 = get_plot_binary(fig1)
    #report.write_h2("分时补贴率")
   # report.write_img("dri_discount1", total_fig1)
   # plt.savefig("/nfs/private/tangxu/scala_figure/distribution.png")
   # df_dataframe=pd.DataFrame(df_hour)
    #df_dataframe=df_dataframe[['hour',,'gmv','subsidy']]
    #df.columns = ['hour', 'gmv', 'ECR', '冒泡占比', '订单占比', 'Delta ECR']
    #report.write_line(df_dataframe.to_html(index=False))
   
    #分时打折订单占比
    #fig2 = plt.figure(figsize=(6, 4))
    plt.style.use('seaborn-whitegrid')
    font = {'fontsize': 15, }
    font2 = {'fontsize': 10, }    
    ax12 = fig1.add_subplot(132)
    plt.xticks([x for x in range(25) if x % 2 == 0])  # x标记step设置为2
    discount_percent_hour=list(np.array(df_hour['discount_ecr'])/np.array(df_hour['ecr']))
    #xnew = np.linspace(0,24,300)
    #power_smooth = spline(df_hour['hour'],discount_percent_hour,xnew)
   # ax12.plot(xnew, power_smooth)
    ax12.plot(df_hour['hour'], discount_percent_hour,color='blue', marker='o', linestyle='solid')
    ax12.set_ylabel('discount_percent')
    ax12.set_xlabel('hour(h)')
    ax12.set_title("Discount order proporition for hour", color="black") 
    #ax121 = ax12.twinx()
    #ax121.scatter(df_hour['hour'],discount_percent_hour, color='black')
    #total_fig2 = get_plot_binary(fig2)
    #report.write_h2("分时打折订单占比")
   # report.write_img("dri_discount2", total_fig2)

    #分时单单打折订单占比
    #fig3 = plt.figure(figsize=(6, 4))
    plt.style.use('seaborn-whitegrid')
    #plt.grid(False)
    font = {'fontsize': 15, }
    font2 = {'fontsize': 10, }    
    ax13 = fig1.add_subplot(133)
    plt.xticks([x for x in range(25) if x % 2 == 0])  # x标记step设置为2
    alldiscount_percent_hour=list(np.array(df_hour['alldiscount_ecr'])/np.array(df_hour['ecr']))
    #xnew = np.linspace(0,24,300)
    #power_smooth = spline(df_hour['hour'],alldiscount_percent_hour,xnew)
    #ax13.plot(xnew, power_smooth)
    ax13.plot(df_hour['hour'],alldiscount_percent_hour,color='blue', marker='o', linestyle='solid')
    ax13.set_ylabel('discountall_percent')
    ax13.set_xlabel('hour(h)')
    ax13.set_title("Discountall order proporition for hour",color="black")
    #ax1.legend(loc="upper right", facecolor='white')    
  #  ax13.grid(axis='y', alpha=0.5)
   # ax131 = ax13.twinx()
    #ax131.scatter(df_hour['hour'],alldiscount_percent_hour, color='black')
    total_fig3 = get_plot_binary(fig1)
    report.write_h2("分时补贴率、分时打折订单占比、分时单单打折订单占比")
    report.write_img("dri_discount3", total_fig3)
    
    #分里程补贴率
    fig4 = plt.figure(figsize=(15, 4))
    plt.style.use('seaborn-whitegrid')
    font = {'fontsize': 15, }
    font2 = {'fontsize': 10, }    
    ax21 = fig4.add_subplot(131)
    plt.xticks([x for x in range(22) if x % 2 == 0])  # x标记step设置为2
    roi_distance=list(np.array(df_distance['subsidy'])/np.array(df_distance['gmv']))
    #xnew = np.linspace(0,21,300)
    #power_smooth = spline(df_distance['distance'],roi_distance,xnew)
    #ax21.plot(xnew, power_smooth)
    ax21.plot(df_distance['distance'],roi_distance,color='blue', marker='o', linestyle='solid')
    ax21.set_ylabel('subsidy_rate')
    ax21.set_xlabel('distance(km)')
    ax21.set_title("Subsidy rate for distance")
    #ax21.legend(loc="upper right", facecolor='white')    
  #  ax21.grid(axis='y', alpha=0.5)
  #  ax211 = ax21.twinx()
  #  ax211.scatter(df_distance['distance'],roi_distance, color='black')
    #total_fig4 = get_plot_binary(fig4)
    #report.write_h2("分里程补贴率")
    #report.write_img("dri_discount4", total_fig4)
    
    #分里程打折订单占比
    #fig5 = plt.figure(figsize=(6, 4))
   # plt.style.use('seaborn-whitegrid')
    font = {'fontsize': 15, }
    font2 = {'fontsize': 10, }    
    ax22 = fig4.add_subplot(132)
    plt.xticks([x for x in range(22) if x % 2 == 0])  # x标记step设置为2
    discount_percent_distance=list(np.array(df_distance['discount_ecr'])/np.array(df_distance['ecr']))
    #xnew = np.linspace(0,21,300)
    #power_smooth = spline(df_distance['distance'],discount_percent_distance,xnew)
    #ax22.plot(xnew, power_smooth)
    ax22.plot(df_distance['distance'],discount_percent_distance,color='blue', marker='o', linestyle='solid')
    ax22.set_ylabel('discount_percent_distance')
    ax22.set_xlabel('distance(km)')
    ax22.set_title("Discount order proporition for distance")
  #  ax221 = ax22.twinx()
  #  ax221.scatter(df_distance['distance'],discount_percent_distance, color='black')
  #  total_fig5 = get_plot_binary(fig5)
  #  report.write_h2("分里程打折订单占比")
 #   report.write_img("dri_discount5", total_fig5)
    
    
    #分里程单单打折订单占比
    #fig6 = plt.figure(figsize=(6, 4))
    plt.style.use('seaborn-whitegrid')
    #plt.grid(False)
    font = {'fontsize': 15, }
    font2 = {'fontsize': 10, }    
    ax23 = fig4.add_subplot(133)
    plt.xticks([x for x in range(22) if x % 2 == 0])  
    alldiscount_percent_distance=list(np.array(df_distance['alldiscount_ecr'])/np.array(df_distance['ecr']))
    #xnew = np.linspace(0,21,300)
    #power_smooth = spline(df_distance['distance'],alldiscount_percent_distance,xnew)
    #ax23.plot(xnew, power_smooth)
    ax23.plot(df_distance['distance'], alldiscount_percent_distance,color='blue', marker='o', linestyle='solid')
    ax23.set_ylabel('discountall_percent_distance')
    ax23.set_xlabel('distance(km)')
    ax23.set_title("Discountall order proporition for distance",color="black")
   # ax23.legend(loc="upper right", facecolor='white')    
   # ax23.grid(axis='y', alpha=0.5)
 #   ax231 = ax23.twinx()
 #   ax231.scatter(df_distance['distance'], alldiscount_percent_distance, color='black')
    total_fig6 = get_plot_binary(fig4)
    report.write_h2("分里程补贴率、分里程打折订单占比、分里程单单打折订单占比")
    report.write_img("dri_discount6", total_fig6)
   

    #rpate占比
    fig7 = plt.figure(figsize=(15, 5))
    plt.style.use('seaborn-whitegrid')
    #plt.grid(False)
    font = {'fontsize': 15, }
    font2 = {'fontsize': 10, }    
    ax31 = fig7.add_subplot(121)
    #plt.xticks(list(np.array([x for x in range(80,101) if (100*x) % 2 == 0])/10))  # x标记step设置为0.2
    #alldiscount_percent_distance=list(np.array(percent_rprate['rprate'])/np.array(df_distance['ecr']))
    #xnew = np.linspace(0.8,1.0,300)
    #power_smooth = spline(percent_rprate['rprate'],percent_rprate['percent'],xnew)
    #ax31.plot(xnew, power_smooth)
    ax31.plot(percent_rprate['rprate'], percent_rprate['percent'],color='blue', marker='o', linestyle='solid')
    #ax1.plot(df_distance['distance'], alldiscount_percent2, "-*")
    ax31.set_ylabel('percent')
    ax31.set_xlabel('rprate)')
    ax31.set_title("bubble percent for rprate ",color="black")
   # ax31.legend(loc="upper right", facecolor='white')    
    #ax31.grid(axis='y', alpha=0.5)
 #   ax311 = ax31.twinx()
 #   ax311.scatter(percent_rprate['rprate'], percent_rprate['percent'], color='black')
    #total_fig7 = get_plot_binary(fig7)
    #report.write_h2("不同rprate对应的冒泡数")
   # report.write_img("dri_discount7", total_fig7)
    
    #NDSDI占比
    #fig8 = plt.figure(figsize=(6, 4))
    plt.style.use('seaborn-whitegrid')
    #plt.grid(False)
    font = {'fontsize': 15, }
    font2 = {'fontsize': 10, }    
    ax32 = fig7.add_subplot(122)
    #plt.xticks([x for x/100 in range(20) if (100*x) % 2 == 0])  # x标记step设置为2
    #alldiscount_percent_distance=list(np.array(df_distance['alldiscount_ecr'])/np.array(df_distance['ecr']))
    
    #xnew = np.linspace(0,2.1,300)
    #spline(percent_ndsdi['NDSDI'],percent_ndsdi['percent'],xnew)
    #ax32.plot(xnew, power_smooth)
    ax32.plot(percent_ndsdi['NDSDI'], percent_ndsdi['percent'],color='blue', marker='o', linestyle='solid')
    ax32.set_ylabel('percent')
    ax32.set_xlabel('NDSDI')
    ax32.set_title("bubble percent for distance",color="black")
   # ax32.legend(loc="upper right", facecolor='white')    
    #ax32.grid(axis='y', alpha=0.5)
 #   ax321 = ax32.twinx()
 #   ax321.scatter(percent_ndsdi['NDSDI'], percent_ndsdi['percent'], color='black')
    total_fig8 = get_plot_binary(fig7)
    report.write_h2("不同rprate、NDSDI对应的冒泡比例")
    report.write_img("dri_discount8", total_fig8)
    with open("%s"%(params_path), "rb") as imageFile:
        f= imageFile.read()
        total_fig9 = bytes(f)
    report.write_h2("模拟参数分布")
    report.write_img("dri_discount9", total_fig9)

