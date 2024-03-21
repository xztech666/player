//#define _CRT_SECURE_NO_WARNINGS  //预定义,因为scanf不安全
//#include<stdio.h>
//#include<math.h>

/*
*   单分支
	if(表达式1)
	{
		语句块1
	}
	// 如果表达式1为真,执行语句块1

	双分支
	if(表达式1)
	{
		语句块1x
	}
	else
	{
		语句块2
	}
	//如果表达式1为真则执行语句块1,否则执行语句块2

	多分枝
	if(表达式1)
	{
		语句块1
	}
	else if(表达式2)
	{
		语句块2
	}
	else
	{
		语句块n
	}
*/

//从小到大输出两个数

//int main()
//{
//	double a, b;
//	scanf("%lf %lf", &a, &b);
//	if (a > b)
//	{
//		printf("%lf %lf\n", b, a);
//	}
//	else
//	{
//		printf("%lf %lf\n", a, b);
//	}
//	return 0;
//}

// 输入三个数a, b, c,要求按由小到大的顺序输出

//int main()
//{
//	double a, b, c;
//	scanf("%lf%lf%lf", &a, &b, &c);
//
//	double tmp;
//	//a是a,b的最小值
//	if (a > b)
//	{
//		tmp = a;
//		a = b;
//		b = tmp;
//	}
//	//a是a,c最小值
//	if (a > c)
//	{
//		tmp = a;
//		a = c;
//		c = tmp;
//	}
//	//b是b,c的最小值
//	if (b > c)
//	{
//		tmp = b;
//		b = c;
//		c = tmp;
//	}
//
//	//a保存最小值,b保存第二小,c保存最大值
//	printf("%lf %lf %lf\n", a, b, c);
//
//	return 0;
//}

//分段函数

//int main()
//{
//	int x;
//	scanf("%d", &x);
//	int y;
//	if (x < 0)
//	{
//		y = -1;
//	}
//	else if (x == 0)
//	{
//		y = 0;
//	}
//	else
//	{
//		y = 1;
//	}
//	printf("%d\n",y);
//
//	return 0;
//}

/*
	switch (整型表达式)   char,bool,int,short,long long int,枚举
	{
		case 常量表达式1:
			语句块1
			break
		case 常量表达式2:
			语句块2
			break
		default:
			语句块

	}
*/

//  运输公司对用户计算运输费用

//int main()
//{
//	int s;
//	scanf("%d", &s);
//	double a = 1;
//	switch (s/250)
//	{
//	case 0:
//		a = 1;
//		break;
//	case 1:
//		a = 0.98;
//		break;
//	case 2:
//		a = 0.95;
//		break;
//	case 3:
//		a = 0.92;
//		break;
//	case 4:
//	case 5:
//	case 6:
//	case 7:
//		a = 0.92;
//		break;
//	default:
//		break;
//		//switch太繁琐了
//	}
//
//}
