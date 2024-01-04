/*#3
LA SUCESIÓN DE FIBONACCI

 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void borrar(void);
void Fibonacci(void);
void borrar(void)
{
    system("clear");
    return;
}
void Fibonacci(void)
{
    unsigned long long int num1 = 0;
    unsigned long long int num2 = 1;
    while (1)
    {
        printf("%llu\n", num1);
        printf("%llu\n", num2);
        num1 += num2;
        num2 += num1;
        if (num2 > 6)
        {
            break;
        }
    }
    return;
}
void main(void)
{
    Fibonacci();
    return;
}