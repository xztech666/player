//#define _CRT_SECURE_NO_WARNINGS  //预定义,因为scanf不安全
//#include<stdio.h>
//#include<math.h>

/*
	华氏温度转换摄氏温度
*/

//int main()
//{
//	double f;
//	scanf("%lf", &f);    //读取double的数据必须使用%lf,易错
//	double c = 5.0 / 9 * (f - 32);
//	printf("%lf\n", c);
//
//	return 0;
//}

//int main()
//{
//	double p0 = 1000, r1 = 0.0036, r2 = 0.0225, r3 = 0.0198;
//	printf("活期本息和:%.2lf\n", p0 * (1 + r1));
//	printf("一年本息和:%.2lf\n", p0 * (1 + r2));
//	printf("两次半年定期本息和:%.2lf\n", p0 * (1 + r3 / 2) * (1 + r3 / 2));
//	//%.2lf:  保留两位小数
//
//	return 0;
//}

/*
	错误越早被发现,代价越小
*/

//#define DOUBLE(x) x + x
//
//int main()
//{
//	printf("%d\n", 2 * DOUBLE(10));  //常考
//	// 宏定义不是函数, 2 * DOUBLE(10) 替换为  2 * 10 + 10 -> 30
//}

/*
	给定一个大写字母,输出小写字母
*/

//int main()
//{
//	char ch;
//	printf("请输入一个大写字母:\n");
//	scanf("%c", &ch);
//	if ('A' <= ch && ch <= 'Z')
//	{
//		printf("%c\n", ch + ('a' - 'A'));
//	}
//	
//	return 0;
//}

/*
	求三角形面积(不判断数据的合法性)
*/

//int main()
//{
//	int a, b, c;
//	printf("请输入三角形三条边的长度:\n");
//	scanf("%d %d %d", &a, &b, &c);
//	if (a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a)
//	{
//		double s = (a + b + c) / 2.0;   //细节,具体看前面代码
//		double area = sqrt(s * (s - a) * (s - b) * (s - c));
//		printf("面积=%lf\n", area);
//	}
//	else
//	{
//		printf("很抱歉,您输入的数据并不合法!\n");
//	}
//	return 0;
//}

/*
	ax^2 + bx + c = 0, 求方程的根
*/

//int main()
//{
//	double x1, x2;
//	int a, b, c;
//	printf("请输入三个数:");
//	scanf("%d %d %d", &a, &b, &c);
//	int d = b * b - 4 * a * c;
//	if (d < 0)
//	{
//		printf("无实根!");
//	}
//	else if (d > 0)
//	{
//		x1 = (-b + sqrt(d)) / (2 * a);
//		x2 = (-b - sqrt(d)) / (2 * a);
//
//		printf("两个实根分别为: x1 = %.2lf, x2 = %.2lf\n", x1, x2);
//	}
//	else
//	{
//		double x = -b / (2 * a);
//
//		printf("只有一个实根为:x = %.2lf\n", x);
//	}
//	
//	return 0;
//}

/*
	getchar  输入一个字符
	putchar  输出一个字符
*/

//int main()
//{
//	//char ch = getchar();  //从键盘获取一个字符并返回
//	//putchar(ch);  //输出一个字符到屏幕
//
//	char ch;
//	//读取一行字符
//	while (((ch = getchar()) != '\n'))
//	{
//		putchar(ch);
//	}
//	
//	return 0;
//}
