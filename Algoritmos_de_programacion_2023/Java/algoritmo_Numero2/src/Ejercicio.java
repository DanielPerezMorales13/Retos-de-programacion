/*#2
¿ES UN ANAGRAMA?

 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
package Algoritmos_de_programacion_2023.Java.algoritmo_Numero2.src;

import java.util.Arrays;
import java.util.Scanner;

public class Ejercicio {
    public static Boolean EsAnagrama(String palabra1, String palabra2) {
        char caracteres[] = palabra1.toCharArray();
        // el metodo toCharArray() convierte un String en un array de caracteres
        Arrays.sort(caracteres);
        // el metodo sort() ordena los elementos de un array

        char caracteres2[] = palabra2.toCharArray();
        Arrays.sort(caracteres2);
        caracteres = String.valueOf(caracteres).toLowerCase().toCharArray();
        caracteres2 = String.valueOf(caracteres2).toLowerCase().toCharArray();
        if (Arrays.equals(caracteres, caracteres2)) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String palabra1, palabra2;
        System.out.print("Ingrese la primera palabra: ");
        palabra1 = scanner.nextLine();
        System.out.print("Ingrese la segunda palabra: ");
        palabra2 = scanner.nextLine();
        scanner.close();
        Boolean anagrama = EsAnagrama(palabra1, palabra2);
        System.out.println("¿Es un anagrama? " + anagrama);

    }
}