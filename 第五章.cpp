//#define _CRT_SECURE_NO_WARNINGS  //Ԥ����,��Ϊscanf����ȫ
//#include<stdio.h>
//#include<math.h>

/*
	ѭ��: for,while,do while,break,continue

	for(���ʽ1; ���ʽ2; ���ʽ3)
	{
		����1
	}
	���ʽ1: ѭ�����ӳ�ʼ��,���类ִ��,����ֻ��һ��
	���ʽ2: �ж�,Ϊ��ѭ������,Ϊ��ѭ������
	���ʽ3: ����,�޸�ѭ�����ӵ�ֵ,ע������������1֮��ִ��
	���ʽ����ʡ����?
		����,���ǷֺŲ���ʡ��
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

//  ��1+2+3+...+100�ĺ�

//int main()
//{
//	int sum = 0;
//	for (int i = 1; i <= 100; i++)
//	{
//		sum += i;
//	}
//	printf("�ܺ���:%d\n", sum);
//
//	return 0;
//}

/*
	while(���ʽ1)
	{
		����1
	}
	���ʽ1 ���Ϊ��,ѭ������,Ϊ��ѭ������,����ʡ��
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
		����1
	}
	while(���ʽ1);

	���ʽ1���Ϊ��,ѭ������.Ϊ��ѭ������,����ʡ��

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
	do while ʵ��1+2+3+4+...+100
*/

//int main()
//{
//	int sum = 0;  // �ܺͳ�ʼ��
//	int i = 1;  // ѭ������
//	do
//	{
//		sum += i;
//		i++;
//	} while (i <= 100);
//	printf("�ܺ�Ϊ:%d\n", sum);
//
//	return 0;
//}

/*
	break: ������ǰѭ��(һ��)
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
//	printf("����=%d,ƽ������=%.2lf\n", i, (double)sum / i);
//
//	return 0;
//}

/*
	continue: ��ǰ��������ѭ��,ֱ�ӽ�����һ��ѭ��
*/

// ���100-200֮��Ĳ��ܱ�3��������

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

// ���4*5�ľ���
// printf("%-3d ", i * j);// ÿ������ռ����,�����

//int main()
//{
//	for (int i = 1; i <= 4; i++)// ��
//	{
//		for (int j = 1; j <= 5; j++)// ��
//		{
//			printf("%-3d ", i * j);// ÿ������ռ����,�����
//		}
//		printf("\n");
//	}
//
//	return 0;
//}

/*
	�󦰵Ľ���ֵ
*/

//int main()
//{
//	double sum = 0;
//	int flg = 1; // ����
//
//	//1/1000001
//	for (int i = 1; i < 1000000; i += 2) // 10^-6����, 1e-6
//	{
//		sum += flg * 1.0 / i; // һ��Ҫע��������������
//		flg *= -1;
//	}
//	printf("pi=%lf\n", sum * 4);
//
//	return 0;
//}

/*
	��쳲��������е�ǰ��ʮ����
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