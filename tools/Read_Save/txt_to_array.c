
#include <malloc.h>  
#include<string.h>
#include<stdio.h>
#include <stdlib.h>
#define rows 4
#define cols 4  
//#define len 1024


float ** get_RGB_araay(int flag)
{
 
  int i,j;
  FILE *fp;
  switch (flag){
        case 1:fp = fopen("G:/工作资料/C语言/data/array1.txt","rb"); break; 
        case 2:fp = fopen("G:/工作资料/C语言/data/array2.txt","rb"); break;
        case 3:fp = fopen("G:/工作资料/C语言/data/array3.txt","rb"); break;
        default:printf("error\n");
    }
  //fp = fopen("G:/工作资料/C语言/data/array.txt","rb");  
  if (fp == NULL)
    {
        printf("can not open file!\n");
        exit(0);
    }


 //rewind(fp);/*指向文件开头*/
 
  float tmp;
  float **array_data =(float **)malloc(rows*sizeof(float *));//先申请M个指针型字节的空间
  for(i=0;i<rows;i++)
        {
	      array_data[i]=(float *)malloc(cols*sizeof(float));
		}
   for(i=0;i<rows;i++)
        {
                for(j=0;j<cols;j++)
                {
                        fscanf(fp,"%f",&tmp);     /*每次读取一个数，fscanf函数遇到空格或者换行结束*/

                        array_data[i][j]=tmp;
                       // *((float *)array_data+cols*i+j) = tmp[i][j];
                }
               // fscanf(fp,"\n");
        }
   

    fclose(fp);

 return array_data;

}

int main()
{
   int i,j;
   float **p;
   p = get_RGB_araay(1);
 printf("\n");
 
	 for(i=0;i<rows;i++)
        {
                for(j=0;j<cols;j++)
                {
                        printf("%f\t",p[i][j]);//输出
                }
                printf("\n");
        }

return 0;

}

