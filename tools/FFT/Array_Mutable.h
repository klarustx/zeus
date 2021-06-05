//定义变长数组

typedef struct
{
	double*array;
	int size;
}Array;

Array array_creat(int init_size)
{
	Array a;
	a.array = (double*)malloc(sizeof(double)*init_size);
	a.size = init_size;
	return a;
}
 
//回收空间
void array_free(Array *a)
{
	free(a->array);
	a->array = NULL;
	a->size = 0;
}
 
//目前有多少个空间可以用
int  array_size(Array *a)
{
	return a->size;
}
 
void array_set(Array*a, int index, double value)
{
	a->array[index] = value;
}
