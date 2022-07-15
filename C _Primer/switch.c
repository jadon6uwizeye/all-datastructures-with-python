// // Online C compiler to run C program online
// #include <stdio.h>
// int main() {
//     int a,b,ans;
//     char op;
//     printf("Enter first value\n");
//     scanf("%d",&a);
//     printf("Enter second value\n");
//     scanf("%d",&b);
//     printf("what doyou want to perfom: +,-,*\n");
//     scanf("%c",&op);
//     switch(op){ 
//         case'+':
//         ans=a+b;
//     printf("%d+%d=%d",a,b,ans);
//     break;
//     case'-':
//     ans=a-b;
//     printf("%d-%d=%d",a,b,ans);
//     break;
//     case'*':ans=a*b;
//     printf("%d*%d=%d",a,b,ans);
//     }
//     return 0;
    
    
    
    
//     return 0;
// }




#include<stdio.h>
int main()
{
	
	char l;
	printf("Enter any character");
	 scanf("%c",&l);
	 switch(l){
	 	case 'a':
	 		 	printf("it is a vowel");
	 	break;
	 	case 'e':
	 	 	printf("it is a vowel");
	 	break;
	 	case 'i':
	 		 	printf("it is a vowel");
	 	break;
	 	case 'u':
	 	printf("it is a vowel");
	 	break;
	 	default:
	 		printf("The character you chosed is not a vowel!");
	 }
	 return 0;
}