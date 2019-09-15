//////////////////文件名： MatrixLib.h ////////////////////////////////////////
////  矩阵运算模块的库函数头文件
/* 主要功能： 用于生成库函数
*/
/***********************************************************/
#ifndef     _TEST_H_
#define    _TEST_H_

#include <math.h>  
#include <malloc.h>  
#include<string.h>
#include<stdio.h>
#include <stdlib.h>
  
typedef struct  
{  
    double re;  
    double im;  
}COMPLEX;  


/*复数初始化*/  
COMPLEX first_set_value(double c1, double c2)  
{  
    COMPLEX c;  
    c.re =c1;  
    c.im = c2;  
    return c;  
}  

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


/*复数的相反数*/  
COMPLEX Oppsite(COMPLEX c1)  
{  
    COMPLEX c;  
    c.re = -c1.re;  
    c.im = -c1.im;  
    return c;  
}  

/*复数的模*/
double Module(COMPLEX c1)
{
	double c;
	c =  pow(c1.re*c1.re + c1.im*c1.im,2);
    return c; 
}
/*复数的赋值*/ 
COMPLEX Set_value(COMPLEX c1)  
{  
    COMPLEX c;  
    c.re = c1.re;  
    c.im = c1.im;  
    return c;  
}  


/*复数的逆*/ 
COMPLEX Get_inverse(COMPLEX c1)  
{  
    COMPLEX c; 
	double p = c1.re*c1.re + c1.im*c1.im;
    c.re = c1.re/p;  
    c.im = -c1.im/p;  
    return c;  
}  


#endif