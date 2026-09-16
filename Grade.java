
import java.util.Scanner;

public class Grade {
public static void main(String[] args) {
Scanner input = new Scanner(System.in);
String continueProgram;
do {
double javaScore, cScore, databaseScore, average;
char grade;
System.out.println(" STUDENT GRADE PROGRAM");
System.out.print("Enter Java Programming score: ");
javaScore = input.nextDouble();
System.out.print("Enter C Programming score: ");
cScore = input.nextDouble();
System.out.print("Enter Database Handling score: ");
databaseScore = input.nextDouble();
average = (javaScore + cScore + databaseScore) / 3;
if (average >= 90 && average <= 100) {
grade = 'A';
} else if (average >= 80) {
grade = 'B';
} else if (average >= 75) {
grade = 'C';
} else {
grade = 'F';
}
System.out.println("\nOUTPUT");
System.out.printf("Average: %.2f%n", average);
System.out.println("Grade: " + grade);
input.nextLine();
System.out.print("\nDo you want to continue: YES / NO: ");
continueProgram = input.nextLine();
} while (continueProgram.equalsIgnoreCase("YES"));
System.out.println("\nProgram terminated.");
input.close();
}
}
