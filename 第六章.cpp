//#define _CRT_SECURE_NO_WARNINGS  //预定义,因为scanf不安全
//#include<stdio.h>
//#include<math.h>
//#include<string.h>
//#include<ctype.h>

/*
	数组: 多个同类型的数据
	定义: 类型  数组名[长度]
	初始化: 在定义的同时,赋值(经常考试),只初始化一部分则剩余部分为0
*/

//int main()
//{
//	int a = 10;  // 定义一个int类型变量a,并且存放数字10
//	int arr[10]; // 定义一个int类型的数组变量arr,长度为10
//	int brr[10] = { 1,2,3,4,5,6,7,8,9,10 }; // 初始化
//	int crr[10] = { 1,2,3,4,5 }; //1,2,3,4,5,0,0,0,0,0
//	int drr[] = { 1,2,3,4,5, }; //自动推导长度,刚好能放下所有元素
//	// int crr[]; // 错误,没有给值
//
//	return 0;
//}

//int main()
//{
//	int a = 10;
//	int arr[a];        // vs2022数组长度为变量是错误的,c99数组长度可以是变量
//  
//  int a = 4;
//  arr[a] = 100;     // 可以这么使用
//}

/*
	如何使用数组元素?
	下表从0开始
	下标时可以使用变量   对的
*/

//int main()
//{
//	int arr[10] = { 1,2,3,4,5,6,7,8,9,10 };
//	arr[2] = 10;
//	int a = 4;
//	arr[a] = 100;
	// printf不能直接输出整个数组
	// printf("%d\n,arr");  // 不对,输出的是arr的地址
//	for (int i = 0; i < 10; ++i)
//	{
//		printf("%d ", arr[i]);
//	}
//
//	return 0;
//}

// 数组arr长度公式: sizeof(arr)/sizeof(arr[0])   arr不能为形参


// 逆序输出
//int main()
//{
//	int arr[] = { 0,1,2,3,4,5,6,7,8,9 };
//	for (int i = sizeof(arr) / sizeof(arr[0]) - 1; i >= 0; i--)  // 单独用的时候--i,i--一样
//	{
//		printf("%d ", arr[i]);
//	}
//	return 0;
//}

//  用数组来处理求斐波那契数列问题
// 1,1,2

//int main()
//{
//	int arr[40] = { 1,1 }; //保存斐波那契数列前40项的值
//	//arr[2] = arr[0] + arr[1]; // 2
//	//arr[3] = arr[1] + arr[2]; // 3
//	//arr[4] = arr[2] + arr[3]; // 5
//
//	for (int i = 2; i < sizeof(arr) / sizeof(arr[0]); i++)
//	{
//		arr[i] = arr[i - 2] + arr[i - 1];
//	}
//	for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); ++i)
//	{
//		printf("%d ", arr[i]);
//		if (i % 10 == 9)
//		{
//			printf("\n");
//		}
//	}
//
//
//	return 0;
//
//}

// 对十个地区的面积由小到大排序
// 冒泡排序: 从头到尾两两比较,大的往后,小的往前


//int main()
//{
//	int arr[] = { 3,7,5,1,8,9,10,15,48,26,189,546 };
//	int len = sizeof(arr) / sizeof(arr[0]);
//	int tmp;
//	for (int i = 0; i < len - 1; ++i) // 循环的趟数, 5个数循环4次
//	{
//		for (int j = 0; j + 1 < len - i; ++j) //每一趟从头到尾(不包含有序的数据), len-i 未排序的数
//		{
//			if (arr[j] > arr[j + 1])
//			{
//				tmp = arr[j];
//				arr[j] = arr[j + 1];
//				arr[j + 1] = tmp;
//			}
//		}
//	}
//	for (int i = 0; i < len; i++)
//	{
//		printf("%d ", arr[i]);
//	}
//	printf("\n");
//
//	return 0;
//}

/*
	二维数组
		定义: 类型 数组名[行][列]     行列式
		初始化, 在定义的同时赋值
		访问元素: 通过行,列下表访问
*/

//int main()
//{
//	int arr[10] = { 1,2,3,4,5,6,7,8,9,10 };
//	int brr[3][4] = { {1,2,3,4},{5,6,7,8},{9,10,11,12} };
//	int brr[3][4] = { 1,2,3,4,5,6,7,8,9,10 }; // 行优先,先从行开始,剩余部分为0
//	int crr[][4] = { 1,2,3,4,5,6,7,8,9,10 }; // 自动推导
//  int drr[][] = {1,2,3,4,5,6,7,8,9};     //错误
//
//	return 0;
//}


//int main()
//{
//	int brr[3][4] = { {1,2,3,4},{5,6,7,8},{9,10,11,12} };
//	brr[1][2] = 100;
//
//	for (int i = 0; i < 3; i++) // 行
//	{
//		for (int j = 0; j < 4; j++) // 列
//		{
//			printf("%d ", brr[i][j]);
//		}
//		printf("\n");
//	}
//
//	return 0;
//}

/*
	矩阵逆置: 行列互换  下标互换
*/

//int main()
//{
//	int a[2][3] = { 1,2,3,4,5,6 };
//	int b[3][2];
//
//	for (int i = 0; i < 2; ++i) // 行
//	{
//		for (int j = 0; j < 3; ++j) // 列
//		{
//			b[j][i] = a[i][j];
//		}
//	}
//
//	for (int i = 0; i < 3; ++i)
//	{
//		for (int j = 0; j < 2; ++j)
//		{
//			printf("%d ", b[i][j]);
//		}
//		printf("\n");
//	}
//}


/*
 有一个3*4的矩阵,要求求出其中值最大的那个元素的值,以及其所在的行号和列号
*/

//int main()
//{
//	int a[3][4] = { 3,5,4,9,26,59,48,165,1,5,9,4 };
//	int max = a[0][0];
//	int row = 0; // 行 row
//	int col = 0; // 列 colum
//
//	for (int i = 0; i < 3; ++i)
//	{
//		for (int j = 0; j < 4; ++j)
//		{
//			if (a[i][j] > max)
//			{
//				max = a[i][j];
//				row = i;
//				col = j;
//			}
//		}
//	}
//	printf("其中最大值是%d,在第%d行,第%d列", max, row, col);
//
//	return 0;
//}

/*
	字符数组: 非常重要,用的多,考的多
	定义: char 数组名[长度];

	字符串: 用""包括的字符序列,可以是0个及以上的字符.
			末尾有一个隐藏的'\0'作为结尾标记

		有两种形式的字符串: 用""包括
							有'\0'的字符数组

*/

//int main()
//{
//	char str1[10]; //定义长度为10的字符数组,没有初始化,随机值  生成烫烫烫
//	//printf("%s\n", str1);
//
//	str1[0] = 'l';
//	str1[1] = ' ';
//	str1[2] = 'a';
//	//printf("%s", str1); // %s输出字符串, 错误,str1不是字符串
//
//	char str2[10] = { 'l',' ','a','m' }; // 初始化 只初始化了一部分,剩余为0
//	char str3[10] = "abcde";
//
//	//printf("%s", str2); // 是字符串
//	//printf("%s", str3); // 是字符串
//
//	//0的表现
//	printf("%d,%d,%d,%d\n", false, '\0', 0, NULL);
//
//	return 0;
//}


/*
	字符数组和字符串
*/

//int main()
//{
//	char str1[10]; // 字符数组,不是字符串
//	char str2[10] = "abcde"; // 字符数组,是字符串
//	char str3[] = "abcde"; // 字符数组,是字符串,长度为6
//	char str4[] = { 'a','b','c','d','e' }; // 字符数组,不是字符串,长度为5
//	char str5[10] = { 'a','b','c','d','e' }; // 字符数组,是字符串,只初始化了一部分
//
//	const char* str6 = "abcde";
//
//	printf("%s", str1);
//	printf("%s", str2);
//	printf("%s", str3);
//	printf("%s", str4);
//	printf("%s", str5);
//
//	return 0;
//}


/*
	输出是字符数组,但不是字符串
*/


//int main()
//{
//	char str[] = { 'a','b','c','d','e' }; // 是字符数组,不是字符串
//	//printf("%s\n", str); // 错误,%s输出字符串,str不是字符串
//
//	for (int i = 0; i < sizeof(str) / sizeof(str[0]); ++i) // 作为数组处理
//	{
//		putchar(str[i]);
//	}
//
//	return 0;
//}


/*
	字符串的输出
*/


//int main()
//{
//	char c[16] = { 'l',' ','a','m',' ','a',' ','s','t','u','d','e','n','t','.'};
//	
//	printf("%s\n", c);
//
//	return 0;
//}


/*
	输出一个菱形图
		1. 字符数组

*/

//int main()
//{
//	char c[5][5] = { {' ',' ','*',' ',' '},{' ','*',' ','*',' '},{'*',' ',' ',' ','*'},{' ','*',' ','*',' '},{' ',' ','*',' ',' '} };
//
//	for (int i = 0; i < 5; ++i)
//	{
//		for (int j = 0; j < 5; ++j)
//		{
//			putchar(c[i][j]); // printf("%c",c[i][j]);
//		}
//		putchar('\n');  //printf("\n");    注意putchar里面是单引号
//	}
//
//	return 0;
//}


/*
	输出一个菱形图
		2.字符串

*/


//int main()
//{
//	char c[5][6] = { "  *  "," * * ","*   *"," * * ","  *  " }; // c[5][6]  六列是因为要有'\0'
//
//	for (int i = 0; i < 5; ++i) // 只需要输出行
//	{
//		printf("%s\n", c[i]);
//	}
//
//	return 0;
//}

/*
	字符数组的输入
*/

//int main()
//{
//	char c[6];
//	for (int i = 0; i < 6; ++i) // 从键盘读取6个字符
//	{
//		scanf("%c", &c[i]); // getchar
//	}
//	for (int i = 0; i < 6; ++i)
//	{
//		printf("%c", c[i]); // putchar
//	}
//
//
//	return 0;
//}

/*
	字符串的输入

	在这段代码中，您定义了一个包含6个元素的字符数组 c。
	然后，您使用 scanf() 函数读取用户输入的字符串，并将其存储到数组 c 中。
	最后，使用 printf() 函数将数组 c 中的字符串打印出来。

	然而，这段代码存在一个潜在的问题：当使用 %s 格式化符读取字符串时，
	scanf() 函数会在遇到空格、制表符或换行符时停止读取，
	因此它可能无法正确地读取包含空格的输入。
	另外，将 &c 传递给 scanf() 函数会产生不正确的行为，
	因为数组名 c 已经是指向数组的指针，不需要再使用 & 运算符。
	应该直接将数组名作为参数传递。

*/

//int main()
//{
//	char c[6];
//	scanf("%s", &c); // scanf("%s",c) // &c等同c
//	printf("%s\n", c);
//
//	return 0;
//}


/*
	字符串处理函数:
		puts: 输出一个字符串,并且自带一个换行'\n'
		gets: 输入一个字符串,已经被废除,不安全,  用fgets替代
		scanf_s: 读取字符串后面必须跟大小
*/


//int main()
//{
//	char str[100] = "abcde xyz";
//	/*puts(str);*/
//	char str2[10];
//	//scanf_s("%s", str, 100); // 100是字符串数组的最大容量
//	fgets(str2, 10, stdin); // stdin:标准输入,键盘
//
//	puts(str2);
//	return 0;
//}


/*
	strcpy: 字符串赋值(拷贝)    strcpy(str2,str1); // 把str1的值复制给str2
	strcat: 字符串连接      str1 = str1 + str2  // "abcdexyz"    第一个字符串长度必须要足够
							strcat(str1, str2);
	strcmp: 字符串比较   不能直接用大于,小于号

*/


//int main()
//{
//	int a = 10;
//	int b = a;
//
//	char str1[] = "abcde";
//	// char str2[10] = str1; // 错误, 把str1复制给str2
//	// str2 = str1; // 错误
//
//	char str2[10];
//	strcpy(str2,str1); // 把str1的值复制给str2
//
//	printf("str2 = %s\n", str2);
//
//	return 0;
//}


//int main()
//{
//	char str1[20] = "abcde";
//	char str2[20] = "xyz";
//
//	// str1 = str1 + str2  // "abcdexyz"
//	strcat(str1, str2);
//	printf("str1 = %s\n", str1);
//
//
//	return 0;
//}


//int main()
//{
//	char str1[20] = "abcde";
//	char str2[20] = "xyz";
//	char str3[20] = "abcde";
//
//	if (strcmp(str1, str2) > 0)
//	{
//		printf("%s>%s\n", str1, str2);
//	}
//	else if (strcmp(str1, str2) == 0)
//	{
//		printf("%s=%s\n", str1, str2);
//	}
//	else
//	{
//		printf("%s<%s\n", str1, str2);
//	}
//
//
//	if (strcmp(str2, str3) > 0)
//	{
//		printf("%s>%s\n", str2, str3);
//	}
//	else if (strcmp(str2, str3) == 0)
//	{
//		printf("%s=%s\n", str2, str3);
//	}
//	else
//	{
//		printf("%s<%s\n", str2, str3);
//	}
//
//	return 0;
//}



// strlen: 求字符串长度   "abc" -> 3 (不包括'\0')
//         注意和sizeof区分
//         sizeof(a) 求a占用的字节数

//int main()
//{
//	char str[] = "abcde";
//	printf("%d\n", strlen(str));
//
//	return 0;
//}


//int main()
//{
//	char str1[10] = "abcde";
//	char str2[] = "abcde";
//	char str3[10] = "abcde\0\nf";
//	char str4[] = "abcde\0\nf";
//	printf("%d,%d\n", strlen(str1), sizeof(str1)); // 5,10
//	printf("%d,%d\n", strlen(str2), sizeof(str2)); // 5,6
//	printf("%d,%d\n", strlen(str3), sizeof(str3)); // 5,10
//	printf("%d,%d\n", strlen(str4), sizeof(str4)); // 5,9
//
//	return 0;
//}


/*
	字符串大小写转换
	strlwr 大变小    已废除
	strupr 小变大    已废除

*/


// 自己实现把字符串中的大写字符换成小写

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


// 自己实现把小写字母转换成大写



// 输入一行字符,统计其中有多少个单词,单词之间用空格分隔开


//int main()
//{
//	char str[100];
//	//scanf("%s", str); // 不能读取空格
//	fgets(str, 100, stdin);  // 从键盘最多读取不超过100个字符(可以有空格)
//	// printf("%s\n", str);
//
//	int n = 0;
//	for (int i = 0; str[i] != '\0'; i++)
//	{
//		if (isalpha(str[i]) && !isalpha(str[i + 1]))  // 当前是字母,下一个不是字母
//		{
//			n++;
//		}
//	}
//	printf("%d\n", n);
//
//	return 0;
//}



// 有三个字符串,找出最大的


//int main() {
//	char str[3][20];
//	char max[20] = "";
//	int i;
//
//	// 读取字符串并去除换行符
//	for (i = 0; i < 3; i++) {
//		fgets(str[i], 20, stdin);
//		//str[i][strlen(str[i]) - 1] = '\0'; // 去除换行符
//	}
//
//	// 比较字符串大小
//	for (i = 0; i < 3; i++) {
//		if (strcmp(max, str[i]) < 0) {
//			strcpy(max, str[i]);
//		}
//	}
//
//	printf("最大的字符串为: %s\n", max);
//
//	return 0;
//}