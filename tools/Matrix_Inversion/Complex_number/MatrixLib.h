//////////////////文件名： MatrixLib.h ////////////////////////////////////////
////  矩阵运算模块的库函数头文件
/* 主要功能： 用于生成库函数
*/
/***********************************************************/

/************************************************************/
//////////////////文件名： MatrixLib.c ////////////////////////////////////////
//主要功能： 用于生成库函数
//1.矩阵运算库函数，包含所有的矩阵运算函数


#ifndef _Matrix_Lib_
#define _Matrix_Lib_

/***********************************************************/
#include	"ComplexLib.h"
#include <stdio.h>
#include <malloc.h>  
#include<string.h>
#include <stdlib.h>
////////////////////////////////////////////////////////////////////////////
//////////////////********矩阵运算****************//////////////////////
////////////////////////////////////////////////////////////////////////////


///矩阵求逆，求成功返回1，否则返回0
int MatInv(COMPLEX a[],int n)
{
   int i,j,k,l,v,u;
   int *is,*js;
   double d,p;
   is=(int *)malloc(n*sizeof(int));
   js=(int *)malloc(n*sizeof(int));
   COMPLEX tmp;
   for(k=0;k<=n-1;k++)
   {
    d=0.0;
    for(i=k;i<=n-1;i++)
     for(j=k;j<=n-1;j++)
     {
      l=i*n+j; 
      p=Module(a[l]);
      if(p>d)
      {
       d=p;
       is[k]=i;
       js[k]=j;
      }
     }
     if(d+1.0==1.0)
     {
      free(is);
      free(js);
//      printf("\n error**not inv\n\n error**not inv\n");
      return(0);
     }
     if(is[k]!=k)
      for(j=0;j<=n-1;j++)
      {
       u=k*n+j;
       v=is[k]*n+j;
       tmp=Set_value(a[u]);
       a[u]=Set_value(a[v]);
       a[v]=Set_value(tmp);
      }
     if(js[k]!=k)
      for(i=0;i<=n-1;i++)
      {
       u=i*n+k;
       v=i*n+js[k];
       tmp=Set_value(a[u]);
       a[u]=Set_value(a[v]);
       a[v]=Set_value(tmp);
      }
      l=k*n+k;
      a[l]=Get_inverse(a[l]);
      for(j=0;j<=n-1;j++)
       if(j!=k)
       {
        u=k*n+j;
        a[u]=Mul(a[u],a[l]);
       }
       for(i=0;i<=n-1;i++)
        if(i!=k)
         for(j=0;j<=n-1;j++)
    if(j!=k)
    {
     u=i*n+j;
     a[u]=Sub(a[u],Mul(a[i*n+k],a[k*n+j]));
    }
    for(i=0;i<=n-1;i++)
     if(i!=k)
     {
      u=i*n+k;
      a[u]=Oppsite(Mul(a[u],a[l]));
      
     }
     }
     for(k=n-1;k>=0;k--)
     {
      if(js[k]!=k)
       for(j=0;j<=n-1;j++)
       {
        u=k*n+j;
        v=js[k]*n+j;
        tmp=Set_value(a[u]);
        a[u]=Set_value(a[v]);
        a[v]=Set_value(tmp);
       }
       if(is[k]!=k)
        for(i=0;i<=n-1;i++)
        {
         u=i*n+k;
         v=i*n+is[k];
         tmp=Set_value(a[u]);
         a[u]=Set_value(a[v]);
         a[v]=Set_value(tmp);
        }
    }
    free(is);
    free(js);
    return(1);
}



#endif
