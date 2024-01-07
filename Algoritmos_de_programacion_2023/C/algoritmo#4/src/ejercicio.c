/*#4
¿ES UN NÚMERO PRIMO?

 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main(void)
{
    short int iterable, iterable_two, contador;
    double numero_double;
    char num[50];
    size_t len;
    // 2 3 5 7 11 13 17 19 23 29
    for (iterable = 1; iterable <= 100; iterable++)
    {
        contador = 0;
        for (iterable_two = 0; iterable_two < iterable; iterable_two++)
        {
            numero_double = (double)iterable / (double)(iterable_two + 1);
            // printf("iterable = %d / %d = %.2lf\n", iterable, iterable_two + 1, numero_double);
            sprintf(num, "%.2lf", numero_double);
            len = strlen(num);
            for (short int i = 0; i < len; i++)
            {
                if (num[i] == '.')
                {
                    if (num[i + 1] == '0' && num[i + 2] == '0')
                    {
                        contador++;
                        break;
                    }
                }
            }
        }

        if (contador > 2 || contador == 1)
        {
            printf("%d no es primo\n", iterable);
            continue;
        }
        else if (contador == 2)
        {
            printf("%d es primo\n", iterable);
            continue;
        }
    }
    return;
}