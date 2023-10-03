#include <stdio.h>

int fibonacci(int n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main() {
    int n, i;
    printf("Ingrese la cantidad de números de Fibonacci que desea mostrar: ");
    scanf("%d", &n);

    printf("Los primeros %d números de Fibonacci son: ", n);
    for (i = 0; i < n; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");

    return 0;
}