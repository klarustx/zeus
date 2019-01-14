import sys
#coding=utf8
import pandas as pd
import numpy as np
from pyspark import SparkConf, SparkContext
#from utils import *
from pyspark.sql import SparkSession

from pyspark.sql.functions import col, round
import itertools
from numpy import *
from pyspark.sql import Row
import math

m=16
n=m*m
h=1.0/(m+1)
t=h

def tridiag(kk1,kk2,kk3,k):
    F=mat(kk2*np.eye(k))
    print(type(F))
    FR=[1 for i in range(k-1)]
    Q1=mat(kk1*np.diag(FR,1))
    Q2=mat(kk3*np.diag(FR,-1))
    Q=Q1+F+Q2
    return Q

#(W,T,b)=prcondition(16)

def spectrum_radius(erfa,beta,theta):
    (W,T) = prcondition(m)
    W1=theta*W+T

    T1=theta*T-W

    M11=np.hstack((erfa*W1,zeros((n,n))))
    M12=np.hstack((T1,beta*W1))
    M1=np.vstack((M11,M12))

    N11=np.hstack(((erfa-1)*W1,T1))
    N12=np.hstack((zeros((n,n)),(beta-1)*W1))
    N1=np.vstack((N11,N12))


    M21=np.hstack((erfa*W1,-T1))
    M22=np.hstack((zeros((n,n)),beta*W1))
    M2=np.vstack((M21,M22))

    N21=np.hstack(((erfa-1)*W1,zeros((n,n))))
    N22=np.hstack((-T1,(beta-1)*W1))
    N2=np.vstack((N21,N22))
    if (np.linalg.det(M1)==0)| (np.linalg.det(M2)==0)|(np.linalg.det(N1)==0)| (np.linalg.det(N2)==0):
        spectrum=100
    else:
        H=(mat(M2).I)*mat(N2)*(mat(M1).I)*mat(N1)
        eigvalue= np.linalg.eig(H)[0]
        eigvalues=[abs(i) for i in eigvalue]
        spectrum = max(eigvalues)
    #print (max(eigvalues))
    return spectrum

def prcondition(m):
    I=np.eye(m)

    Bm=(1.0/(h*h))*tridiag(-1,2,-1,m)
    K=np.kron(np.eye(m),Bm)+np.kron(Bm,np.eye(m))
    # b=zeros((2*n,1))

    # for i in range(n):
    #    b[i]=pow(h,2)*((1-1j)*i)/(t*pow(i+1,2))
    W=pow(h,2)*(K+((3-pow(3,1/2))/t)*np.eye(n))
    T=pow(h,2)*(K+((3+pow(3,1/2))/t)*np.eye(n))
    #   print (type(W))
    #  print (type(T))
    return (W,T)


def params_space():

    erfa = [float(i)/10 for i in range(1,10,1)]
    beta =  [float(i)/10 for i in range(1,10,1)]
    theta = [float(i)/10 for i in range(1,10,1)]
    params=list(itertools.product(erfa,beta,theta))

    sc = SparkContext()
    RDD = sc.parallelize(params)
    spectrum_RDD = RDD.map(lambda s : ((s[0],s[1],s[2]),spectrum_radius(s[0],s[1],s[2])))
#           .sortBy(lambda x: x[1]).collect()
    spectrum_RDD.saveAsTextFile("/user/bigdata_driver_ecosys_test/tangxu/text/")
#    print spectrum_RDD
   # RDD.saveAsTextFile("/user/bigdata_driver_ecosys_test/tangxu/text/")
 #   print spectrum_RDD.collect()
    sc.stop()
'''

    stringRDD = sc.parallelize(['Apple','Orange','Grape','Banana','Apple'])
           print (intRDD.collect())
           print (stringRDD.collect())
           print (intRDD.map(lambda x:x+1).collect())
'''
def sss(mmm):
    return mmm*mmm+1


def main():
    sc = SparkContext()
    spark = SparkSession.builder \
            .appName("Word Count") \
            .config("spark.some.config.option", "some-value") \
            .getOrCreate()
    df = sc.parallelize([ \
            Row(name='Alice', age=5, height=80), \
            Row(name='Alice', age=5, height=80), \
            Row(name='Alice', age=10, height=80)]).toDF()
    print (df.dropDuplicates().show())

    intRDD = sc.parallelize([3,1,2,5,5])

    stringRDD = sc.parallelize(['Apple','Orange','Grape','Banana','Apple'])
    print (intRDD.collect())
    print (stringRDD.collect())
    print (intRDD.map(lambda x: sss(x)).collect())
    sc.stop()
if __name__ =="__main__":
    params_space()
    #main()

