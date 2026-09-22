import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class ThreeWords {
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        Scanner input = new Scanner(System.in);

        System.out.print("Enter first word: ");
        String first = input.next();

        System.out.print("Enter second word: ");
        String second = input.next();

        System.out.print("Enter third word: ");
        String third = input.next();

        System.out.println(first + " " + second + " " + third);

        input.close();
    }
}