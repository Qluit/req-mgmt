// test_bmi_calculator.cpp
#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "bmi_calculator.cpp"

TEST_CASE("Normal BMI") {
    REQUIRE(calculate_bmi(70, 1.75) == Approx(22.86).epsilon(0.01));
}

TEST_CASE("Overweight BMI") {
    REQUIRE(calculate_bmi(85, 1.75) == Approx(27.76).epsilon(0.01));
}

TEST_CASE("Underweight BMI") {
    REQUIRE(calculate_bmi(50, 1.75) == Approx(16.33).epsilon(0.01));
}

TEST_CASE("Zero Height") {
    REQUIRE_THROWS_AS(calculate_bmi(70, 0), std::invalid_argument);
}

TEST_CASE("Negative Height") {
    REQUIRE_THROWS_AS(calculate_bmi(70, -1.75), std::invalid_argument);
}