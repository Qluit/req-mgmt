def calculate_bmi(weight, height):
    """
    Calculate BMI given weight in kilograms and height in meters.
    """
    if height < 0:
        raise ValueError("Height must be greater than zero")
    return weight / (height ** 2)

if __name__ == "__main__":
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")
