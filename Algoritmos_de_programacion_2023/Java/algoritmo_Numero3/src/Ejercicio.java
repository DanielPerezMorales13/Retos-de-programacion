/* #3
    LA SUCESIÓN DE FIBONACCI

* Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
package Algoritmos_de_programacion_2023.Java.algoritmo_Numero3.src;

public class Ejercicio {
    public void Fibonacci() {
        int num1 = 0;
        int num2 = 1;
        while (true) {
            System.out.println(num1);
            System.out.println(num2);
            num1 += num2;
            num2 += num1;
            if (num2 > 10) {
                break;
            }
        }

    }

    public static void main(String[] args) {
        Ejercicio ejercicio = new Ejercicio();
        ejercicio.Fibonacci();

    }
}