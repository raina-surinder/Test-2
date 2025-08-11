import java.util.Scanner;

public class test1 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter value for a: ");
            int a = scanner.nextInt();

            System.out.print("Enter value for b: ");
            int b = scanner.nextInt();

            int sum = a + b;
            System.out.println("Sum of a and b: " + sum);
        }
    }
}