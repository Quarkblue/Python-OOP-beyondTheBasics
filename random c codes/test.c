#include<stdio.h>
#include<conio.h>
#include<stdbool.h>
#include<string.h>

struct student
{
   int roll_no;
   char fname[50];
   char lname[50];
}s1,s2,s3,s4,s5;

void main(){
   
   struct student ar[5] = {s1,s2,s3,s4,s5};

   for(int i=0;i<5;i++){
      printf("%d\n",i);
      printf("roll num: ");
      scanf("%d",&ar[i].roll_no);
      printf("fname: ");
      gets(ar[i].fname);
      printf("lname");
      gets(ar[i].lname);
   }
   
}
   
   
