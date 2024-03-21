//#define _CRT_SECURE_NO_WARNINGS  //预定义,因为scanf不安全
//#include<stdio.h>
//#include<math.h>

/*
	五的阶乘
*/

//int main()
//{
//	int a = 1;
//	for (int i = 2; i <= 5; i++)
//	{
//		a = a * i;
//	}
//	printf("%d\n", a);
//	return 0;
//}

/*
	判定2000-2500之间的闰年

	/: 除,得到商,注意整除问题(整数/整数,结果为丢弃小数的整数), 10/3 -> 3
	%: 取余,得到余数
*/

//int main()
//{
//	for (int year = 2000; year <= 2500; year++)
//	{
//		if (year % 4 == 0 && year % 100 != 0 || year % 4 == 0)
//		{
//			printf("%d是闰年\n", year);
//		}
//	}
//
//	return 0;
//}

/*
	sizeof: 求字节数
	数据类型:(字节数)
	字符:char(1)
		用于保存英文字符,不能保存中文,能表示2^8(256)种不同情况
	整数:short(2) int(4, 默认) long(4) long long(8)
	小数:float(4) double(8, 默认)
*/

/*
	真: C99 True   非0
	假: C99 False   0
	!: 非,不是               注意短路现象
	&&: 与  都为真,才为真    注意短路现象
	||: 或  一个真
	++i,i++    单独使用无区别
	前置先算,后置后算
		eg:   int j = 10,i = 10
			  j = ++i   ->   j = 11,i=11
			  j = i++   ->   j = 10,i=11
	(类型)变量: 把变量强制转换为()中的类型
*/

//int main()
//{
//	for (int i = 1; i <= 100; i++)
//	{
//		printf("%d\t", i);
//		if (i % 10 == 0)
//		{
//			printf("\n");
//		}
//	}
//
//	return 0;
//}

/*
	阿里面试题:
		设x,y,t均为int型变量,则执行语句: t = 3; x = y = 2; t = x++ || ++y,变量t和y的值分别为:
			t = 1,y = 2
*/

/*
	给出一个大于或等于3的正整数,判断它是不是一个素数
*/

//int main()
//{
//	int n;
//	scanf("%d", &n);
//	for (int i = 2; i <= sqrt(n); i++)
//	{
//		if (n % i == 0)
//		{
//			printf("%d不是素数\n", n);
//			return 0;
//		}
//	}
//	printf("%d是素数\n", n);
//	
//	return 0;
//}

/*
	求1 - 1/2 + 1/3 - 1/4 + ... + 1/99 - 1/100
*/

//int main()
//{
//	double sum = 0;
//	int sign = 1;
//	for (int demo = 1; demo <= 100; demo++)
//	{
//		sum += sign * 1.0 / demo;   //注意整数除以整数会整除
//		sign *= -1;
//	}
//	printf("%lf\n", sum);
//
//	return 0;
//}
