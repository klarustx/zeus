// hilbert_transform.cpp : Defines the entry point for the console application.
#include <math.h>  
#include <malloc.h>  
#include<string.h>
#include<stdio.h>
#define pi (double) 3.14159265359  
#define len 8
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
/*负数的减运算*/  
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
    //printf("count = %d\n",count);
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

int main()
{
 // int len=8;
  COMPLEX signal[len];
  COMPLEX FD_signal[len];
  COMPLEX expand_signal[len];
  COMPLEX recover_signal[len];
  COMPLEX hil_signal[len];
  int original_signal[8] = {1, 5, 7, 8, 11, 8, 4, 1}; 

  int power = int(log(len+1)/log(2));
  printf("power = %d\n",power);
  int i;
  for(i=0; i<len; i++)
  {
    signal[i].re = double(original_signal[i]);
    signal[i].im = double(0);
  }
 /*快速傅里叶变换*/  
  FFT(signal, FD_signal, power);
 for(i=0; i<len; i++)
  {
    if(i==0)
	{
	expand_signal[i].re = FD_signal[i].re;
        expand_signal[i].im = FD_signal[i].im;
	}
	else if(0<i&&i<len/2)
	{
	expand_signal[i].re =2* FD_signal[i].re;
        expand_signal[i].im =2* FD_signal[i].im;
	}
	else
	{
	expand_signal[i].re = 0;
        expand_signal[i].im = 0;
	}

  }
 
 /*快速傅里叶逆变换*/  
 IFFT(expand_signal, recover_signal, power);
	
  for( i=0; i<len; i++)
{
  hil_signal[i].im = recover_signal[i].im;
  hil_signal[i].re = original_signal[i];
}
  for( i=0; i<len; i++)
{
  printf("%.4f",hil_signal[i].re );
  printf("+" );
  printf("i*%.4f\n",hil_signal[i].im );
}
return 0;
}
