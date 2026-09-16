
import java.util.Scanner;

public class SwitchAct {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double x, y, result;
        int choice;

        System.out.print("Enter value of x: ");
        x = input.nextDouble();

        System.out.print("Enter value of y: ");
        y = input.nextDouble();

        result = 0.0;

        System.out.println("\nVariable values:");
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("result = " + result);

        System.out.println("\nSelect Arithmetic Operation:");
        System.out.println("1. Addition (+)");
        System.out.println("2. Subtraction (-)");
        System.out.println("3. Multiplication (*)");
        System.out.println("4. Division (/)");
        System.out.println("5. Modulus (%)");
        System.out.println("6. Increment & Decrement (x++ and x--)");
        System.out.print("Enter your choice (1-6): ");
        choice = input.nextInt();

        System.out.println("\nResult:");
        switch (choice) {
            case 1:
                result = x + y;
                System.out.println("Addition: x + y = " + result);
                break;
            case 2:
                result = x - y;
                System.out.println("Subtraction: x - y = " + result);
                break;
            case 3:
                result = x * y;
                System.out.println("Multiplication: x * y = " + result);
                break;
            case 4:
                if (y != 0) {
                    result = x / y;
                    System.out.println("Division: x / y = " + result);
                } else {
                    System.out.println("Error: Division by zero is not allowed.");
                }
                break;
            case 5:
                if (y != 0) {
                    result = x % y;
                    System.out.println("Modulus: x % y = " + result);
                } else {
                    System.out.println("Error: Modulus by zero is not allowed.");
                }
                break;
            case 6:
                x++;
                System.out.println("Increment: x++ = " + x);
                x--;
                x--;
                System.out.println("Decrement: x-- = " + x);
                break;
            default:
                System.out.println("Invalid choice! Please select an option between 1 and 6.");
                break;
        }

        input.close();
    }
}
