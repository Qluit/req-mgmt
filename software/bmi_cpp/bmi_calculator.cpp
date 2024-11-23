// bmi_calculator.cpp
#include <iostream>
#include <stdexcept>

double calculate_bmi(double weight, double height) {
    if (height < 0) {
        throw std::invalid_argument("Height must be greater than zero");
    }
    return weight / (height * height);
}

#ifndef CATCH_CONFIG_MAIN
int main(int argc, char * argv[]) {
    double weight, height;
    std::cout << "Enter weight in kilograms: ";
    std::cin >> weight;
    std::cout << "Enter height in meters: ";
    std::cin >> height;

    try {
        double bmi = calculate_bmi(weight, height);
        std::cout << "Your BMI is: " << bmi << std::endl;
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
#endif