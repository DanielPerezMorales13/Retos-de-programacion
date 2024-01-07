/*#01
OPERADORES Y ESTRUCTURAS DE CONTROL

 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

package Algoritmos_de_programacion_2024.Java.algoritmo_Numero2.src;

public class Ejercicio {
    public static void main(String[] args) {
        // Operadores aritméticos
        int a = 10;
        int b = 3;
        System.out.println(a + b); // Suma
        System.out.println(a - b); // Resta
        System.out.println(a * b); // Multiplicación
        System.out.println(a / b); // División
        System.out.println(a % b); // Módulo

        // Operadores de comparación
        System.out.println(a == b); // Igual a
        System.out.println(a != b); // No igual a
        System.out.println(a > b); // Mayor que
        System.out.println(a < b); // Menor que
        System.out.println(a >= b); // Mayor o igual que
        System.out.println(a <= b); // Menor o igual que

        // Operadores lógicos
        System.out.println(true && false); // AND lógico
        System.out.println(true || false); // OR lógico
        System.out.println(!true); // NOT lógico

        // Operadores de asignación
        a = 10; // Asignación
        a += 5; // Suma y asignación
        a -= 2; // Resta y asignación
        a *= 3; // Multiplicación y asignación
        a /= 2; // División y asignación
        a %= 3; // Módulo y asignación

        // Operadores de identidad
        // En Java, la igualdad de objetos se verifica con equals()
        String str1 = new String("Hello");
        String str2 = new String("Hello");
        System.out.println(str1.equals(str2)); // Devuelve true

        // Operadores de bits
        a = 60; // 60 = 0011 1100
        b = 13; // 13 = 0000 1101
        System.out.println(a & b); // AND de bits
        System.out.println(a | b); // OR de bits
        System.out.println(a ^ b); // XOR de bits
        System.out.println(~a); // NOT de bits
        System.out.println(a << 2); // Desplazamiento a la izquierda
        System.out.println(a >> 2); // Desplazamiento a la derecha

    }
}
