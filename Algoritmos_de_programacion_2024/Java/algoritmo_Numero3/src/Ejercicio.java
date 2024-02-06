
/*#03
ESTRUCTURAS DE DATOS

 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

package Algoritmos_de_programacion_2024.Java.algoritmo_Numero3.src;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.regex.Pattern;

public class Ejercicio {

    public static void agenda() {

        Scanner scanner = new Scanner(System.in);
        scanner.nextLine(); // consume newline
        int opcion;
        String telefono;
        Map<String, String> agenda = new HashMap<>();

        while (true) {
            System.out.print(borrarPantalla());
            System.out.println("\n1. Insertar contacto");
            System.out.println("2. Borrar contacto");
            System.out.println("3. Actualizar contacto");
            System.out.println("4. Buscar contacto");
            System.out.println("5. Salir");

            System.out.print("\nElige una opción: ");

            try {
                opcion = scanner.nextInt();
                scanner.nextLine(); // consume newline
            } catch (Exception e) {
                System.out.println("Ingrese un numero valido");
                // ponemos 2 scanner.nextLine() para consumir los dos newlines que quedan en el
                // buffer
                scanner.nextLine(); // consume newline
                scanner.nextLine(); // consume newline
                continue;
            }

            switch (opcion) {
                case 1:
                    System.out.print("Introduce el nombre del contacto: ");
                    String nombre = scanner.nextLine();
                    while (true) {
                        System.out.print("Introduce el número de teléfono del contacto: ");
                        telefono = scanner.nextLine();
                        // para saber si es un número de teléfono válido se puede usar el método matches
                        // de la clase Pattern
                        // que recibe una expresión regular y devuelve true si el String cumple con la
                        // expresión regular
                        // en este caso la expresión regular es "\\d+" que significa que el String debe
                        // contener solo dígitos
                        // y el método length para saber si el número de teléfono tiene más de 11
                        // dígitos
                        if (telefono.length() > 11 || telefono.length() < 11 || !Pattern.matches("\\d+", telefono)) {
                            System.out.println("Número de teléfono no válido.");
                            scanner.nextLine(); // consume newline
                        } else {
                            agenda.put(nombre.toLowerCase(), telefono);
                            System.out.println("Contacto añadido.");
                            scanner.nextLine(); // consume newline
                            break;
                        }
                    }
                    break;
                case 2:
                    // para saber si la agenda tiene contactos se puede usar el método .isEmpty()
                    // que devuelve true si la agenda está vacía y false si no lo está
                    if (agenda.isEmpty()) {
                        System.out.println("La agenda está vacía.");
                        scanner.nextLine(); // consume newline
                        break;
                    }
                    System.out.print("Introduce el nombre del contacto a borrar: ");
                    nombre = scanner.nextLine();
                    // El metodo .containsKey() devuelve true si el mapa contiene la clave
                    // especificada y false si no la contiene
                    if (agenda.containsKey(nombre.toLowerCase())) {
                        agenda.remove(nombre.toLowerCase());
                        System.out.println("Contacto borrado.");
                        scanner.nextLine(); // consume newline
                    } else {
                        System.out.println("Contacto no encontrado.");
                        scanner.nextLine(); // consume newline
                    }
                    break;
                case 3:
                    // para saber si la agenda tiene contactos se puede usar el método .isEmpty()
                    // que devuelve true si la agenda está vacía y false si no lo está
                    if (agenda.isEmpty()) {
                        System.out.println("La agenda está vacía.");
                        scanner.nextLine(); // consume newline
                        break;
                    }
                    System.out.print("Introduce el nombre del contacto a actualizar: ");
                    nombre = scanner.nextLine();
                    // El metodo .containsKey() devuelve true si el mapa contiene la clave
                    // especificada y false si no la contiene
                    if (agenda.containsKey(nombre.toLowerCase())) {
                        System.out.print("Introduce el nuevo número de teléfono del contacto: ");
                        telefono = scanner.nextLine();
                        if (telefono.length() > 11 || telefono.length() < 11 || !Pattern.matches("\\d+", telefono)) {
                            System.out.println("Número de teléfono no válido.");
                            scanner.nextLine(); // consume newline
                        } else {
                            // le volvemos a pedir los datos al usuario para actualizar el contacto
                            System.out.print("Introduce el nuevo nombre del contacto: ");
                            nombre = scanner.nextLine();
                            agenda.put(nombre.toLowerCase(), telefono);
                            System.out.println("Contacto actualizado.");
                            scanner.nextLine(); // consume newline
                        }
                    } else {
                        System.out.println("Contacto no encontrado.");
                        scanner.nextLine(); // consume newline
                    }
                    break;
                case 4:
                    // para saber si la agenda tiene contactos se puede usar el método .isEmpty()
                    // que devuelve true si la agenda está vacía y false si no lo está
                    if (agenda.isEmpty()) {
                        System.out.println("La agenda está vacía.");
                        scanner.nextLine(); // consume newline
                        break;
                    }
                    System.out.print("Introduce el nombre del contacto a buscar: ");
                    nombre = scanner.nextLine();
                    if (agenda.containsKey(nombre.toLowerCase())) {
                        System.out.println("El número de " + nombre.toLowerCase() + " es " + agenda.get(nombre.toLowerCase()));
                        scanner.nextLine(); // consume newline
                    } else {
                        System.out.println("Contacto no encontrado.");
                        scanner.nextLine(); // consume newline
                    }
                    break;
                case 5:
                    scanner.close();
                    System.out.println("Saliendo...");
                    System.exit(0);
                default:
                    System.out.println("Opción no válida.");
                    scanner.nextLine(); // consume newline
            }
        }
    }

    public static String borrarPantalla() {
        System.out.flush();
        return "\033[H\033[2J";
    }

    public static void main(String[] args) {
        // Clase ArrayList para crear listas dinámicas
        List<String> arrayList = new ArrayList<>();
        arrayList.add("Elemento 1"); // Inserción o añaadir un elemento al final de la lista
        arrayList.add(0, "Elemento 4"); // Inserción o añadir un elemento en una posición concreta
        arrayList.remove("Elemento 1"); // Borrado o eliminar un elemento por su valor

        arrayList.remove(0); // Borrado o eliminar un elemento por su posición

        arrayList.add("Elemento 3"); // Inserción

        arrayList.add("Elemento 2"); // Inserción

        arrayList.add("Elemento 1"); // Inserción
        Collections.sort(arrayList); // Ordenación ascendente

        Collections.sort(arrayList, Collections.reverseOrder()); // Ordenación descendente
        System.out.println("arrayList String = " + arrayList);

        List<Integer> arrayList1 = new ArrayList<>();
        arrayList1.add(0); // Inserción o añadir un elemento al final de la lista

        arrayList1.add(0, 4); // añadir un elemento en una posición concreta

        arrayList1.remove(0); // Borrado o eliminar un elemento por su valor

        arrayList1.remove(0); // Borrado o eliminar un elemento por su posición

        arrayList1.add(1); // Inserción
        arrayList1.add(5); // Inserción
        arrayList1.add(2); // Inserción
        Collections.sort(arrayList1); // Ordenación ascendente

        Collections.sort(arrayList1, Collections.reverseOrder()); // Ordenación descendente
        System.out.println("arrayList Integer = " + arrayList1);

        // ArrayList of ArrayLists
        List<List<String>> arrayList2 = new ArrayList<>();
        arrayList2.add(new ArrayList<>());
        arrayList2.get(0).add("Elemento 1");
        arrayList2.get(0).remove("Elemento 1");
        arrayList2.get(0).add("Elemento 2");
        arrayList2.get(0).add(0, "Elemento 4");
        Collections.sort(arrayList2.get(0));
        System.out.println("arrayList Bidimensional = " + arrayList2);

        // LinkedList
        List<String> linkedList = new LinkedList<>();
        linkedList.add("Elemento 1");
        linkedList.remove("Elemento 1");
        // linkedList.remove(0); // This would cause an IndexOutOfBoundsException
        // because the list is empty at this point
        linkedList.add("Elemento 2");
        linkedList.add(0, "Elemento 4");
        Collections.sort(linkedList);
        System.out.println("linkedList = " + linkedList);

        // HashSet
        Set<String> hashSet = new HashSet<>();
        hashSet.add("Elemento 1");
        hashSet.remove("Elemento 1");
        hashSet.add("Elemento 2");
        System.out.println("hashSet = " + hashSet);

        // LinkedHashSet
        Set<String> linkedHashSet = new LinkedHashSet<>();
        linkedHashSet.add("Elemento 1");
        linkedHashSet.remove("Elemento 1");
        linkedHashSet.add("Elemento 2");
        System.out.println("linkedHashSet = " + linkedHashSet);

        // TreeSet
        Set<String> treeSet = new TreeSet<>();
        treeSet.add("Elemento 1");
        treeSet.remove("Elemento 1");
        treeSet.add("Elemento 2");
        System.out.println("treeSet = " + treeSet);

        // HashMap
        Map<String, String> hashMap = new HashMap<>();
        hashMap.put("Clave 1", "Valor 1");
        hashMap.remove("Clave 1");
        hashMap.put("Clave 2", "Valor 2");
        System.out.println("hashMap = " + hashMap);

        // LinkedHashMap
        Map<String, String> linkedHashMap = new LinkedHashMap<>();
        linkedHashMap.put("Clave 1", "Valor 1");
        linkedHashMap.remove("Clave 1");
        linkedHashMap.put("Clave 2", "Valor 2");
        System.out.println("linkedHashMap = " + linkedHashMap);

        // TreeMap
        Map<String, String> treeMap = new TreeMap<>();
        treeMap.put("Clave 1", "Valor 1");
        treeMap.remove("Clave 1");
        treeMap.put("Clave 2", "Valor 2");
        System.out.println("treeMap = " + treeMap);
        agenda();
    }
}
