#include "MatrixLib.h"
#include <stdio.h>
#include <stdlib.h>

int main()
{

double a[9]={1,2,3,4,5,6,7,8,10};
int i,j,m;
for (i=0;i<3;i++)
	{
	 for (j=0;j<3;j++)
		{
		printf("%lf\t",a[i*3+j]);
		}
	 printf("\n");

}

//double b[9];

m = MatInv(a,3);

//判断矩阵是否可逆，如果可逆，则打印其逆矩阵，否则报错
if(m)
{
	//MatInv1(b,a,3);
	printf("\n");

	for (i=0;i<3;i++)
	{
	   for (j=0;j<3;j++)
		{
			printf("%lf\t",a[i*3+j]);
		}
	   printf("\n");
	}
}
else
{
 printf("matrix doesn't exist inverse!\n");

}

return 0;
}