# Author: Jessica Strait
# This project determines BMI based on height and weight input from the user.

# First, the program will prompt the user to enter their weight.

weight = float(input("Enter your weight in pounds."))

# Next, the program will prompt the user to enter their heights.

height = float(input("Enter your height in inches."))

# We will assign the variable "BMI" to calculate our target using the two earlier variables of
# weight and height as entered by the user.

BMI = weight*703/height**2
print("Your BMI is", BMI)

# Now, we will tell the program how to determine if a BMI is overweight, underweight, or
# optimal weight based on the calculated number.

underweight = BMI <= 18.5
if underweight:
    print("Your BMI indicates that you are underweight.")
else:
    overweight = BMI >= 25
    if overweight:
        print("Your BMI indicates that you are overweight.")
    else:
        print("Your BMI indicates that you are optimal weight.")