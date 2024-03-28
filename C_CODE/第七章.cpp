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
*   函数的递归调用
		直接或者间接调用函数本身
		三部分:
			1.边界条件
			2.前进段
			3.返回段

	数组作为参数传递的结论: 一定要传递数组名和数组长度
*/


/*
	有5个学生坐在一起，问第5个学生多少岁，他说比第4个学生大2岁。问第4个学生岁数，他说比第3个学生大2岁。问第3个学生，又说比第2个学生大2岁。间第2个学生，说比第1个学生大
	2岁。最后问第1个学生，他说是10岁。请问第5个学生多大。

*/


// 用循环解析

//int Age_for(int n)
//{
//	int tmp = 10;
//	for (int i = 1; i < n; i++)
//	{
//		tmp += 2;
//	}
//	return tmp;
//}


// 递归实现

//int Age(int n)  // 求第n个人的年龄
//{
//	int tmp = 10;
//	if (n == 1)   // 边界条件
//	{
//		return tmp;
//	}
//	else
//	{
//		tmp = Age(n - 1) + 2;  // 前进段
//	}
//	return tmp;
//}
//
//
//
//int main()
//{
//	printf("%d\n", Age_for(5));
//	printf("%d\n", Age(5));
//
//	return 0;
//}


// 递归实现斐波那契数列

//int fibonacci(int n) {
//	if (n <= 1) {
//		return n;
//	}
//	else {
//		return fibonacci(n - 1) + fibonacci(n - 2);
//	}
//}
//
//int main() {
//	int n;
//	printf("请输入要计算的斐波那契数列的项数：");
//	scanf("%d", &n);
//
//	printf("斐波那契数列的第 %d 项为：%d\n", n, fibonacci(n));
//
//	return 0;
//}


/*
	分析函数递归调用的过程

	int Age(int n)  // 求第n个人的年龄
//  { 
//	int tmp = 10;
//	if (n == 1)   // 边界条件
//	{
//		return tmp;
//	}
//	else
//	{
//		tmp = Age(n - 1) + 2;  // 前进段
//	}
//	return tmp;
//  }

	int main()
	{
		Age(5);
	}

*/

/*
	栈(函数调用)

	为Age(5)分配内存空间
		
		保存现场                         恢复现场    18
		为Age(4)分配内存空间
		保存现场                         恢复现场    16
		为Age(3)分配内存空间             
		保存现场                         恢复现场    14
		为Age(2)分配内存空间             
		保存现场                         恢复现场    12
		为Age(1)分配内存空间      ->     10

	栈帧,函数将结束才能回收
*/


// 阶乘递归实现
// 0! == 1,1! == 1,n! == n * (n-1)!

//long long Fac(int n) // Fac(n)  求阶乘
//{
//	if (n == 0 || n == 1)
//	{
//		return 1;
//	}
//	return n * Fac(n - 1);
//}
//
//int main()
//{
//	for (int i = 0; i < 10; ++i)
//	{
//		printf("%d!=%lld\n", i, Fac(i));
//	}
//}


/*
	经典例题: Hanoi塔
	有三根杆子A，B，C。A杆上有 N 个 (N>1) 穿孔圆盘，盘的尺寸由下到上依次变小。要求按下列规则将所有圆盘移至 C 杆：
	每次只能移动一个圆盘；
	大盘不能叠在小盘上面。
	提示：可将圆盘临时置于 B 杆，也可将从 A 杆移出的圆盘重新移回 A 杆，但都必须遵循上述两条规则。

	一定存在: 上面n-1个盘子在B上
*/

// 把n个盘子,从a通过b移到c
//void Hanoi(int n, char a, char b, char c)
//{
//	if (n == 1) // 只有一个盘子,直接从A->C
//	{
//		printf("%c->%c\n", a, c);
//	}
//	else
//	{
//		Hanoi(n - 1, a, c, b); // 把上面的n-1个盘子,从a通过c移到b
//		printf("%c->%c\n", a, c);// 把最下面的一个从a移到c
//		Hanoi(n - 1, b, a, c); // 把b上面的n-1个盘子,从b通过a移到c
//	}
//}
//
//int main()
//{
//	Hanoi(64, 'A', 'B', 'C');
//
//	return 0;
//}


// 一维数组作为参数传递,错误应用
// 求一个数组中的最大值
//int Max(int arr[10])  // 声明不起任何作用,C语言不检测形参数组大小,传的首地址作为指针变量
//{
//	int tmp = arr[0]; // 保存最大值
//	for (int i = 1; i < 10; ++i)
//	{
//		if (tmp < arr[i])
//		{
//			tmp = arr[i];
//		}
//	}
//
//	return tmp;
//}
//
//int main()
//{
//	//int arr[] = { 1,5,9,7,15,48,56,12,4,6 };
//	int arr[] = { 1,5,9,7,15,48,56,12,4,6,156,564 };
//	int a = Max(arr); // 数组作为参数传递时,只传数组的起始地址
//	printf("最大值为%d\n", a);
//
//}


// 修改后的代码
//arr: 数组名
//n: 数组长度
//int Max(int arr[], int n)  // arr本质是指针,不是数组
//{
//	int tmp = arr[0]; // 保存最大值
//	for (int i = 1; i < n; ++i)
//	{
//		if (tmp < arr[i])
//		{
//			tmp = arr[i];
//		}
//	}
//
//	return tmp;
//}
//
//int main()
//{
//	int arr[] = { 1,5,9,7,15,48,56,12,4,6,156,564 };
//	int a = Max(arr, sizeof(arr) / sizeof(arr[0]));
//	printf("最大值为%d\n", a);
//
//	return 0;
//}


// 求一个数组的平均数
// arr: 数组名
// n: 数组长度

//float Avg(double arr[], int n)
//{
//	double sum = 0;
//	for (int i = 0; i < n; ++i)
//	{
//		sum += arr[i];
//	}
//	return sum / n;
//}
//
//int main()
//{
//	double arr[] = { 67,78,89.5,100,99,80 };
//	printf("%lf\n", Avg(arr, sizeof(arr) / sizeof(arr[0])));
//
//	return 0;
//}


// 用选择法对数组中10个整数由小到大排序
// arr: 数组名
// n: 数组长度

/*
	选择法排序: 
		每次都从排序中找最小值,和待排序第一个值交换
		4    2    1     5     3
		1    2    4     5     3
		1    2    3     5     4
		1    2    3     4     5
*/

//void SelectSort(int arr[],int n)
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
//		// 把最小的放在最前面
//		tmp = arr[i];
//		arr[i] = arr[k];
//		arr[k] = tmp;   
//	}
//}

// 输出长度为n的数组arr所有元素
//void Show(int arr[], int n)
//{
//	for (int i = 0; i < n; ++i)
//	{
//		printf("%d ", arr[i]);
//	}
//	printf("\n");
//}
//
//int main()
//{
//	int arr[] = { 4,2,1,5,3 };
//	SelectSort(arr, sizeof(arr) / sizeof(arr[0]));
//	Show(arr, sizeof(arr) / sizeof(arr[0]));
//
//	return 0;
//}


// 输出row行,col列的二维数组arr
//void Show(int arr[][4], int row, int col)   // // 代码并不完美,后面指针会完善代码
//{
//	for (int i = 0; i < row; i++)
//	{
//		for (int j = 0; j < col; ++j)
//		{
//			printf("%d ", arr[i][j]);
//		}
//		printf("\n");
//	}
//}

//int main()
//{
//	int arr[][4] = { 1,2,3,4,5,6,7,8,9 };
//	Show(arr, 3, 4);
//}


// 求3*4二维数组的最大值
//int Max(int arr[][4], int row, int col)   // 代码并不完美,后面指针会完善代码
//{
//	int tmp = arr[0][0];
//	for (int i = 0; i < row; i++)
//	{
//		for (int j = 0; j < col; ++j)
//		{
//			if (arr[i][j] > tmp)
//			{
//				tmp = arr[i][j];
//			}
//		}
//	}
//	return tmp;
//}
//
//int main()
//{
//	int arr[][4] = { 1,2,3,4,5,6,7,8,9 };
//	Show(arr, 3, 4);
//	printf("%d\n", Max(arr, 3, 4));
//
//	return 0;
//}


/*
	全局变量和局部变量

	全局变量: 定义在函数外部的变量   少用,不安全
	局部变量: 定义在函数内部的变量,包括形参

	         作用域   生命周期   默认值
全局变量  从定义开始,到文件结束,都能使用  程序运行创建,程序结束才销毁  默认为0
局部变量  只在本函数中使用(优点)   进入函数创建,函数结束就销毁    默认值无效

static: 静态,修饰变量或者函数
静态局部变量: 在函数内部使用,从第一次进入函数创建,程序结束才销毁,默认值为0
*/

