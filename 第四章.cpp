//#define _CRT_SECURE_NO_WARNINGS  //Ԥ����,��Ϊscanf����ȫ
//#include<stdio.h>
//#include<math.h>

/*
*   ����֧
	if(���ʽ1)
	{
		����1
	}
	// ������ʽ1Ϊ��,ִ������1

	˫��֧
	if(���ʽ1)
	{
		����1x
	}
	else
	{
		����2
	}
	//������ʽ1Ϊ����ִ������1,����ִ������2

	���֦
	if(���ʽ1)
	{
		����1
	}
	else if(���ʽ2)
	{
		����2
	}
	else
	{
		����n
	}
*/

//��С�������������

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

// ����������a, b, c,Ҫ����С�����˳�����

//int main()
//{
//	double a, b, c;
//	scanf("%lf%lf%lf", &a, &b, &c);
//
//	double tmp;
//	//a��a,b����Сֵ
//	if (a > b)
//	{
//		tmp = a;
//		a = b;
//		b = tmp;
//	}
//	//a��a,c��Сֵ
//	if (a > c)
//	{
//		tmp = a;
//		a = c;
//		c = tmp;
//	}
//	//b��b,c����Сֵ
//	if (b > c)
//	{
//		tmp = b;
//		b = c;
//		c = tmp;
//	}
//
//	//a������Сֵ,b����ڶ�С,c�������ֵ
//	printf("%lf %lf %lf\n", a, b, c);
//
//	return 0;
//}

//�ֶκ���

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
	switch (���ͱ��ʽ)   char,bool,int,short,long long int,ö��
	{
		case �������ʽ1:
			����1
			break
		case �������ʽ2:
			����2
			break
		default:
			����

	}
*/

//  ���乫˾���û������������

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
//		//switch̫������
//	}
//
//}