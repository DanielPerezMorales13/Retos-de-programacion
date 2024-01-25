/*
# 5
ÁREA DE UN POLÍGONO

* Crea una única función (importante que sólo sea una) que sea capaz
* de calcular y retornar el área de un polígono.
* - La función recibirá por parámetro sólo UN polígono a la vez.
* - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
* - Imprime el cálculo del área de un polígono de cada tipo.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void borrar()
{
    system("clear");
}

/*

*    Área de un triángulo:
*    La fórmula general es Área = (base * altura) / 2.
*
*    Área de un cuadrado:
*    La fórmula es Área = lado * lado.
*
*    Área de un rectángulo:
*    La fórmula es Área = longitud * ancho.

*/

short int Validacion_Numero_Int();
double Validacion_Numero_Float();

double Validacion_Numero_Float()
{
    short int contador = 0;
    char opcion[100];
    char caracteres_validos[] = "0123456789.";

    fgets(opcion, sizeof(opcion), stdin);
    for (short int iterable = 0; iterable < strlen(opcion); iterable++)
    {

        for (short int iterable_two = 0; iterable_two < strlen(caracteres_validos); iterable_two++)
        {
            if (opcion[iterable] == caracteres_validos[iterable_two])
            {
                contador++; // Si encuentra un numero en la cadena de caracteres, se suma 1 al contador
                break;      // Si encuentra un numero en la cadena de caracteres, se sale del bucle y continua con la siguiente iteracion
            }
            else
            {
                // Si no encuentra un numero en la cadena de caracteres, se continua con la siguiente iteracion
                continue;
            }
        }
    }
    if (contador == strlen(opcion) - 1)
    {
        return atof(opcion);
    }
    else
    {
        return 0.0; // Si retorna 0 es porque no es un numero
    }
}

short int Validacion_Numero_Int()
{
    short int contador = 0;
    char opcion[100], caracteres_validos[] = "0123456789";

    fgets(opcion, sizeof(opcion), stdin);
    for (short int iterable = 0; iterable < strlen(opcion); iterable++)
    {
        for (short int iterable_two = 0; iterable_two < strlen(caracteres_validos); iterable_two++)
        {
            if (opcion[iterable] == caracteres_validos[iterable_two])
            {

                contador++; // Si encuentra un numero en la cadena de caracteres, se suma 1 al contador
                break;      // Si encuentra un numero en la cadena de caracteres, se sale del bucle y continua con la siguiente iteracion
            }
            else
            {
                // Si no encuentra un numero en la cadena de caracteres, se continua con la siguiente iteracion
                continue;
            }
        }
    }
    if (contador == strlen(opcion) - 1)
    {

        return atoi(opcion);
    }
    else
    {
        return 0.0; // Si retorna 0 es porque no es un numero
    }
}
char *funcion()
{
    char poligono[100];
    short int opcion;
    double base = 0.0, altura = 0.0, lado = 0.0, longitud = 0.0, ancho = 0.0;
    while (1)
    {
        borrar();
        puts("Que poligono deseas calcular?");
        puts("1. Triangulo");
        puts("2. Cuadrado");
        puts("3. Rectangulo");
        // %hd para short int
        opcion = Validacion_Numero_Int();

        switch (opcion)
        {
        case 1:
            while (!base)
            {
                borrar();
                printf("Ingresa la base del triangulo tiene que se mayor a 0\n");
                // if (scanf("%lf", &base) == 1 && base >= 1.0)
                base = Validacion_Numero_Float();
                if (base >= 1.0)
                {
                    // La expresión scanf("%lf", &base) == 1 verifica si la función scanf ha leído con éxito un valor.

                    /*
                     * Si scanf no puede leer un número (por ejemplo, si el usuario introduce una letra en lugar de un número), no puede almacenar ningún valor en base y devuelve 0. En este caso, scanf("%lf", &base) == 1 es falso.
                     */
                    break;
                }
                else
                {
                    while (getchar() != '\n')
                        ;
                    /*
                    * La línea while (getchar() != '\n'); es un bucle que continúa leyendo caracteres de la entrada estándar hasta que encuentra un carácter de nueva línea ('\n'). Esto se utiliza a menudo para "limpiar" el buffer de entrada después de una operación de lectura que no consume toda la línea de entrada.

                    * Cuando el usuario ingresa algo en la consola y presiona Enter, todo lo que se ingresa, incluyendo el carácter de nueva línea que se genera cuando se presiona Enter, se coloca en el buffer de entrada. Si una operación de lectura como scanf no consume toda la línea de entrada, los caracteres no consumidos permanecen en el buffer de entrada y pueden interferir con la próxima operación de lectura.
                    */
                    puts("opcion no valida");
                    getchar();
                    continue;
                }
            }
            while (!altura)
            {
                borrar();
                printf("Ingresa la altura del triangulo tiene que se mayor a 0\n");
                // if (scanf("%lf", &altura) == 1 && altura >= 1.0)

                altura = Validacion_Numero_Float();
                if (altura >= 1.0)
                {
                    sprintf(poligono, "El area del poligono triangulo es: %.2lf", (base * altura) / 2);
                    return strdup(poligono);
                }
                else
                {
                    while (getchar() != '\n')
                        ;
                    // limpiar el buffer de entrada
                    puts("opcion no valida");
                    continue;
                }
            }

        case 2:
        {
            while (!lado)
            {
                borrar();
                printf("Ingresa el lado del cuadrado tiene que se mayor a 0\n");
                // if (scanf("%lf", &lado) == 1 && lado >= 1.0)
                lado = Validacion_Numero_Float();
                if (lado >= 1.0)
                {
                    // La expresión scanf("%lf", &lado) == 1 verifica si la función scanf ha leído con éxito un valor.

                    /*
                     * Si scanf no puede leer un número (por ejemplo, si el usuario introduce una letra en lugar de un número), no puede almacenar ningún valor en lado y devuelve 0. En este caso, scanf("%lf", &lado) == 1 es falso.
                     */
                    sprintf(poligono, "El area del poligono cuadrado es: %.2lf", lado * lado);
                    return strdup(poligono);
                }
                else
                {
                    while (getchar() != '\n')
                        ;
                    /*
                    * La línea while (getchar() != '\n'); es un bucle que continúa leyendo caracteres de la entrada estándar hasta que encuentra un carácter de nueva línea ('\n'). Esto se utiliza a menudo para "limpiar" el buffer de entrada después de una operación de lectura que no consume toda la línea de entrada.

                    * Cuando el usuario ingresa algo en la consola y presiona Enter, todo lo que se ingresa, incluyendo el carácter de nueva línea que se genera cuando se presiona Enter, se coloca en el buffer de entrada. Si una operación de lectura como scanf no consume toda la línea de entrada, los caracteres no consumidos permanecen en el buffer de entrada y pueden interferir con la próxima operación de lectura.
                    */
                    puts("opcion no valida");
                    getchar();
                    continue;
                }
            }
        }

        case 3:
        {
            while (!longitud)
            {
                borrar();
                printf("Ingresa la longitud del rectángulo tiene que se mayor a 0\n");
                // if (scanf("%lf", &longitud) == 1 && longitud >= 1.0)
                longitud = Validacion_Numero_Float();
                if (longitud >= 1.0)

                {
                    // La expresión scanf("%lf", &longitud) == 1 verifica si la función scanf ha leído con éxito un valor.

                    /*
                     * Si scanf no puede leer un número (por ejemplo, si el usuario introduce una letra en lugar de un número), no puede almacenar ningún valor en longitud y devuelve 0. En este caso, scanf("%lf", &longitud) == 1 es falso.
                     */
                    break;
                }
                else
                {
                    while (getchar() != '\n')
                        ;
                    /*
                    * La línea while (getchar() != '\n'); es un bucle que continúa leyendo caracteres de la entrada estándar hasta que encuentra un carácter de nueva línea ('\n'). Esto se utiliza a menudo para "limpiar" el buffer de entrada después de una operación de lectura que no consume toda la línea de entrada.

                    * Cuando el usuario ingresa algo en la consola y presiona Enter, todo lo que se ingresa, incluyendo el carácter de nueva línea que se genera cuando se presiona Enter, se coloca en el buffer de entrada. Si una operación de lectura como scanf no consume toda la línea de entrada, los caracteres no consumidos permanecen en el buffer de entrada y pueden interferir con la próxima operación de lectura.
                    */
                    puts("opcion no valida");
                    getchar();
                    continue;
                }
            }
            while (!ancho)
            {
                borrar();
                printf("Ingresa la altura del triangulo tiene que se mayor a 0\n");

                // if (scanf("%lf", &ancho) == 1 && ancho >= 1.0)
                ancho = Validacion_Numero_Float();
                if (ancho >= 1.0)
                {
                    sprintf(poligono, "El area del poligono del rectángulo es: %.2lf", longitud * ancho);
                    return strdup(poligono);
                }
                else
                {
                    while (getchar() != '\n')
                        ;
                    // limpiar el buffer de entrada
                    puts("opcion no valida");
                    getchar();
                    continue;
                }
            }
        }

        default:
        {
            while (getchar() != '\n')
                ;
            puts("Opcion no valida");
            getchar();
            continue;
        }
        }
    }
}

int main()
{
    borrar();
    char *resultado = funcion();
    printf("El resultado es: %s\n", resultado);
    return 0;
    /*
    Sí, existen varias maneras de formatear un número double en C utilizando la función printf(). Aquí te dejo algunos ejemplos:

    %.2lf: Imprime el número con dos dígitos después del punto decimal.
    ejemplos de printf con double en c

    printf("%lf", 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);
    Imprime "3.141593"

    printf("%.2lf", 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);
    Imprime "3.14"

    %10.2lf: Imprime el número con dos dígitos después del punto decimal y al menos 10 caracteres de ancho. Si el número es más corto, se añaden espacios en blanco al principio.

    Ejemplo:
    printf("%10.2lf", 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);
    Imprime "      3.14"

    %-10.2lf: Similar al anterior, pero los espacios en blanco se añaden al final si el número es más corto.
    Ejemplo:
    printf("%-10.2lf", 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);
    Imprime "3.14      "

    %e o %E: Imprime el número en notación científica.
    Ejemplo:

    printf("%E", 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);
    Imprime "3.141593E+00"

    printf("%e", 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);
    Imprime "3.141593e+00"

    %10.2e: Imprime el número en notación científica con dos dígitos después del punto decimal y al menos 10 caracteres de ancho. Si el número es más corto, se añaden espacios en blanco al principio.
    Ejemplo:
    printf("%10.2e", 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);
    Imprime "  3.14e+00"

    %-10.2e: Similar al anterior, pero los espacios en blanco se añaden al final si el número es más corto.
    Ejemplo:
    printf("%-10.2e", 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);
    Imprime "3.14e+00  "


    %f: Imprime el número en formato normal.

    Ejemplo:
    printf("%f", 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);
    Imprime "3.141593"

    %g o %G: Imprime el número en formato normal o en notación científica, dependiendo de su valor.

    Ejemplo:
    printf("%g", 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);
    Imprime "3.14159"

    printf("%G", 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);
    Imprime "3.14159"

    Además, puedes usar la función sprintf() para formatear un número double y almacenarlo en una cadena. Esto puede ser útil si necesitas manipular el número formateado como una cadena en lugar de imprimirlo directamente.

    Ejemplo:
    char buffer[100];
    sprintf(buffer, "%lf", 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);
    printf("%s", buffer);
    */
}
