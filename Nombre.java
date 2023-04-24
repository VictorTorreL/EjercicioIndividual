import java.util.Scanner;

public class Saludo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("¿Cuál es tu nombre?");
        String nombre = input.nextLine();

        System.out.println("Hola, " + nombre + "! Bienvenido al programa de saludo.");
    }
}
