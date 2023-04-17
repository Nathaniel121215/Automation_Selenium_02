import java.util.Scanner;
import java.util.InputMismatchException;

public class Employee {
    private String name;
    private int age;
    private double salary;
    public Employee(String name, int age, double salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }
    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }
    public double getSalary() {
        return salary;
    }
    public void setSalary(double newSalary) {
        this.salary = newSalary;
    }

    public double getAnnualSalary() {
        return salary * 12;
    }

    public void raised(double percentage) {
        double newsalary = salary * percentage / 100.0;
        salary += newsalary;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        System.out.print("Enter your salary: ");
        Double salary = scanner.nextDouble();


        Employee test = new Employee(name, age, salary);

        System.out.println("result:");
        System.out.println("name: " +test.getName());
        System.out.println("age: " +test.getAge());
        System.out.println("salary: " +test.getSalary());
        System.out.println("anual: " + test.getAnnualSalary());

        test.raised(50);
        
        System.out.println("raised salary: " +test.getSalary());

    }
}