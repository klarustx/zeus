/*计算一个信号快速傅里叶变换后的幅度*/
#include<string.h>
#include<stdio.h>
#include "fft.h"
int main()
{
	double ss[8]= {1,7,3,4,5,7,8,9};
	double *yy;
	yy=fft(ss,8);
	int i;
	for (i=0;i<8;i++)
	{
		printf("%lf\n",yy[i]);
	}
    return 0;
}

