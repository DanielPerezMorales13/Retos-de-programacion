package Algoritmos_de_programacion_2023.Java.algoritmo_Numero1.src;

/*  #1
    EL FAMOSO "FIZZ BUZZ"

 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
public class ejercicio 
{
    public static void main(String[] args) 
    {
        final String FIZZ = "fizz";
        final String BUZZ = "BUZZ";
        final String FIZZBUZZ = "fizzbuzz";
        for (short i = 0; i <= 100; i++) 
        {
            if (i % 3 == 0 && i % 5 == 0) 
            {
                System.out.println(i + " " + FIZZBUZZ);
            } else if (i % 3 == 0) 
            {
                System.out.println(i + " " + FIZZ);

            }
            else if (i % 5 == 0)
            {
                System.out.println(i + " " + BUZZ);
            }
            else
            {
                System.out.println(i);
            }
        }
    }
}
