// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int age;
    float salary;
    char name[10];
    printf("how old are you \n");
    scanf("%d", &age);
    printf("what is your name \n");
    scanf("%s", name);
    printf("how much do you get\n");
    scanf("%f",&salary);
    
    printf("%s you are %d years old,  with %f Rwf",name,age,salary);
    
}