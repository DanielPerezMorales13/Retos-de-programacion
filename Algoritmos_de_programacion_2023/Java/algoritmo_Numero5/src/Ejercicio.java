package Algoritmos_de_programacion_2023.Java.algoritmo_Numero5.src;

import java.util.Scanner;

/*
# 5
ÁREA DE UN POLÍGONO

* Crea una única función (importante que sólo sea una) que sea capaz
* de calcular y retornar el área de un polígono.
* - La función recibirá por parámetro sólo UN polígono a la vez.
* - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
* - Imprime el cálculo del área de un polígono de cada tipo.
*/

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
public class Ejercicio {

    public static void borrar() {
        System.out.println("Ingrese un numero valido");
        System.out.print("\033[H\033[2J");
        System.out.flush();
        /*
         * Este código imprime el carácter de escape \033[H que mueve el cursor al
         * inicio de la pantalla y el carácter de escape \033[2J que limpia la pantalla
         * desde el cursor hasta el final. Luego, System.out.flush() asegura que los
         * caracteres de escape se envíen a la terminal inmediatamente.
         */

        /*
         * \033[H: Este es un código de escape CSI (Control Sequence Introducer). El [H
         * es un comando que mueve el cursor a la posición de inicio (esquina superior
         * izquierda de la terminal).
         * 
         * \033[2J: Este es otro código de escape CSI. El [2J es un comando que borra la
         * pantalla desde el cursor hasta el final de la pantalla.
         * 
         * Link de informacion(https://en.wikipedia.org/wiki/ANSI_escape_code)
         */

        return;
    }

    public static String funcion() {
        Scanner scanner = new Scanner(System.in);
        Double base, altura, lado, longitud, ancho;
        int opcion;

        while (true) {
            while (true) {
                try {
                    System.out.println("Que poligono desea calcular su area?");
                    System.out.println("1. Triangulo");
                    System.out.println("2. Cuadrado");
                    System.out.println("3. Rectangulo");
                    opcion = Integer.parseInt(System.console().readLine());
                    if (opcion >= 1) {
                        break;
                    } else {
                        continue;
                    }

                } catch (NumberFormatException e) {
                    System.out.println("Ingrese una opcion valida");
                    scanner.nextLine();
                    borrar();
                    continue;
                }
            }
            switch (opcion) {
                case 1:
                    while (true) {
                        try {
                            System.out.println("Ingrese la base del triangulo");
                            base = Double.parseDouble(System.console().readLine());
                            if (base >= 1.0) {
                                break;
                            } else {
                                continue;
                            }

                        } catch (NumberFormatException e) {
                            System.out.println("Ingrese un numero valido");
                            scanner.nextLine();
                            borrar();
                            continue;
                        }
                    }
                    while (true) {
                        try {
                            System.out.println("Ingrese la altura del triangulo");
                            altura = Double.parseDouble(System.console().readLine());
                            if (altura >= 1.0) {
                                break;
                            } else {
                                continue;
                            }
                        } catch (NumberFormatException e) {
                            System.out.println("Ingrese un numero valido");
                            scanner.nextLine();
                            borrar();
                            continue;
                        }
                    }

                    scanner.close();
                    return "La area del triangulo es " + String.valueOf((base * altura) / 2);

                case 2:
                    while (true) {
                        try {
                            System.out.println("Ingrese el lado del cuadrado");
                            lado = Double.parseDouble(System.console().readLine());
                            if (lado >= 1) {
                                break;
                            } else {
                                continue;
                            }

                        } catch (NumberFormatException e) {
                            System.out.println("Ingrese un numero valido");
                            scanner.nextLine();
                            borrar();
                            continue;
                        }
                    }
                    scanner.close();
                    return "La area del cuadrado es " + String.valueOf((lado * lado));
                case 3:
                    while (true) {
                        try {
                            System.out.println("Ingrese la longitud del rectangulo");
                            longitud = Double.parseDouble(System.console().readLine());
                            if (longitud >= 1.0) {
                                break;
                            } else {
                                continue;
                            }

                        } catch (NumberFormatException e) {
                            System.out.println("Ingrese un numero valido");
                            scanner.nextLine();
                            borrar();
                            continue;
                        }
                    }
                    while (true) {
                        try {
                            System.out.println("Ingrese la ancho del rectangulo");
                            ancho = Double.parseDouble(System.console().readLine());
                            if (ancho >= 1.0) {
                                break;
                            } else {
                                continue;
                            }
                        } catch (NumberFormatException e) {
                            System.out.println("Ingrese un numero valido");
                            scanner.nextLine();
                            borrar();
                            continue;
                        }
                    }
                    scanner.close();
                    return "La area del rectangulo es " + String.valueOf((longitud * ancho));
                default:
                    break;

            }

        }
        /*
         * Puedes tener varios bloques catch para manejar diferentes tipos de
         * excepciones. También puedes tener un bloque catch que maneje todas las
         * excepciones
         * try {
         * Código que puede lanzar una excepción
         * } catch (ArithmeticException e) {
         * Manejar excepción ArithmeticException
         * } catch (NullPointerException e) {
         * Manejar excepción NullPointerException
         * } catch (Exception e) {
         * Manejar todas las demás excepciones
         * }
         */

        // Para que sirve Integer.parseInt(System.console().readLine())

    }

    public static void main(String[] args) {
        borrar();
        String resultado = funcion();
        System.out.println(resultado);
    }
}

/*
 * 
 * boolean
 * Clase Envolvente: Boolean
 * Valor Predeterminado (Primitivo): false
 * Valor Predeterminado (Objeto): null
 * 
 * 
 * byte
 * Clase Envolvente: Byte
 * Valor Predeterminado (Primitivo): 0
 * Valor Predeterminado (Objeto): null
 * 
 * 
 * short
 * Clase Envolvente: Short
 * Valor Predeterminado (Primitivo): 0
 * Valor Predeterminado (Objeto): null
 * 
 * 
 * int
 * Clase Envolvente: Integer
 * Valor Predeterminado (Primitivo): 0
 * Valor Predeterminado (Objeto): null
 * 
 * 
 * long
 * Clase Envolvente: Long
 * Valor Predeterminado (Primitivo): 0L
 * Valor Predeterminado (Objeto): null
 * 
 *
 * float
 * Clase Envolvente: Float
 * Valor Predeterminado (Primitivo): 0.0f
 * Valor Predeterminado (Objeto): null
 * 
 * 
 * double
 * Clase Envolvente: Double
 * Valor Predeterminado (Primitivo): 0.0d
 * Valor Predeterminado (Objeto): null
 * 
 *
 * char
 * Clase Envolvente: Character
 * Valor Predeterminado (Primitivo): \u0000
 * Valor Predeterminado (Objeto): null
 * 
 * 
 * String
 * Clase: String
 * Valor Predeterminado: null
 */