# Author: Jessica Strait
# This project calculates how far an object falls based on time and the force of gravity.

# First things first, let's go ahead and define the gravity constant.

gravity = 9.8

# Now, we're going to define our function. We will use the formula given to us to solve for distance, with respect to
# time, which will be the input given by the user. Don't forget to return the function!


def fallingDistance(time):
    distance = (1/2)*gravity*(time**2)
    return distance


# As always, we will tell the user what the program does. We will also assign the time variable as the value the user
# inputs. Remember that this input should be an integer, since it is time.

print("This program tells you how far an object will fall in a number of seconds.")
time = int(input("Enter your desired falling time in seconds. Enter a negative number to stop."))

# Time to call our function!

solution = fallingDistance(time)

# Let's use a while loop to make sure the user can input more values for time. Remember to round the solution to one
# decimal place as well. When the user decides to input a negative number, the program will end.

while time >= 0:
    solution = fallingDistance(time)
    print("The distance the object will fall in", time, "seconds is:", round(float(solution), 1), "meters.")
    time = int(input("Enter your next desired falling time in seconds. Enter a negative number to stop."))
else:
    print("Thank you for calculating.")