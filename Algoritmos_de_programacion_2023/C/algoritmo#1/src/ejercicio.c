/*  #1
    EL FAMOSO "FIZZ BUZZ"

 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

#include <stdio.h>
#define FIZZ "fizz"
#define BUZZ "buzz"
#define FIZZBUZZ "fizzbuzz"

void main(void)
{
    short i;
    for (i=0;i<=100;i++)
    {
        if (i % 3 == 0 && i % 5 == 0)
        {
            printf("%d %s\n",i, FIZZBUZZ);
        }
        else if (i % 3 == 0)
        {
            printf("%d %s\n", i,FIZZ);
        }
        else if (i % 5 == 0)
        {
            printf("%d %s\n", i,BUZZ);
        }
        else
        {
            printf("%d\n", i);
        }
    }
    return;
}