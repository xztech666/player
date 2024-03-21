//#define _CRT_SECURE_NO_WARNINGS  //预定义,因为scanf不安全
//#include<stdio.h>
//#include<math.h>

/*
	循环: for,while,do while,break,continue

	for(表达式1; 表达式2; 表达式3)
	{
		语句块1
	}
	表达式1: 循环因子初始化,最早被执行,有且只有一次
	表达式2: 判断,为真循环进行,为假循环结束
	表达式3: 步进,修改循环因子的值,注意它是在语句块1之后执行
	表达式可以省略吗?
		可以,但是分号不能省略
*/

//int main()
//{
//	int i = 0;
//	for (;;)
//	{
//		if (i >= 3)
//		{
//			break;
//		}
//		printf("%d\n", i);
//
//		++i;
//	}
//
//	return 0;
//}

//  求1+2+3+...+100的和

//int main()
//{
//	int sum = 0;
//	for (int i = 1; i <= 100; i++)
//	{
//		sum += i;
//	}
//	printf("总和是:%d\n", sum);
//
//	return 0;
//}

/*
	while(表达式1)
	{
		语句块1
	}
	表达式1 如果为真,循环继续,为假循环结束,不能省略
*/

//int main()
//{
//	int i = 0;
//	while (i < 3)
//	{
//		printf("%d\n", i);
//		++i;
//	}
//
//	return 0;
//}

/*
	do
	{
		语句块1
	}
	while(表达式1);

	表达式1如果为真,循环继续.为假循环结束,不能省略

*/

//int main()
//{
//	int i = 0;
//	do
//	{
//		printf("%d\n", i);
//		++i;
//	} while (i < 3);
//	
//}

/*
	do while 实现1+2+3+4+...+100
*/

//int main()
//{
//	int sum = 0;  // 总和初始化
//	int i = 1;  // 循环因子
//	do
//	{
//		sum += i;
//		i++;
//	} while (i <= 100);
//	printf("总和为:%d\n", sum);
//
//	return 0;
//}

/*
	break: 跳出当前循环(一层)
*/

//int main()
//{
//	int sum = 0;
//	int n;
//	int i;
//	for(i = 1; i <= 1000; i++)
//	{
//		scanf("%d", &n);
//		sum += n;
//		if (sum >= 100000)
//		{
//			break;
//		}
//	}
//
//	printf("人数=%d,平均数额=%.2lf\n", i, (double)sum / i);
//
//	return 0;
//}

/*
	continue: 提前结束本次循环,直接进入下一次循环
*/

// 输出100-200之间的不能被3整除的数

//int main()
//{
//	for (int i = 100; i < 130; i++)
//	{
//		if (i % 3 == 0)
//			continue;
//		printf("%d\n", i);
//	}
//	return 0;
//}

// 输出4*5的矩阵
// printf("%-3d ", i * j);// 每个数字占三格,左对齐

//int main()
//{
//	for (int i = 1; i <= 4; i++)// 行
//	{
//		for (int j = 1; j <= 5; j++)// 列
//		{
//			printf("%-3d ", i * j);// 每个数字占三格,左对齐
//		}
//		printf("\n");
//	}
//
//	return 0;
//}

/*
	求Π的近似值
*/

//int main()
//{
//	double sum = 0;
//	int flg = 1; // 符号
//
//	//1/1000001
//	for (int i = 1; i < 1000000; i += 2) // 10^-6错误, 1e-6
//	{
//		sum += flg * 1.0 / i; // 一定要注意整数除以整数
//		flg *= -1;
//	}
//	printf("pi=%lf\n", sum * 4);
//
//	return 0;
//}

/*
	求斐波那契数列的前四十个数
*/

//int main()
//{
//	int f1 = 1, f2 = 1,f3 = 0;
//	printf("1 1 ");
//	for (int i = 3; i <= 40; i++)
//	{
//		f3 = f1 + f2;
//		printf("%d ", f3);
//		f1 = f2;
//		f2 = f3;
//	}
//	return 0;
//}