
import java.util.Scanner;

public class Elif {
public static void main(String[] args) {
    try (Scanner input = new Scanner(System.in)) {
        String continueProgram;
        do {
        double x, y, result;
        System.out.print("Enter value of x: ");
        x = input.nextDouble();
        System.out.print("Enter value of y: ");
        y = input.nextDouble();
        result = 0.0;
        System.out.println("\nVariable values:");
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("result = " + result);
        System.out.println("\nArithmetic Operation:");
        System.out.println("Addition: x + y = " + (x + y));
        System.out.println("Subtraction: x - y = " + (x - y));
        System.out.println("Multiplication: x * y = " + (x * y));
        System.out.println("Division: x / y = " + (x / y));
        System.out.println("Modulus: x % y = " + (x % y));
        x++;
        System.out.println("Increment: x++ = " + x);
        x--;
        System.out.println("Decrement: x-- = " + x);
   input.nextLine();
System.out.print("\nDo you want to continue: YES / NO: ");
continueProgram = input.nextLine();
} while (continueProgram.equalsIgnoreCase("YES"));
System.out.println("\nProgram terminated.");
input.close();
}
}
}