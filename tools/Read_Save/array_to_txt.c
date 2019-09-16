
#include<string.h>
#include<stdio.h>
#include <stdlib.h>
#define rows 2
#define cols 2  
//#define len 1024


void save_RGB_araay(float array_data[][cols] ,int flag)
{
 
  int i,j;
  FILE *fp;
  switch (flag){
        case 1:fp = fopen("G:/工作资料/C语言/data/array.txt","w"); break; 
        case 2:fp = fopen("G:/工作资料/C语言/data/array.txt","w"); break;
        case 3:fp = fopen("G:/工作资料/C语言/data/array.txt","w"); break;
        default:printf("error\n");
    }
  //fp = fopen("G:/工作资料/C语言/data/array.txt","rb");  
  if (fp == NULL)
    {
        printf("can not open file!\n");
        exit(0);
    }


 //rewind(fp);/*指向文件开头*/
 
   for(i=0;i<rows;i++)
        {
                for(j=0;j<cols;j++)
                {
                   fprintf(fp,"%f\t",array_data[j][i]);     /*每次读取一个数，fscanf函数遇到空格或者换行结束*/

                }
               fprintf(fp,"\n");
        }

    fclose(fp);


}

int main()
{
   float aa[2][2]={1,2,3,4};
   save_RGB_araay(aa ,1);

return 0;

}

