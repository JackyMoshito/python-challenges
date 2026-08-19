weight = float(input("Enter your weight(kgs): "))
height = float(input("Enter your height(m): "))

BMI = weight / (height ** 2)

# Print BMI rounded to 1 decimal place
print(f"Your BMI is: {BMI:.1f}")

# Check BMI category
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI <= 24.9:
    print("Normal")
elif 25 <= BMI <= 29.9:
    print("Overweight")
else:
    print("Obese")