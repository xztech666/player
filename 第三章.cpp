//#define _CRT_SECURE_NO_WARNINGS  //Ԥ����,��Ϊscanf����ȫ
//#include<stdio.h>
//#include<math.h>

/*
	�����¶�ת�������¶�
*/

//int main()
//{
//	double f;
//	scanf("%lf", &f);    //��ȡdouble�����ݱ���ʹ��%lf,�״�
//	double c = 5.0 / 9 * (f - 32);
//	printf("%lf\n", c);
//
//	return 0;
//}

//int main()
//{
//	double p0 = 1000, r1 = 0.0036, r2 = 0.0225, r3 = 0.0198;
//	printf("���ڱ�Ϣ��:%.2lf\n", p0 * (1 + r1));
//	printf("һ�걾Ϣ��:%.2lf\n", p0 * (1 + r2));
//	printf("���ΰ��궨�ڱ�Ϣ��:%.2lf\n", p0 * (1 + r3 / 2) * (1 + r3 / 2));
//	//%.2lf:  ������λС��
//
//	return 0;
//}

/*
	����Խ�类����,����ԽС
*/

//#define DOUBLE(x) x + x
//
//int main()
//{
//	printf("%d\n", 2 * DOUBLE(10));  //����
//	// �궨�岻�Ǻ���, 2 * DOUBLE(10) �滻Ϊ  2 * 10 + 10 -> 30
//}

/*
	����һ����д��ĸ,���Сд��ĸ
*/

//int main()
//{
//	char ch;
//	printf("������һ����д��ĸ:\n");
//	scanf("%c", &ch);
//	if ('A' <= ch && ch <= 'Z')
//	{
//		printf("%c\n", ch + ('a' - 'A'));
//	}
//	
//	return 0;
//}

/*
	�����������(���ж����ݵĺϷ���)
*/

//int main()
//{
//	int a, b, c;
//	printf("�����������������ߵĳ���:\n");
//	scanf("%d %d %d", &a, &b, &c);
//	if (a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a)
//	{
//		double s = (a + b + c) / 2.0;   //ϸ��,���忴ǰ�����
//		double area = sqrt(s * (s - a) * (s - b) * (s - c));
//		printf("���=%lf\n", area);
//	}
//	else
//	{
//		printf("�ܱ�Ǹ,����������ݲ����Ϸ�!\n");
//	}
//	return 0;
//}

/*
	ax^2 + bx + c = 0, �󷽳̵ĸ�
*/

//int main()
//{
//	double x1, x2;
//	int a, b, c;
//	printf("������������:");
//	scanf("%d %d %d", &a, &b, &c);
//	int d = b * b - 4 * a * c;
//	if (d < 0)
//	{
//		printf("��ʵ��!");
//	}
//	else if (d > 0)
//	{
//		x1 = (-b + sqrt(d)) / (2 * a);
//		x2 = (-b - sqrt(d)) / (2 * a);
//
//		printf("����ʵ���ֱ�Ϊ: x1 = %.2lf, x2 = %.2lf\n", x1, x2);
//	}
//	else
//	{
//		double x = -b / (2 * a);
//
//		printf("ֻ��һ��ʵ��Ϊ:x = %.2lf\n", x);
//	}
//	
//	return 0;
//}

/*
	getchar  ����һ���ַ�
	putchar  ���һ���ַ�
*/

//int main()
//{
//	//char ch = getchar();  //�Ӽ��̻�ȡһ���ַ�������
//	//putchar(ch);  //���һ���ַ�����Ļ
//
//	char ch;
//	//��ȡһ���ַ�
//	while (((ch = getchar()) != '\n'))
//	{
//		putchar(ch);
//	}
//	
//	return 0;
//}