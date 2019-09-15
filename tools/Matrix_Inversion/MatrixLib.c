/************************************************************/
//////////////////文件名： MatrixLib.c ////////////////////////////////////////
//主要功能： 用于生成库函数
//1.矩阵运算库函数，包含所有的矩阵运算函数
//
/***********************************************************/

#include	"MatrixLib.h"
#include <stdio.h>
#include <malloc.h>  
#include<string.h>
#include <stdlib.h>
////////////////////////////////////////////////////////////////////////////
//////////////////********矩阵运算****************//////////////////////
////////////////////////////////////////////////////////////////////////////
void Mat_Multf(float *p1,float *p2,int m,int k,int n,float *p3)//矩阵相乘 单精度浮点
{
	int i,j,l;
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{	
			*(p3+i*n+j)=0.0;		
			for(l=0;l<k;l++)
			    *(p3+i*n+j)=*(p3+i*n+j)+(*(p1+i*k+l))*(*(p2+l*n+j));
		}
	}
}

void MatMult(double a[],double b[],int m1,int n1,int k,double c[])	//矩阵相乘
{
	 int i,j,l,u;
	 for(i=0;i<=m1-1;i++)
	 {
	  for(j=0;j<=k-1;j++)
	  {
	   u=i*k+j; c[u]=0.0;
	   for(l=0;l<=n1-1;l++)
	    c[u]=c[u]+a[i*n1+l]*b[l*k+j];
	   }
	  }
	  return;
 }

void MatMultf(float a[],float b[],int m1,int n1,int k,float c[])	//矩阵相乘
{
	 int i,j,l,u;
	 for(i=0;i<=m1-1;i++)
	 {
	  for(j=0;j<=k-1;j++)
	  {
	   u=i*k+j; c[u]=0.0;
	   for(l=0;l<=n1-1;l++)
	    c[u]=c[u]+a[i*n1+l]*b[l*k+j];
	   }
	  }
	  return;
 
}
  
void MatSub(double a[],double b[],int m1,int n1,double c[])	//矩阵相减
{
	 int i,j,u;
	 for(i=0;i<=m1-1;i++)
	 {
	  for(j=0;j<=n1-1;j++)
	  {
	   u=i*n1+j;
	   c[u]=a[u]-b[u];
	   }
	  }
	  return;
}

void MatSubf(float a[],float b[],int m1,int n1,float c[])	//矩阵相减单浮点
{
	 int i,j,u;
	 for(i=0;i<=m1-1;i++)
	 {
	  for(j=0;j<=n1-1;j++)
	  {
	   u=i*n1+j;
	   c[u]=a[u]-b[u];
	   }
	  }
	  return;
}

///矩阵求逆，求成功返回1，否则返回0
int MatInv(double a[],int n)
{
	 int *is,*js,i,j,k,l,v,u;
	 double d,p;
	 is=(int *)malloc(n*sizeof(int));
	 js=(int *)malloc(n*sizeof(int));
	 for(k=0;k<=n-1;k++)
	 {
	  d=0.0;
	  for(i=k;i<=n-1;i++)
	   for(j=k;j<=n-1;j++)
	   {
	    l=i*n+j; p=fabs(a[l]);
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
//	    printf("\n error**not inv\n\n error**not inv\n");
	    return(0);
	   }
	   if(is[k]!=k)
	    for(j=0;j<=n-1;j++)
	    {
	     u=k*n+j;
	     v=is[k]*n+j;
	     p=a[u];
	     a[u]=a[v];
	     a[v]=p;
	    }
	   if(js[k]!=k)
	    for(i=0;i<=n-1;i++)
	    {
	     u=i*n+k;
	     v=i*n+js[k];
	     p=a[u];
	     a[u]=a[v];
	     a[v]=p;
	    }
	    l=k*n+k;
	    a[l]=1.0/a[l];
	    for(j=0;j<=n-1;j++)
	     if(j!=k)
	     {
	      u=k*n+j;
	      a[u]=a[u]*a[l];
	     }
	     for(i=0;i<=n-1;i++)
	      if(i!=k)
	       for(j=0;j<=n-1;j++)
		if(j!=k)
		{
		 u=i*n+j;
		 a[u]=a[u]-a[i*n+k]*a[k*n+j];
		}
		for(i=0;i<=n-1;i++)
		 if(i!=k)
		 {
		  u=i*n+k;
		  a[u]=-a[u]*a[l];
		 }
	   }
	   for(k=n-1;k>=0;k--)
	   {
	    if(js[k]!=k)
	     for(j=0;j<=n-1;j++)
	     {
	      u=k*n+j;
	      v=js[k]*n+j;
	      p=a[u];
	      a[u]=a[v];
	      a[v]=p;
	     }
	     if(is[k]!=k)
	      for(i=0;i<=n-1;i++)
	      {
	       u=i*n+k;
	       v=i*n+is[k];
	       p=a[u];
	       a[u]=a[v];
	       a[v]=p;
	      }
	  }
	  free(is);
	  free(js);
	  return(1);
}

int MatInv1(double  out_m[], double  in_m[],int n)	//矩阵求逆，输入输出
{
	int i,j;
	double fabs_m;

	fabs_m=get_fabs_m(&in_m[0],n);
	if(fabs_m>-0.00001&&fabs_m<=0)
		fabs_m=-0.00001;
	if(fabs_m<0.00001&&fabs_m>0)
		fabs_m=0.00001;
	get_m_Start(&out_m[0], &in_m[0],  n);
	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
		{
			out_m[i*n+j]=out_m[i*n+j]/fabs_m;
		}
	return 1;
}


//计算每一行每一列的每个元素所对应的余子式，组成A*  
void get_m_Start(double ans[],double m[],int n)
{  
	int i,j,k,t,isk,ist;  
	double  temp[100]; 
	if(n==1)  
	{  
		ans[0] = 1;  
		return ;  
	} 
	for(i=0;i<n;i++)  
	{  
		for(j=0;j<n;j++)  
		{  
			for(k=0;k<n-1;k++)  
			{  
			        for(t=0;t<n-1;t++)  
			        {  
					if(k>=i)
					{
						isk=k+1;
					}
					else
					{
						isk=k;
					}
					if(t>=j)
					{
						ist=t+1;
					}
					else
					{
						ist=t;
					}
					temp[k*(n-1)+t] = m[isk*n+ist];  
			        }  
			}  
			ans[j*n+i]  = get_fabs_m(&temp[0],n-1);  
			if((i+j)%2 == 1)  
			{  
				ans[j*n+i] = - ans[j*n+i];  
			}  
		}  
	}  
}

void MatT(float a[],int m1,int n1,float at[])
{
	 int i,j;
	 for(i=0;i<m1;i++)
	  for(j=0;j<n1;j++)
	  {
	   at[j*m1+i]=a[i*n1+j];
	   }
	   return;
 }

void MatDiv(float a[],float t,int m1,int n1,float at[])
{
	 int i,j,u;
	 for(i=0;i<m1;i++)
	  for(j=0;j<n1;j++)
	  {
	   u=i*n1+j;
	   at[u]=a[u]/t;
	   }
	   return;
}

void MatPlus(double a[],double b[],int m1,int n1,double c[])
{
	 int i,j,u;
	 for(i=0;i<=m1-1;i++)
	 {
	  for(j=0;j<=n1-1;j++)
	  {
	   u=i*n1+j;
	   c[u]=a[u]+b[u];
	   }
	  }
	  return;
 }

 void MatPlusf(float a[],float b[],int m1,int n1,float c[]) //// 矩阵相加 单浮点
{
	 int i,j,u;
	 for(i=0;i<=m1-1;i++)
	 {
	  for(j=0;j<=n1-1;j++)
	  {
	   u=i*n1+j;
	   c[u]=a[u]+b[u];
	   }
	  }
	  return;
 }
///矩阵乘以 常数
 void MatkMult(double out_m[], double in_m[],double k,int rows,int cols)
{
	 int i,j;
	for(i=0;i<cols;i++)
		for(j=0;j<rows;j++)
			out_m[i*cols+j] = k*in_m[i*cols+j];
}

 void MatkMultf(float out_m[], float in_m[],float k,int rows,int cols)
{
	 int i,j;
	for(i=0;i<cols;i++)
		for(j=0;j<rows;j++)
			out_m[i*cols+j] = k*in_m[i*cols+j];
}

// VD分解函数 分解成功返回1，否则返回0
int MatVD(double a[],int n,double v[],double eps,int jt)		
{
	int i,j,p,q,u,w,t,s,l;
	double fm,cn,sn,omega,x,y,d;
	l=1;
	for (i=0; i<=n-1; i++)
	{
		v[i*n+i]=1.0;
		for (j=0; j<=n-1; j++)
		if (i!=j) 
			v[i*n+j]=0.0;
	}
	while (1==1)
	{
		fm=0.0;
		for (i=1; i<=n-1; i++)
		for (j=0; j<=i-1; j++)
		{ 
			d=fabs(a[i*n+j]);
			if ((i!=j)&&(d>fm))
		  	{ 
		  		fm=d; 
		  		p=i; 
		  		q=j;
		  	}
		}
	        if (fm<eps)  
	        {
	        		return(1);
	        	}
	        if (l>jt)
		{
			return(-1);
		}
		l=l+1;
		u=p*n+q; w=p*n+p; t=q*n+p; s=q*n+q;
		x=-a[u]; y=(a[s]-a[w])/2.0;
		omega=x/sqrt(x*x+y*y);
		if (y<0.0)
		{
			omega=-omega;
		}
		sn=1.0+sqrt(1.0-omega*omega);
		sn=omega/sqrt(2.0*sn);
		cn=sqrt(1.0-sn*sn);
		fm=a[w];
	        a[w]=fm*cn*cn+a[s]*sn*sn+a[u]*omega;
	        a[s]=fm*sn*sn+a[s]*cn*cn-a[u]*omega;
	        a[u]=0.0; a[t]=0.0;
		for (j=0; j<=n-1; j++)
		if ((j!=p)&&(j!=q))
		{ 
			u=p*n+j; w=q*n+j;
			fm=a[u];
			a[u]=fm*cn+a[w]*sn;
			a[w]=-fm*sn+a[w]*cn;
		}
		for (i=0; i<=n-1; i++)
		if ((i!=p)&&(i!=q))
		{
			 u=i*n+p; w=i*n+q;
			fm=a[u];
			a[u]=fm*cn+a[w]*sn;
			a[w]=-fm*sn+a[w]*cn;
		}
		for (i=0; i<=n-1; i++)
		{ 
			u=i*n+p; w=i*n+q;
			fm=v[u];
			v[u]=fm*cn+v[w]*sn;
			v[w]=-fm*sn+v[w]*cn;
		}
	}
//	return(1);
}  

double get_fabs_m(double  m[],int n)//按第一行展开计算|Mag_A|  
{     
	double  ans = 0;  
	double temp[100];  
	int i,j,k,isk; 
	double  t;
	
	if(n==1)  
	{  
		return m[0];  
	}
	for(i=0;i<n;i++)  
	{  
		for(j=0;j<n-1;j++)  
		{  
		    for(k=0;k<n-1;k++)  
		    {  
			if(k>=i)
			{
				isk=k+1;
			}
			else
			{	
				isk=k;
			}
			temp[j*(n-1)+k] = m[(j+1)*n+isk];  
		    }  
		}  
		t = get_fabs_m(&temp[0],n-1);  
		if(i%2==0)  
		{  
			ans += m[i]*t;  
		}  
		else  
		{  
			ans -=  m[i]*t;  
		}  
	}  
	return ans;  
}  


 void Across_Multply(double a[3],double b[3],double c[3])	// 向量叉乘
{
	c[0]=-a[2]*b[1]+a[1]*b[2];
	c[1]=a[2]*b[0]-a[0]*b[2];
	c[2]=-a[1]*b[0]+a[0]*b[1];	
}


/*去除野点，fData  为采集的数据，nNum为数据的个数，返回去掉畲笞钚≈岛蟮钠骄**/
double DelWildGyroPoint(double *fData,int nNum)
{
	char j;
	double fAve;
	fAve = 0 ;
	for(j=0;j<nNum;j++)
	{
	    fAve += fData[j];
	}
//	fAve = (fAve - fMax - fMin) /(nNum-2);
	fAve = fAve /nNum;
	return fAve;
}



