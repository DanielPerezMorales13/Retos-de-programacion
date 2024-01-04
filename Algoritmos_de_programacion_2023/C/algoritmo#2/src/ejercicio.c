/*#2
¿ES UN ANAGRAMA?

 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

void Borrar(void);
void Anagrama(char *palabra1, char *palabra2);
void Input(char *palabra, size_t len);
void Minusculas(char *palabra);
void DelEnter(char *palabra);
void Sort(short int *lista, size_t len);
void Comparar(short int *lista, short int *lista2, size_t len);

void Comparar(short int *lista, short int *lista2, size_t len)
{
    short int *list_temp = lista;
    short int *list_temp2 = lista2;
    short int contador = 0;
    for (short int iterable = 0; iterable < len; iterable++)
    {
        if (*list_temp == *list_temp2)
        {
            contador++;
        }
        list_temp++;
        list_temp2++;
    }

    printf("%s\n", contador == len ? "Es un anagrama" : "No es un anagrama");
    // char *message = contador == len ? "Es un anagrama" : "No es un anagrama";
    // printf("%s\n", message);
}

void Sort(short int *lista, size_t len)
{
    short int num;
    for (short int iterable = 0; iterable < len; iterable++)
    {
        for (short int iterable_two = iterable + 1; iterable_two < len; iterable_two++)
        {
            if (lista[iterable] > lista[iterable_two])
            {
                num = lista[iterable_two];
                lista[iterable_two] = lista[iterable];
                lista[iterable] = num;
            }
        }
    }
    return;
}
void Borrar(void)
{
    system("clear");
    return;
}
void Anagrama(char *palabra1, char *palabra2)
{
    size_t len = strlen(palabra1);
    size_t len2 = strlen(palabra2);
    // crear una lista dinamica con el tamaño de la palabra
    short int *lista = (short int *)malloc(len * sizeof(short int));
    short int *lista2 = (short int *)malloc(len2 * sizeof(short int));

    // crear una lista temporal para guardar los valores de la palabra en la lista original
    short int *list_temp = lista;
    short int *list_temp_two = lista2;
    for (short int iterable = 0; iterable < len; iterable++)
    {

        *list_temp = (short int)palabra1[iterable];
        list_temp++;
    }
    for (short int iterable = 0; iterable < len2; iterable++)
    {
        *list_temp_two = (short int)palabra2[iterable];
        list_temp_two++;
    }
    Sort(lista, len);
    Sort(lista2, len2);
    Comparar(lista, lista2, len);
    // 97 - 122 y 196 rango de codigo ascii el 196 es la ñ
    free(lista);
    free(lista2);
    return;
}

void DelEnter(char *palabra)
{
    size_t len = strlen(palabra);
    if (len > 0 && palabra[len - 1] == '\n')
    {
        palabra[len - 1] = '\0'; // Elimina el salto de linea \0 significa fin de cadena
    }
}

void Input(char *palabra, size_t len)
{
    fgets(palabra, len, stdin);
    return;
}

void Minusculas(char *palabra)
{
    size_t len = strlen(palabra);
    for (short int iterable = 0; iterable < len; iterable++)
    {
        palabra[iterable] = tolower(palabra[iterable]);
    }
    return;
}

void main(void)
{
    char palabra[100];
    char palabra2[100];
    printf("Palabra #1: ");
    Input(&palabra, sizeof(palabra));
    printf("\nPalabra #2: ");
    Input(&palabra2, sizeof(palabra2));
    DelEnter(&palabra);
    DelEnter(&palabra2);
    Minusculas(&palabra);
    Minusculas(&palabra2);
    Anagrama(palabra, palabra2);
    return;
}