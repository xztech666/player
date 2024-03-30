#define _CRT_SECURE_NO_WARNINGS  //预定义,因为scanf不安全
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>

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

int Fun(int a, int b, int c,double* x1,double* x2)
{
	int d = b * b - 4 * a * c;
	*x1 = (-b + sqrt(d)) / (2 * a);
	*x2 = (-b - sqrt(d)) / (2 * a);

	return 2; // 返回两个根
}


int main()
{
	double x1;
	double x2;
	Fun(3, 5, 1, &x1, &x2);
	printf("%lf,%lf\n", x1, x2);

	return 0;
}
