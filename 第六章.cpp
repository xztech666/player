//#define _CRT_SECURE_NO_WARNINGS  //Ԥ����,��Ϊscanf����ȫ
//#include<stdio.h>
//#include<math.h>
//#include<string.h>
//#include<ctype.h>

/*
	����: ���ͬ���͵�����
	����: ����  ������[����]
	��ʼ��: �ڶ����ͬʱ,��ֵ(��������),ֻ��ʼ��һ������ʣ�ಿ��Ϊ0
*/

//int main()
//{
//	int a = 10;  // ����һ��int���ͱ���a,���Ҵ������10
//	int arr[10]; // ����һ��int���͵��������arr,����Ϊ10
//	int brr[10] = { 1,2,3,4,5,6,7,8,9,10 }; // ��ʼ��
//	int crr[10] = { 1,2,3,4,5 }; //1,2,3,4,5,0,0,0,0,0
//	int drr[] = { 1,2,3,4,5, }; //�Զ��Ƶ�����,�պ��ܷ�������Ԫ��
//	// int crr[]; // ����,û�и�ֵ
//
//	return 0;
//}

//int main()
//{
//	int a = 10;
//	int arr[a];        // vs2022���鳤��Ϊ�����Ǵ����,c99���鳤�ȿ����Ǳ���
//  
//  int a = 4;
//  arr[a] = 100;     // ������ôʹ��
//}

/*
	���ʹ������Ԫ��?
	�±��0��ʼ
	�±�ʱ����ʹ�ñ���   �Ե�
*/

//int main()
//{
//	int arr[10] = { 1,2,3,4,5,6,7,8,9,10 };
//	arr[2] = 10;
//	int a = 4;
//	arr[a] = 100;
	// printf����ֱ�������������
	// printf("%d\n,arr");  // ����,�������arr�ĵ�ַ
//	for (int i = 0; i < 10; ++i)
//	{
//		printf("%d ", arr[i]);
//	}
//
//	return 0;
//}

// ����arr���ȹ�ʽ: sizeof(arr)/sizeof(arr[0])   arr����Ϊ�β�


// �������
//int main()
//{
//	int arr[] = { 0,1,2,3,4,5,6,7,8,9 };
//	for (int i = sizeof(arr) / sizeof(arr[0]) - 1; i >= 0; i--)  // �����õ�ʱ��--i,i--һ��
//	{
//		printf("%d ", arr[i]);
//	}
//	return 0;
//}

//  ��������������쳲�������������
// 1,1,2

//int main()
//{
//	int arr[40] = { 1,1 }; //����쳲���������ǰ40���ֵ
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

// ��ʮ�������������С��������
// ð������: ��ͷ��β�����Ƚ�,�������,С����ǰ


//int main()
//{
//	int arr[] = { 3,7,5,1,8,9,10,15,48,26,189,546 };
//	int len = sizeof(arr) / sizeof(arr[0]);
//	int tmp;
//	for (int i = 0; i < len - 1; ++i) // ѭ��������, 5����ѭ��4��
//	{
//		for (int j = 0; j + 1 < len - i; ++j) //ÿһ�˴�ͷ��β(���������������), len-i δ�������
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
	��ά����
		����: ���� ������[��][��]     ����ʽ
		��ʼ��, �ڶ����ͬʱ��ֵ
		����Ԫ��: ͨ����,���±����
*/

//int main()
//{
//	int arr[10] = { 1,2,3,4,5,6,7,8,9,10 };
//	int brr[3][4] = { {1,2,3,4},{5,6,7,8},{9,10,11,12} };
//	int brr[3][4] = { 1,2,3,4,5,6,7,8,9,10 }; // ������,�ȴ��п�ʼ,ʣ�ಿ��Ϊ0
//	int crr[][4] = { 1,2,3,4,5,6,7,8,9,10 }; // �Զ��Ƶ�
//  int drr[][] = {1,2,3,4,5,6,7,8,9};     //����
//
//	return 0;
//}


//int main()
//{
//	int brr[3][4] = { {1,2,3,4},{5,6,7,8},{9,10,11,12} };
//	brr[1][2] = 100;
//
//	for (int i = 0; i < 3; i++) // ��
//	{
//		for (int j = 0; j < 4; j++) // ��
//		{
//			printf("%d ", brr[i][j]);
//		}
//		printf("\n");
//	}
//
//	return 0;
//}

/*
	��������: ���л���  �±껥��
*/

//int main()
//{
//	int a[2][3] = { 1,2,3,4,5,6 };
//	int b[3][2];
//
//	for (int i = 0; i < 2; ++i) // ��
//	{
//		for (int j = 0; j < 3; ++j) // ��
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
 ��һ��3*4�ľ���,Ҫ���������ֵ�����Ǹ�Ԫ�ص�ֵ,�Լ������ڵ��кź��к�
*/

//int main()
//{
//	int a[3][4] = { 3,5,4,9,26,59,48,165,1,5,9,4 };
//	int max = a[0][0];
//	int row = 0; // �� row
//	int col = 0; // �� colum
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
//	printf("�������ֵ��%d,�ڵ�%d��,��%d��", max, row, col);
//
//	return 0;
//}

/*
	�ַ�����: �ǳ���Ҫ,�õĶ�,���Ķ�
	����: char ������[����];

	�ַ���: ��""�������ַ�����,������0�������ϵ��ַ�.
			ĩβ��һ�����ص�'\0'��Ϊ��β���

		��������ʽ���ַ���: ��""����
							��'\0'���ַ�����

*/

//int main()
//{
//	char str1[10]; //���峤��Ϊ10���ַ�����,û�г�ʼ��,���ֵ  ����������
//	//printf("%s\n", str1);
//
//	str1[0] = 'l';
//	str1[1] = ' ';
//	str1[2] = 'a';
//	//printf("%s", str1); // %s����ַ���, ����,str1�����ַ���
//
//	char str2[10] = { 'l',' ','a','m' }; // ��ʼ�� ֻ��ʼ����һ����,ʣ��Ϊ0
//	char str3[10] = "abcde";
//
//	//printf("%s", str2); // ���ַ���
//	//printf("%s", str3); // ���ַ���
//
//	//0�ı���
//	printf("%d,%d,%d,%d\n", false, '\0', 0, NULL);
//
//	return 0;
//}


/*
	�ַ�������ַ���
*/

//int main()
//{
//	char str1[10]; // �ַ�����,�����ַ���
//	char str2[10] = "abcde"; // �ַ�����,���ַ���
//	char str3[] = "abcde"; // �ַ�����,���ַ���,����Ϊ6
//	char str4[] = { 'a','b','c','d','e' }; // �ַ�����,�����ַ���,����Ϊ5
//	char str5[10] = { 'a','b','c','d','e' }; // �ַ�����,���ַ���,ֻ��ʼ����һ����
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
	������ַ�����,�������ַ���
*/


//int main()
//{
//	char str[] = { 'a','b','c','d','e' }; // ���ַ�����,�����ַ���
//	//printf("%s\n", str); // ����,%s����ַ���,str�����ַ���
//
//	for (int i = 0; i < sizeof(str) / sizeof(str[0]); ++i) // ��Ϊ���鴦��
//	{
//		putchar(str[i]);
//	}
//
//	return 0;
//}


/*
	�ַ��������
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
	���һ������ͼ
		1. �ַ�����

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
//		putchar('\n');  //printf("\n");    ע��putchar�����ǵ�����
//	}
//
//	return 0;
//}


/*
	���һ������ͼ
		2.�ַ���

*/


//int main()
//{
//	char c[5][6] = { "  *  "," * * ","*   *"," * * ","  *  " }; // c[5][6]  ��������ΪҪ��'\0'
//
//	for (int i = 0; i < 5; ++i) // ֻ��Ҫ�����
//	{
//		printf("%s\n", c[i]);
//	}
//
//	return 0;
//}

/*
	�ַ����������
*/

//int main()
//{
//	char c[6];
//	for (int i = 0; i < 6; ++i) // �Ӽ��̶�ȡ6���ַ�
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
	�ַ���������

	����δ����У���������һ������6��Ԫ�ص��ַ����� c��
	Ȼ����ʹ�� scanf() ������ȡ�û�������ַ�����������洢������ c �С�
	���ʹ�� printf() ���������� c �е��ַ�����ӡ������

	Ȼ������δ������һ��Ǳ�ڵ����⣺��ʹ�� %s ��ʽ������ȡ�ַ���ʱ��
	scanf() �������������ո��Ʊ�����з�ʱֹͣ��ȡ��
	����������޷���ȷ�ض�ȡ�����ո�����롣
	���⣬�� &c ���ݸ� scanf() �������������ȷ����Ϊ��
	��Ϊ������ c �Ѿ���ָ�������ָ�룬����Ҫ��ʹ�� & �������
	Ӧ��ֱ�ӽ���������Ϊ�������ݡ�

*/

//int main()
//{
//	char c[6];
//	scanf("%s", &c); // scanf("%s",c) // &c��ͬc
//	printf("%s\n", c);
//
//	return 0;
//}


/*
	�ַ���������:
		puts: ���һ���ַ���,�����Դ�һ������'\n'
		gets: ����һ���ַ���,�Ѿ����ϳ�,����ȫ,  ��fgets���
		scanf_s: ��ȡ�ַ�������������С
*/


//int main()
//{
//	char str[100] = "abcde xyz";
//	/*puts(str);*/
//	char str2[10];
//	//scanf_s("%s", str, 100); // 100���ַ���������������
//	fgets(str2, 10, stdin); // stdin:��׼����,����
//
//	puts(str2);
//	return 0;
//}


/*
	strcpy: �ַ�����ֵ(����)    strcpy(str2,str1); // ��str1��ֵ���Ƹ�str2
	strcat: �ַ�������      str1 = str1 + str2  // "abcdexyz"    ��һ���ַ������ȱ���Ҫ�㹻
							strcat(str1, str2);
	strcmp: �ַ����Ƚ�   ����ֱ���ô���,С�ں�

*/


//int main()
//{
//	int a = 10;
//	int b = a;
//
//	char str1[] = "abcde";
//	// char str2[10] = str1; // ����, ��str1���Ƹ�str2
//	// str2 = str1; // ����
//
//	char str2[10];
//	strcpy(str2,str1); // ��str1��ֵ���Ƹ�str2
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



// strlen: ���ַ�������   "abc" -> 3 (������'\0')
//         ע���sizeof����
//         sizeof(a) ��aռ�õ��ֽ���

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
	�ַ�����Сдת��
	strlwr ���С    �ѷϳ�
	strupr С���    �ѷϳ�

*/


// �Լ�ʵ�ְ��ַ����еĴ�д�ַ�����Сд

//void Mystrlwr(char str[])
//{
//	for (int i = 0; str[i] != '\0'; ++i)
//	{
//		if (isupper(str[i])) // �Ǵ�д��ĸ
//		{
//			str[i] = tolower(str[i]); // ��д��ĸת��ΪСд��ĸ
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


// �Լ�ʵ�ְ�Сд��ĸת���ɴ�д



// ����һ���ַ�,ͳ�������ж��ٸ�����,����֮���ÿո�ָ���


//int main()
//{
//	char str[100];
//	//scanf("%s", str); // ���ܶ�ȡ�ո�
//	fgets(str, 100, stdin);  // �Ӽ�������ȡ������100���ַ�(�����пո�)
//	// printf("%s\n", str);
//
//	int n = 0;
//	for (int i = 0; str[i] != '\0'; i++)
//	{
//		if (isalpha(str[i]) && !isalpha(str[i + 1]))  // ��ǰ����ĸ,��һ��������ĸ
//		{
//			n++;
//		}
//	}
//	printf("%d\n", n);
//
//	return 0;
//}



// �������ַ���,�ҳ�����


//int main() {
//	char str[3][20];
//	char max[20] = "";
//	int i;
//
//	// ��ȡ�ַ�����ȥ�����з�
//	for (i = 0; i < 3; i++) {
//		fgets(str[i], 20, stdin);
//		//str[i][strlen(str[i]) - 1] = '\0'; // ȥ�����з�
//	}
//
//	// �Ƚ��ַ�����С
//	for (i = 0; i < 3; i++) {
//		if (strcmp(max, str[i]) < 0) {
//			strcpy(max, str[i]);
//		}
//	}
//
//	printf("�����ַ���Ϊ: %s\n", max);
//
//	return 0;
//}