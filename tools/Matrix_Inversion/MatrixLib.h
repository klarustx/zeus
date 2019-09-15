//////////////////文件名： MatrixLib.h ////////////////////////////////////////
////  矩阵运算模块的库函数头文件
/* 主要功能： 用于生成库函数
*/
/***********************************************************/

#ifndef _Matrix_Lib_
#define _Matrix_Lib_


#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>


void	 MatMult(double a[],double b[],int m1,int n1,int k,double c[]);	    //矩阵相乘
void	 MatkMult(double out_m[], double in_m[],double k,int rows,int cols);///矩阵乘以常数 k
void     MatkMultf(float out_m[], float in_m[],float k,int rows,int cols); ///矩阵乘以常数 k 单精度浮点
void     MatSub(double a[],double b[],int m1,int n1,double c[]);		   //矩阵相减
void	 MatSubf(float a[],float b[],int m1,int n1,float c[]);	    //矩阵相减单浮点
void	 get_m_Start(double ans[],double m[],int n);				//计算每一行每一列的每个元素所对应的余子式，组成A*  
void	 MatT(double a[],int m1,int n1,double at[]);				//矩阵转置
void	 MatDiv(double a[],float t,int m1,int n1,double at[]);	//矩阵除以常数 t

int	MatVD(double a[],int n,double v[],double eps,int jt);	// VD分解函数
int	MatInv(double a[],int n);							    // 矩阵求逆
int	MatInv1(double  out_m[], double  in_m[],int n);			// 矩阵求逆，输入输出，采用余子式方法
void	MatPlus(double a[],double b[],int m1,int n1,double c[]);// 矩阵相加
void    MatPlusf(float a[],float b[],int m1,int n1,float c[]);   // 矩阵相加 单浮点
void    Mat_Multf(float *p1,float *p2,int m,int k,int n,float *p3);//矩阵相乘 单精度浮点
void    MatMultf(float a[],float b[],int m1,int n1,int k,float c[]);	//矩阵相乘
double	get_fabs_m(double  m[],int n);	//按第一行展开计算|Mag_A|
void    Across_Multply(double a[3],double b[3],double c[3]);		//向量叉乘


float  DelWildGyroPoint(float *fData,int nNum);		 // 去除野点

#endif
