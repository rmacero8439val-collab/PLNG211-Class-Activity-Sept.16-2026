import java.util.Scanner;

public class HighestNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int first = input.nextInt();

        System.out.print("Enter second number: ");
        int second = input.nextInt();

        System.out.print("Enter third number: ");
        int third = input.nextInt();

        int highest = first;

        if (second > highest) {
            highest = second;
        }

        if (third > highest) {
            highest = third;
        }

        System.out.println("The highest number is " + highest);

        input.close();
    }
}