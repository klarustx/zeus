// FFT.cpp : Defines the entry point for the console application.
#include <math.h>  
#include <malloc.h>  
#include<string.h>
#include<stdio.h>
#include <stdlib.h>
#include "Array_mutable.h"
#define pi (double) 3.14159265359  
/*复数的定义*/  
typedef struct  
{  
    double re;  
    double im;  
}COMPLEX;  



/*复数的加运算*/  
COMPLEX Add(COMPLEX c1, COMPLEX c2)  
{  
    COMPLEX c;  
    c.re = c1.re + c2.re;  
    c.im = c1.im + c2.im;  
    return c;  
}  
/*复数的减运算*/  
COMPLEX Sub(COMPLEX c1, COMPLEX c2)  
{  
    COMPLEX c;  
    c.re = c1.re - c2.re;  
    c.im = c1.im - c2.im;  
    return c;  
}  
/*复数的乘运算*/  
COMPLEX Mul(COMPLEX c1, COMPLEX c2)  
{  
    COMPLEX c;  
    c.re = c1.re*c2.re - c1.im*c2.im;  
    c.im = c1.re*c2.im + c1.im*c2.re;  
    return c;  
}  


/*快速傅立叶变换 
TD为时域值，FD为频域值，power为2的幂数*/  
void FFT(COMPLEX *TD, COMPLEX *FD, int power)  
{  
  
    int count;  
    int i,j,k,bfsize,p;  
    double angle;  
    COMPLEX *W,*X1,*X2,*X;  
    /*计算傅立叶变换点数*/  
    count=1<<power;  

    printf("count = %d\n",count);
    /*分配运算器所需存储器*/  
    W=(COMPLEX *)malloc(sizeof(COMPLEX)*count/2);  
    X1=(COMPLEX *)malloc(sizeof(COMPLEX)*count);  
    X2=(COMPLEX *)malloc(sizeof(COMPLEX)*count);  
    /*计算加权系数*/  
    for(i=0;i<count/2;i++)  
    {  
        angle=-i*pi*2/count;  
        W[i].re=cos(angle);  
        W[i].im=sin(angle);  
    }  
    /*将时域点写入存储器*/  
    memcpy(X1, TD, sizeof(COMPLEX)*count);  
    /*蝶形运算*/  
    for(k=0; k<power; k++)  
    {  
        for(j=0;j<1<<k;j++)  
        {  
            bfsize=1<<power-k;  
            for(i=0;i<bfsize/2;i++)  
            {  
                p=j*bfsize;  
                X2[i+p]=Add(X1[i+p], X1[i+p+bfsize/2]);  
                X2[i+p+bfsize/2]=Mul(Sub(X1[i+p], X1[i+p+bfsize/2]),W[i*(1<<k)]);  
            }  
        }  
        X=X1;  
        X1=X2;  
        X2=X;  
    }  
  

    /*重新排序*/  
    for(j=0;j<count;j++)  
    {  
    p=0;  
        for(i=0;i<power;i++)  
        {  
            if(j&(1<<i))  
               p+=1<<power-i-1;  
        }  
        FD[j]=X1[p];
    }  

    /*释放存储器*/  
    free(W);  
    free(X1);  
    free(X2);  

}  
/*快速傅立叶反变换，利用快速傅立叶变换 
FD为频域值，TD为时域值，power为2的幂数*/  
void IFFT(COMPLEX *FD, COMPLEX *TD, int power)  
{  
    int i,count;  
    COMPLEX *x;  
    /*计算傅立叶反变换点数*/  
    count=1<<power;
    /*分配运算所需存储器*/  
    x=(COMPLEX *)malloc(sizeof(COMPLEX)*count);  
    /*将频域点写入存储器*/  
    memcpy(x,FD,sizeof(COMPLEX)*count);  
    /*求频域点的共轭*/  
    for(i=0;i<count;i++)  
    {  
        x[i].im=-x[i].im;  
    }  
    /*调用快速傅立叶变换*/  
    FFT(x,TD,power);  
    /*求时域点的共轭*/  
    for(i=0;i<count;i++)  
    {  
        TD[i].re/=count;  
        TD[i].im=-TD[i].im/count;  
    }  
    /*释放存储器*/  
    free(x);  
}  

/*信号的傅里叶变换函数入口*/
double * fft(double original_signal[], int len )
{
  int i;
  Array Amplitude;
  Amplitude=array_creat(len);
  COMPLEX *signal  = (COMPLEX *) malloc(len * sizeof(COMPLEX));
  COMPLEX *FD_signal  = (COMPLEX *) malloc(len * sizeof(COMPLEX));
 

for(i=0; i<len; i++)
  {
    signal[i].re = double(original_signal[i]);
    signal[i].im = double(0);
  }
 //快速傅里叶变换 
int power = int(log(len+1)/log(2));
printf("power=%d\n",power);

FFT(signal, FD_signal, power);
double tmp;

/*
for(i=0;i<len;i=i+1)
{
	printf("%lf  %lf\n",FD_signal[i].re,FD_signal[i].im);
}
*/


for(i=0;i<len;i=i+1)
{
  
  tmp = sqrt(pow(FD_signal[i].re,2) + pow(FD_signal[i].im,2));
  array_set(&Amplitude, i, tmp);
}

return Amplitude.array;

}
