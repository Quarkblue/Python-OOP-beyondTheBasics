#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    const int n,q;
    scanf("%d",&n);
    char *names = (char*) malloc(n * 12 * sizeof(char));
    char *qNames = (char*) malloc(q * 12 * sizeof(char));

    for(int i = 0; i <= n; i++){
        gets(names);
    }
    for (int i = 0; i <= q; i++){
        gets(qNames);
    }

    

    return 0;
}
