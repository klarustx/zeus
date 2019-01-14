import pandas as pd
import numpy as np
from numpy import *
import math
m=16
n=m*m
h=1.0/(m+1)
t=h

def tridiag(kk1,kk2,kk3,k):
    F=kk2*np.eye(k)
    print(type(F))
    FR=[1 for i in range(k-1)]
    Q1=kk1*np.diag(FR,1)
    Q2=kk3*np.diag(FR,-1)
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

    H=(mat(M2).I)*mat(N2)*(mat(M1).I)*mat(N1)

    eigvalue= np.linalg.eig(H)[0]
    eigvalues=[abs(i) for i in eigvalue]
    spectrum = max(eigvalues)
    #print (max(eigvalues))
    return spectrum


def prcondition(m):
    I=np.eye(m)

    Bm=(1.0/pow(h,2))*tridiag(-1,2,-1,m)
    K=np.kron(np.eye(m),Bm)+np.kron(Bm,np.eye(m))
   # b=zeros((2*n,1))

   # for i in range(n):
    #    b[i]=pow(h,2)*((1-1j)*i)/(t*pow(i+1,2))
    W=pow(h,2)*(K+((3-pow(3,1/2))/t)*np.eye(n))
    T=pow(h,2)*(K+((3+pow(3,1/2))/t)*np.eye(n))
 #   print (type(W))
  #  print (type(T))
    return (W,T)

if __name__ == '__main__':
  print "0.74,0.65,0.6",spectrum_radius(0.88,0.91,0.9)


def sss(mmm):
    return mmm*mmm
