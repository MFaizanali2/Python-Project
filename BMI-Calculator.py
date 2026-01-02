weight: float = float(input("Enter Your Weight in kg: "))
print("Enter your height:")

feet = int(input("  Feet: "))
inches = int(input("  Inches: "))

height_meters = (feet * 0.3048) + (inches * 0.0254)

bmi = weight / (height_meters * height_meters)
bmi = round(bmi, 2)

print(f"Your Bmi is {bmi}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obesity")

print("Thank you for using BMI Calculator!")