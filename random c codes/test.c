#include <stdio.h>

int main(){

   int n;
   scanf("%d", &n);

   int fact,i;
   fact=1;

   for(i=1;i<=n;i++){
      fact=fact*i;
   }
   printf("%d",fact);

}