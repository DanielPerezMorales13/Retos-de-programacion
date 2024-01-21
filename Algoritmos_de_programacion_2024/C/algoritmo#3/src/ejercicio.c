#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define VARIABLE_GLOBAL 10

short int funcion()
{
    short int variable_local = 10;
    variable_local += VARIABLE_GLOBAL;
    return variable_local;
}

void funcion_con_parametros_sin_retorno(short int parametro1, short int parametro2)
{
    short int variable_local = 10;
    variable_local += parametro1 + parametro2;
}

short int funcion_con_parametros_con_retorno(short int parametro1, short int parametro2)
{
    short int variable_local = 10;
    variable_local += parametro1 + parametro2;
    return variable_local;
}

short int funcion_sin_parametros_con_retorno()
{
    short int variable_local = 10;
    return variable_local;
}

void funcion_sin_parametros_ni_retorno()
{
    short int variable_local = 10;
}

short int main(void)
{
    short int variable = funcion();
    printf("%d\n", variable);
    return 0;
}