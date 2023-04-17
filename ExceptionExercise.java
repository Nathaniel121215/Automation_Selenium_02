import java.util.Scanner;
import java.util.InputMismatchException;

public class ExceptionExercise {
    
    public static void main(String[] args) {
       
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter the first number: ");
            Integer first = scanner.nextInt();
            first = 1 / first;

            System.out.print("Enter the second number: ");
            Integer second = scanner.nextInt();
            second = 1 / second;
    
            System.out.print("Enter the third number: ");
            Integer third = scanner.nextInt();
            third = 1 / third;
            
            float average = (first + second + third)/3;
    
            System.out.println(average);
          }
          catch(InputMismatchException e) {
            System.out.println("Invalid input. Please enter an integer.");
          }
          catch(ArithmeticException e) {
            System.out.println("Cannot divide by zero.");
          }
          catch(NullPointerException e) {
            System.out.println("One or more numbers are missing.");
          }
          
        
    }
}