// BMICalculator.java
public class BMICalculator {
    public static double calculateBMI(double weight, double height) {
        if (height < 0) {
            throw new IllegalArgumentException("Height must be greater than zero");
        }
        return weight / (height * height);
    }

    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Enter weight in kilograms: ");
        double weight = scanner.nextDouble();
        System.out.print("Enter height in meters: ");
        double height = scanner.nextDouble();
        scanner.close();

        try {
            double bmi = calculateBMI(weight, height);
            System.out.printf("Your BMI is: %.2f%n", bmi);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}