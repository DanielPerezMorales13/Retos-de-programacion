#include <stdio.h>

int main() {
    // Operadores aritméticos
    int a = 10;
    int b = 3;
    printf("%d\n", a + b);  // Suma
    printf("%d\n", a - b);  // Resta
    printf("%d\n", a * b);  // Multiplicación
    printf("%d\n", a / b);  // División
    printf("%d\n", a % b);  // Módulo

    // Operadores de comparación
    printf("%d\n", a == b);  // Igual a
    printf("%d\n", a != b);  // No igual a
    printf("%d\n", a > b);   // Mayor que
    printf("%d\n", a < b);   // Menor que
    printf("%d\n", a >= b);  // Mayor o igual que
    printf("%d\n", a <= b);  // Menor o igual que

    // Operadores lógicos
    printf("%d\n", 1 && 0);  // AND lógico
    printf("%d\n", 1 || 0);  // OR lógico
    printf("%d\n", !1);      // NOT lógico

    // Operadores de asignación
    a = 10;  // Asignación
    a += 5;  // Suma y asignación
    a -= 2;  // Resta y asignación
    a *= 3;  // Multiplicación y asignación
    a /= 2;  // División y asignación
    a %= 3;  // Módulo y asignación

    // Operadores de bits
    a = 60;  // 60 = 0011 1100
    b = 13;  // 13 = 0000 1101
    printf("%d\n", a & b);  // AND de bits
    printf("%d\n", a | b);  // OR de bits
    printf("%d\n", a ^ b);  // XOR de bits
    printf("%d\n", ~a);     // NOT de bits
    printf("%d\n", a << 2); // Desplazamiento a la izquierda
    printf("%d\n", a >> 2); // Desplazamiento a la derecha

    return 0;
}