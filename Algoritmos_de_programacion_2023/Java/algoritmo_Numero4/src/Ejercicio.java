/*
#4
¿ES UN NÚMERO PRIMO?

 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
*/

package Algoritmos_de_programacion_2023.Java.algoritmo_Numero4.src;

public class Ejercicio {
    public static Boolean EsPrimo(int numero) {
        String str = "";
        int contador = 0, index;
        for (Integer i = 1; i <= 100; i++) {
            str = String.valueOf((double) numero / (double) i);
            // En Java tambien se pueden sumar strings
            str += "0";
            index = str.indexOf(".");
            // En Java para acceder al indice de un string se usa el metodo indexOf
            if (str.charAt(index + 1) == '0' && str.charAt(index + 2) == '0') {
                contador++;
            } else {
                continue;
            }

        }
        if (contador == 1 || contador > 2) {
            return false;
        } else if (contador == 2) {
            return true;
        }
        // En Java es obligatorio retornar un valor en todos los casos
        return false;
    }

    public static void main(String[] args) {
        // En Java Integer es un objeto que representa un numero entero
        // y int es un tipo de dato primitivo que representa un numero entero
        // En Java los tipos de datos primitivos no son objetos
        for (Integer i = 1; i <= 100; i++) {
            // Ternario en Java
            // condicion ? valorSiVerdadero : valorSiFalso
            System.out.println(i + (EsPrimo(i) ? " = Es Primo" : " = No es Primo"));

        }
    }
}