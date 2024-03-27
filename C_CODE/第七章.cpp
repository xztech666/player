#define _CRT_SECURE_NO_WARNINGS  //预定义,因为scanf不安全
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>

/*
	函数:
		1. 功能更清晰
		2. 提高代码的使用率

	返回值  函数名(参数列表)
	{
		函数体
	}
	函数名: 独一无二
	void: 无, 可以修饰返回值(必须写)或者函数列表(可以省略)
	return: 返回
	函数定义后,不能直接运行,需要调用
	返回值: 函数计算的结果通过返回值返回给函数的调用者
	函数调用没有限制,函数定义有限制
						函数定义的内部不能定义另外一个函数
*/

/*
void Max1()
{
	int a;
	int b;
	scanf("%d%d", &a, &b);
	int c = a >= b ? a : b;
	printf("%d\n", c);
}

void Max2(int a, int b) // 形式参数,a,b  已经有数据,不需要通过scanf获取
{
	int c = a >= b ? a : b;
	printf("%d\n", c);
}


int Max(int a, int b)
{
	int c = a >= b ? a : b;
	return c;  // 返回c
}

int Max3(int a, int b, int c)
{
	//int d = Max2(a, b); // int d = void(没有)
	int d = Max(a, b);
	int e = Max(c, d);
	return e;
	 
}

// 输出两个数的最大值

int main()
{
	//int a;
	//int b;
	//scanf("%d%d", &a, &b);
	//int c = a >= b ? a : b;
	//printf("%d\n", c);

	//Max1();  // 参数列表  函数调用

	//Max2(10, 20);  // 实际参数 a,b
	//double n = pow(5, 3);
	//double m = sqrt(10);
	//printf("%lf\n", n);
	//printf("%lf\n", m);

	int z = Max3(100, 200, 640);
	printf("%d\n", z);

	return 0;
}
*/



// 输入两个实数,用函数求他们的和

//float Add(float a, float b)
//{
//	return a + b;
//
//}
//
//
//int main()
//{
//	// 从上往下
//	float a = Add(12.5f, 23.5f);
//	printf("%f\n", a);
//
//	return 0;
//}

// 如果函数定义放在函数使用(调用)的后面,那么在前面必须有函数声明

//int main()
//{
//	float Add(float a, float b);
//	// 
//	float a = Add(12.5f, 23.5f);
//	printf("%f\n", a);
//
//	return 0;
//}
//
//float Add(float a, float b)
//{
//
//	return a + b;
//}


/*
	函数嵌套
		自己实现把字符串中的大写字符换成小写
*/


//void Mystrlwr(char str[])
//{
//	for (int i = 0; str[i] != '\0'; ++i)
//	{
//		if (isupper(str[i])) // 是大写字母
//		{
//			str[i] = tolower(str[i]); // 大写字母转换为小写字母
//		}
//	}
//}
//
//int main()
//{
//	char str[] = "asdasfDDFDSFQ865sad ASD";
//	Mystrlwr(str);
//	printf("%s\n", str);
//
//	return 0;
//}


// 统计一个数字中1的个数(常考)
// 例如: 123->1;  12121->3;  11111->5
/*
	n: 需要统计的数字,  例如123
	返回值: 返回1的个数
	取个位  得个位  丢各位  统计
	12121   1       1212      1
	1212    2       121       1
	121     1       12        2
	12      2       1         2
	1       1       1         3
	0
*/

//int Count(int n)
//{
//	int sum = 0; // 统计1的个数
//	while (n != 0)
//	{
//		if (n % 10 == 1)  // 得个位
//		{
//			sum++;
//		}
//		n /= 10; // 丢弃个位
//	}
//
//	return sum;
//}
//
//int main()
//{
//	printf("1的个数%d\n", Count(123123));
//}


/*
	递归求年龄
*/
