#define _CRT_SECURE_NO_WARNINGS  //预定义,因为scanf不安全
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>

/*
	指针: 就是地址
	&变量名: 获取该变量的地址(指针)
	指针变量: 保存指针(地址)的变量
	类型  *  变量名; 定义一个类型的指针变量

	在指针变量定义时出现的*用来说明该变量是一个指针变量

	如何使用指针变量?  *p含义访问p所指向的变量
		*p: 解引用,间接访问符
*/

//int main()
//{
//	int a = 10;
//	a = 20;
//	int b = 20;
//	b = a;
//	&a;
//	&b;
//
//	printf("a的地址=%p,b的地址=%p\n", &a, &b); // %p输出地址(指针),以十六进制输出
//
//	return 0;
//}

//int main()
//{
//	int a = 10;
//	int b = 20;
//	int *p = &a; // 一个int地址赋值给一个int指针变量
//			// 获取a的地址
//	p = &b; // 把b的地址赋值给p
//	char c;
//	double d;
//	char* p1 = &c;
//	double* p2 = &d;
//
//	return 0;
//}


//int main()
//{
//	int a = 10;
//	int b = 20;
//	int* p = &a;
//	*p = 100; // a = 100
//	p = &b; // p保存的是b的地址
//	*p = 200;
//	printf("%p,%p\n",&b,p);
//
//	return 0;
//}


//int main()
//{
//	int a = 10;
//	printf("%d,%d\n", a, &a); // a的值, a的地址
//	int* p = &a;
//	printf("%d,%d,%d\n", *p, p, &p); // p指向的变量a的值,a的地址,p的地址
//
//	return 0;
//}


/*
	&的作用:  
			1. 按位与.
			2. 取地址

*/

//int main()
//{
//	int a = 10;
//	int b = 20;
//	int c = 4 & 3; // 按位与   100&011  相同的位都为1才为1
//	printf("%d\n", c);
//	printf("%p,%p,%p\n", &a, &b, &c);
//	printf("%d\n", a & b);
//
//	return 0;
//}

/*
	指针的应用

	局部变量: 定义在函数内部的变量包括形参,作用域在函数体内部
*/

// 交换两个变量的值(写成函数)
// 总结: 一个函数A通过调用函数B,来达到修改A中变量的值
//		1.必须传指针
//		2.在B中必须解应用 
//      

//void Swap(int a, int b)  // 没有交换成功,错误   没传指针
//{
//	int tmp = a;
//	a = b;
//	b = tmp;
//}
//
//int main()
//{
//	int a, b;
//	scanf("%d%d", &a, &b);
//	//int tmp = a;
//	//a = b;
//	//b = tmp;
//	printf("交换前=%d,%d", a, b);
//	Swap(a, b);
//	printf("交换后=%d,%d", a, b);
//
//	return 0;
//}


//void Swap(int* p1, int* p2)  // 没有解应用,交换失败
//{
//	int* tmp;
//	tmp = p1;
//	p1 = p2;
//	p2 = tmp;
//}


//void Swap(int* p1, int* p2)
//{
//	int tmp;
//	tmp = *p1;
//	*p1 = *p2;
//	*p2 = tmp;
//
//}
//int main()
//{
//	int a, b;
//	scanf("%d%d", &a, &b);
//	
//	printf("交换前=%d,%d\n", a, b);
//	Swap(&a, &b);
//	printf("交换后=%d,%d\n", a, b);
//
//	return 0;
//}


// 解一元二次方程
// 提前假定d=b^2-4ac>0
// 如何返回两个值
// C语言只能返回0个或者1个返回值
// 返回根的数量

//double Fun(int a, int b, int c)
//{
//	double x1, x2;
//	int d = b * b - 4 * a * c;
//
//	x1 = (-b + sqrt(d)) / (2 * a);
//	x2 = (-b - sqrt(d)) / (2 * a);
//
//	return x1;
//}


// x1,x2 称为输出参数(传指针,内部解引用)
// 究极常用, 力扣刷题常见

//int Fun(int a, int b, int c,double* x1,double* x2)
//{
//	int d = b * b - 4 * a * c;
//	*x1 = (-b + sqrt(d)) / (2 * a);
//	*x2 = (-b - sqrt(d)) / (2 * a);
//
//	return 2; // 返回两个根
//}
//
//
//int main()
//{
//	double x1;
//	double x2;
//	Fun(3, 5, 1, &x1, &x2);
//	printf("%lf,%lf\n", x1, x2);
//
//	return 0;
//}

// 课本不合适案例  

//int main()
//{
//	int* p; // 错误, 悬空指针, 野指针
//	*p = 10;
//
//	return 0;
//}


// 通过指针引用数组

/*
	一维数组arr的名字arr表示整个数组只在如下情况
		1.在定义数组的同一个函数中求sizeof.   例如:  int arr[10];  sizeof(arr) -> 40
		2.在定义数组的同一个函数中,&arr+1表示加整个数组的大小   例如:  int arr[10],&arr,&arr+1
		其他情况  arr都表示数组的起始地址(数组首元素地址)
*/

//int main()
//{
//	int arr[10] = { 1,3,5,7,9,11,13,15,17,19 };
//	//int* p = &arr[0];  // 第一个元素int的地址
//	int* p = arr; // 和上一行等价
//	printf("%d,%d\n", arr[0], *p);
//
//	printf("%d\n", sizeof(arr)); // 表示整个数组的大小(字节数)
//	printf("%d,%d\n", &arr, &arr + 1); // &arr+1表示加整个数组的大小(字节数)
//
//	return 0;
//}


// 指针的加法操作(运算)  
// 前提这个指针指向一个数组,同时程序应该保存不越界
/*
	p+整数,p++,++p合法
	p-整数,p--,--p合法
*/

//int main()
//{
//	int arr[10] = { 1,3,5,7,9,11,13,15,17,19 };
//	int* p = arr;
//	//for (int i = 0; i < 10; i++, p++) // 把指针往后调
//	//{
//	//	printf("%d ", *p); // 指针输出(访问)数组所有元素
//	//	// p++
//	//}
//
//	//for (int i = 0; i < 10; i++)
//	//{
//	//	printf("%d ", *p++);
//	//}
//
//	for (int i = 0; i < 10; i++)
//	{
//		printf("%d ", *(p + i));
//	}
//
//
//	return 0;
//}


// 指针的减法运算

//int main()
//{
//	int arr[10] = { 1,3,5,7,9,11,13,15,17,19 };
//	int* p = &arr[9];
//	// 从未到头输出数组的元素
//	//for (int i = 0; i < 10; i++)   // 把指针往前移动
//	//{
//	//	printf("%d ", *p);
//	//	--p;
//	//}
//
//	//for (int i = 0; i < 10; i++)   // 把指针往前移动
//	//{
//	//	printf("%d ", *p--);
//	//}
//
//	for (int i = 0; i < 10; i++)   // 把指针往前移动
//	{
//		printf("%d ", *(p-i));
//	}
//
//	return 0;
//}


// 输出数组元素的多种方法

// 有一个整形数组a, 有十个元素, 要求输出数组中的全部元素

//int main()
//{
//	int arr[10];
//	int i;
//	printf("请输入十个整形数字:");
//	for (i = 0; i < 10; ++i)
//	{
//		scanf("%d", &arr[i]);
//	}
//	for (i = 0; i < 10; ++i)
//	{
//		printf("%d ", arr[i]);
//	}
//	// 数组元素用数组名和下标表示
//	printf("\n");
//
//	return 0;
//}

//int main()
//{
//	int arr[10];
//	int i;
//	int* p = arr;
//	printf("请输入十个整形数字:");
//	for (i = 0; i < 10; ++i)
//	{
//		scanf("%d", &arr[i]);
//	}
//	for (i = 0; i < 10; ++i)
//	{
//		printf("%d ", *(arr + i)); // printf("%d ",*(p + i));
//	}
//	// 通过数组名和元素序号计算元素地址找到该元素
//	printf("\n");
//
//	return 0;
//
//}

/*
	指针的关系运算  >,<,>=,<=,==,!=
	前提: 必须在同一个数组
*/

//int main()
//{
//	int arr[10] = { 1,2,3,4,5,6,7,8,9,10 };
//	// 从头到尾输出数组元素
//	for (int* p = arr; p != &arr[10]; ++p) // p不等于第十一个元素的地址    标准规定可以使用尾后地址(指针)
//	{
//		printf("%d ", *p);
//	}
//	//for (int* p = arr; p <= &arr[9]; ++p)
//	//for (int* p = arr; p < &arr[10]; p++)
//
//	return 0;
//}


// 一个错误,第一次循环已到数组尾后元素  越界

//int main()
//{
//	int* p, i, arr[10];
//	p = arr; // p指向arr[0]
//	printf("请输入十个整型数字:");
//	for (i = 0; i < 10; ++i)
//	{
//		scanf("%d", p++);
//	}
//	// p已经到达a的尾后指针
//	p = arr;
//	for (i = 0; i < 10; ++i, ++p)
//	{
//		printf("%d ", *p);
//	}
//	printf("\n");
//
//	return 0;
//}

/*
	数组作为参数传递: 数组名仅仅表示数组首元素的地址
		传数组名 + 数组长度
*/

// 输出数组的所有元素
// p: 数组的起始地址
// n: 数组长度

//void Show(int *p, int n)
//{
//	for (int i = 0; i < n; i++)
//	{
//		printf("%d ", p[i]);
//	}
//	printf("\n");
//}
//
//int main()
//{
//	int arr[] = { 1,2,3,4,5,6,7,8,9,10 };
//	Show(arr,sizeof(arr)/sizeof(arr[0]));
//
//	return 0;
//}

// 将数组arr中n个整数按相反顺序存放
// x: 数组的起始地址, n: 元素个数

//void inv(int* x, int n)
//{
//	int tmp;
//	//for (int i = 0, j = n - 1; i < j; j--, i++) // 把x当作数组名操作,没有问题
//	//{
//	//	tmp = x[i];
//	//	x[i] = x[j];
//	//	x[j] = tmp;
//	//}
//
//	for (int i = 0, j = n - 1; i < j; j--, i++) // 把x当作指针操作
//	{
//		tmp = *(x + i);
//		*(x + i) = *(x + j);
//		*(x + j) = tmp;
//	}
//}
//
//void Show(int *p, int n)
//{	
//	for (int i = 0; i < n; i++)
//	{
//		printf("%d ", p[i]);
//	}
//	printf("\n");
//}
//
//int main()
//{
//	int arr[] = { 1,3,5,7,9,11,13,15,17,19 };
//	inv(arr, sizeof(arr) / sizeof(arr[0]));
//	Show(arr, sizeof(arr) / sizeof(arr[0]));
//	
//
//	return 0;
//}


// 用指针方法对10个整数按由大到小顺序排序   (选择排序法)
// 选择排序:  每次从待排序中找最小值和待排序的第一个值交换,直到结束
// arr: 数组起始地址 n; 元素个数(元素的长度)

//void SelectSort1(int* arr, int n)
//{
//	int k; // 最小值的下标
//	int tmp;
//	for (int i = 0; i < n - 1; ++i)  // 循环的趟数
//	{
//		k = i;
//		for (int j = i + 1; j < n; ++j)
//		{
//			if (arr[j] < arr[k]) // 找到最小值,更新下标
//			{
//				k = j;
//			}
//		}
//		if (k != i) // 把第一个值和最小值交换
//		{
//			// 把最小的放在最前面
//			tmp = arr[i];
//			arr[i] = arr[k];
//			arr[k] = tmp;
//		}
//	}
//}
//
//void SelectSort2(int* arr, int n)
//{
//	int k; // 最小值的下标
//	int tmp; // 临时变量
//	for (int i = 0; i < n - 1; ++i)  // 循环的趟数
//	{
//		k = i;
//		for (int j = i + 1; j < n; ++j)
//		{
//			if (*(arr+j) < *(arr+k)) // 找到最小值,更新下标
//			{
//				k = j;
//			}
//		}
//		if (k != i) // 把第一个值和最小值交换
//		{
//			// 把最小的放在最前面
//			tmp = *(arr+i);
//			*(arr + i) = *(arr + k);
//			*(arr + k) = tmp;
//		}
//	}
//}
//
//void Show(int *p, int n)
//{	
//	for (int i = 0; i < n; i++)
//	{
//		printf("%d ", p[i]);
//	}
//	printf("\n");
//}
//
//int main()
//{
//	int arr[] = { 1,15,9748,156,153,6,123,321,48,9 };
//	SelectSort2(arr, sizeof(arr) / sizeof(arr[0]));
//	Show(arr, sizeof(arr) / sizeof(arr[0]));
//
//	return 0;
//}


/*
	一维数组以及二维数组指针含义
*/

//int main()
//{
//	int arr[4];
//	int brr[3][4] = { {1,2,3,4},{5,6,7,8},{9,10,11,12} }; // 行优先
//	int* p = arr; // arr的类型就是int*
//	p = arr + 1; // arr + 1的类型还是int*
//	int a = arr[0]; // arr[0]的类型是int
//
//	// int** p2 = brr; // 错误的,说明brr的类型不是int **
//	// 必须把brr想象为一维数组   把每行视为一个元素
//	int(*p2)[4] = brr; // brr的类型为int(*)[4]
//	int* p3 = brr[0]; // brr[0]的类型为int *
//	// brr[0] 就是一维数组   arr也是一维数组  所以,brr[0]和arr含义相同
//	p2 = brr + 1; // brr + 1的类型为int(*)[4]  相当于第二行
//	p3 = brr[0] + 1; // brr[0] + 1的类型为int *
//	int b = brr[0][0]; // brr[0][0]的类型是int
//	b = brr[0][0] + 1; // brr[0][0] + 1的类型是int
//
//	return 0;
//}


/*
	通过指针引用多维数组     重要: 笔试 面试
*/

// 输出二维数组,所有元素的值
// void Show(int brr[3][4]) // 不太对, 3是个无效值,等同下一行
// void Show(int brr[][4]) // 等同下一行
void Show(int (*brr)[4])
{
	for (int i = 0; i < 3; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			printf("%d ", brr[i][j]);
		}
		printf("\n");
	}
}

void Show(int(*brr)[4],int row)
{
	for (int i = 0; i < row; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			printf("%d ", brr[i][j]);
		}
		printf("\n");
	}
}

//int main()
//{
//	int a[3][4] = { 1,2,3,4,5,6,7,8,9,10,11,12 };
//	Show(a, 3);
//	//Show(a);
//	/*for (int i = 0; i < 3; ++i)
//	{
//		for (int j = 0; j < 4; ++j)
//		{
//			printf("%d ", a[i][j]);
//		}
//		printf("\n");
//	}*/
//
//
//	return 0;
//}

/*
	通过指针引用字符串

	字符串常量和字符数组:
*/

//int main()
//{
//	char str1[] = "hello world"; // 是字符数组,是字符串
//	// char* str2 = "hello world"; // 是字符串,是字符常量  在vs2022中语法错误
//	const char* str2 = "hello world"; // 是字符串,是字符常量
//	// "hello world"需要12个字节的空间,如果是32位系统,str2才要4字节
//	printf("%s\n%s\n", str1, str2);
//
//	str1[0] = 'x'; // 数组中每一个元素都能修改
//	str2[0] = 'x'; // 能编译,但是运行崩溃(字符串常量,不能修改)
//
//	return 0;
//}

/*
	const: 不允许修改(其修饰的)内容

	1. 基本类型对于const是透明的 例如: const int ca = 10;等同于 int const ca =10;
	2. const修饰直接右边的值
*/

//int main()
//{
//	int a = 10;
//	a = 20;
//	printf("%d\n", a);  // 可读可写
//	const int ca = 10; // 只读,不允许修改ca的值
//	ca = 20; // 错误
//
//	return 0;
//}

//int main()
//{
//	int a = 10;
//	int b = 20;
//	int* p = &a;
//	p = &b; // 修改p的内容
//	*p = 100; // 修改*p的内容
//	printf("%d,%d", p, *p);
//
//	const int* p2 = &a;
//	p2 = &b;
//	// *p2 = 100; // 错误
//	int const* p3 = &a; // 等同p2
//	p3 = &a;
//	// *p3 = &a; // 错误
//	int* const p4 = &a;
//	// p4 = &b; // 错误
//	*p4 = 100;
//
//	return 0;
//}


/*
	不适用库函数,实现字符串复制

	字符串和普通数组的区别: 
		字符串可以通过'\0'判断结尾
*/


// des:目的地址
// src: 源字符串的地址 

//void Mystrcpy(char* des,const char* src)
//{
//	int i;
//	for (i = 0; src[i] != '\0'; ++i)
//	{
//		des[i] = src[i];
//	}
//	des[i] = '\0';
//}
//
//
//int main()
//{
//	char str1[] = "abcde";
//	char str2[10];
//	// 通过调用Mystrcpy,实现把str1复制到str2中
//	Mystrcpy(str2, str1);
//	// strcpy()
//	printf("str2=%s", str2);
//	
//
//	return 0;
//}

/*
	指向函数的指针     把函数作为参数传递
	函数族
	标准规定: 函数名也表示函数的入口地址
*/

int Max(int a,int b)
{
	return a >= b ? a : b;
}

int Min(int a, int b)
{
	return a <= b ? a : b;
}

int Avg(int a, int b)
{
	return (a + b) / 2;
}

//int main()
//{
//	int(*pfun)(int, int);// pfun一定是指针,该指针指向函数,函数参数为int类型,返回值也是int
//	pfun = Max;
//	printf("%d\n", pfun(10, 20));

	//pfun = Min;
	//printf("%d\n", pfun(10, 20));

	//pfun = Avg;
	////pfun = &Avg;
	//printf("%d\n", pfun(10, 20));

//	return 0;
//}


/*
	快排

	qsort: 最不好处理的如何比较两个数据的大小

	提供比较依据
*/

int Cmp_int(const void* vp1, const void* vp2)
{
	return *(int*)vp1 - *(int*)vp2; // 还原本质
}

/*
	返回值: 第一个 > 第二个  返回大于0的数字
			第一个 == 第二个 返回0
			第一个 < 第二个  返回小于0的数字
*/

int Cmp_double(const void* vp1, const void* vp2)
{
	double tmp = *(double*)vp1 - *(double*)vp2;
	if (tmp > 0)
	{
		return 1;
	}
	else if (tmp < 0)
	{
		return -1;
	}
	else
	{
		return 0;
	}
		
}

//int main()
//{
//	int arr[] = { 1,3,5,9,0,12,13,41,22,56,6,2 };
//	// 对arr排序
//	double brr[] = { 34.5,12.3,56.7,89.2,34.3,34.2 };
//	// 对brr排序
//
//	int len1 = sizeof(arr) / sizeof(arr[0]);
//	int len2 = sizeof(brr) / sizeof(brr[0]);
//
//	qsort(arr, len1, sizeof(arr[0]), Cmp_int);
//	qsort(brr, len2, sizeof(brr[0]), Cmp_double);
//	// 库函数,快排
//
//	return 0;
//}

/*
	局部变量: 分配的内存区域在栈,很小(1-10M)
	动态内存分配
		使用的场景:
			1.需要大容量内存时
			2.在一个函数创建的内存在别的函数中还需要使用
*/

char* GetMemroy()
{
	//char str[] = "梦想总是要有的,万一实现了呢";
	char* str = (char*)malloc(100 * sizeof(char));
	strcpy(str, "梦想总是要有的,万一实现了呢");

	return str;// 已经被销毁
}

//int main()
//{
//	// char arr[100000000] = "";  // 程序崩溃
//	// printf("好了\n");
//
//	char* p = GetMemroy();
//	printf("%s\n", p);
//
//
//	return 0;
//}

/*
	如何创建动态内存
	void: 没有,可以修饰返回值和参数列表
	void *: 没有类型信息的指针,这个指针仅仅只记录地址
		malloc: 创建内存,需要引用 <stdlib.h> 失败返回NULL 成功返回地址
		calloc: 创建内存  把每个元素置为0
		realloc: 创建内存  主要用于修改动态内存的大小
		free: 释放内存  如果不是释放,会出现内存泄漏
*/

int main()
{
	// 需要创建100M的内存
	/*void* p = malloc(1024 * 1024 * 100);
	if (p == NULL)
	{
		printf("申请失败了\n");
	}
	printf("好了");
	getchar();*/

	// 申请100个int单元
	/*int n = 100;
	int *arr = (int *)calloc(n,sizeof(int));
	for (int i = 0; i < n; ++i)
	{
		arr[i] = i;
	}*/

	/*char* p = GetMemroy();
	printf("%s\n", p);
	free(p);*/

	// 申请10个int单元
	int n = 10;
	//int arr[n]; // vs2022变量不能作为数组长度
	int* arr = (int*)malloc(n * sizeof(int));
	for (int i = 0; i < n; ++i)
	{
		arr[i] = i;
	}
	// 使用过程中,发现内存不够,需要2n个单元  realloc
	arr = (int*)realloc(arr,2*n*sizeof(int));  // 光标移动到然后F1, 查看版本手册
	for (int i = 0; i < 2 * n; ++i)
	{
		arr[i] = i;
	}
	free(arr);

	return 0;
}
