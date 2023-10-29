# Ideas to add
# Clear the screen after every input
# Libraries

import matplotlib.pyplot as plt
import NutritionLabelOCR as nut

# Global Variables to Keep track of Various Counts
calorie_goal = 2000
calorie_count = 0
carb_count = 0
fat_count = 0
protein_count = 0
premium = False
bmi_list = ["Underweight", "Healthy", "Overweight", "Obese"]
BMI = 0
bmiscoreT = False


# BMI Calculator | This takes the input from the function and puts it into a BMI Calculator. If it is done,
# bmiscoreT will return as True which causes it to show up on the visualize option.
def BMI():
    global bmi_list
    global bmiscore
    global bmiscoreT
    global BMI
    bmi_catergory = ""
    weight = input("Please enter your weight in lb \n=>")
    height = input("Please enter height in inches\n=>")
    bmi = (int(weight) * 703) / (int(height) ** 2)
    bmi = round(bmi, 2)
    if bmi < 18.4:
        bmi_catergory = bmi_list[0]
    elif bmi > 18.5 and bmi < 24.9:
        bmi_catergory = bmi_list[1]
    elif bmi > 24.9 and bmi < 39.9:
        bmi_catergory = bmi_list[2]
    elif bmi > 39.9:
        bmi_catergory = bmi_list[3]
    print(f"\n{'-' * 49}\n\nYour BMI score is {bmi}. You are considered {bmi_catergory}\n\n{'-' * 49}")
    bmiscoreT = True
    BMI = bmi
    return bmi and bmiscoreT


# Advertisement
def advertisement():
    global premium
    print("Would you like to upgrade to PT Fitness Premium for $9.99 (Y/N)")
    verdict = input("\n=> ").upper()
    if verdict == "Y":
        print("Thanks for upgrading, enjoy premium!\n")
        premium = True
    else:
        print("Man, you're really broke. It is only $9.99\n")


# Custom Calorie Creator
def calorie_creator():
    new = input("What would you like to set as your calorie goal?\n=> ")
    if new.isdigit():
        calorie_goal = int(new)
        print(f"\n{'-' * 49} \n\n Your calorie goal has been updated to: {calorie_goal}\n")
        print(f"{'-' * 49}")
    else:
        print("Please enter a valid number")
    return calorie_goal


# Splash Screen: This will be the message that prints to the console as soon as our program runs
def print_splash():
    print("Welcome to the Health and Wellness Tracker!")
    print()


# This method is used to list out all possible things to do in the program and grab user input for what they want to do
def get_input():
    print("What would you like to do?")
    print("Enter (G) to set your own calorie goal")
    print("Enter (A) to add some food")
    print("Enter (V) to visualize your progress")
    print("Enter (B) to calculate BMI")
    print("Enter (X) to quit")
    return input().upper()


# Take a user-input letter from get_input and call the associated method
def input_manager(user_input):
    global premium
    if user_input == 'A':
        print("Let's add some food!")
        food_adder()
    elif user_input == 'V':
        print("Let's visualize your progress!")
        visualize_progress()
    elif user_input == 'X':
        print("Thanks for using fitness tracker, see ya!")
    elif user_input == "G":
        if premium:
            calorie_creator()
        else:
            print("Sorry that's a premium feature")
            advertisement()
    elif user_input == "B":
        if premium:
            BMI()
        else:
            print("Sorry, that's a premium feature")
            advertisement()
    else:
        print("Hm, looks like you didn't enter a valid input. Please try again.")


# Method for adding food (I started this, but we still need to add grams fat etc)
def food_adder():
    global calorie_count
    global fat_count
    global protein_count
    global carb_count
    ans = input("Would you like to upload an image? (Y/N)").upper()
    if ans == "Y":
        picture_food()
    else:
    # Add Calories, fat, carbs, and protein
        calorie_count += number_adder("calories")
        fat_count += number_adder("grams of fat")
        protein_count += number_adder("grams of protein")
        carb_count += number_adder("grams of carbs")


def picture_food():
    global calorie_count
    global fat_count
    global protein_count
    global carb_count
    try:
        filename = input("Please enter the filename of your image")
        serving = int(input("How many servings did you eat?"))
        text = nut.read_text(filename)
        protein = serving * nut.grab_number(text, "PROTEIN")
        protein_count += protein
        fat = serving * nut.grab_number(text, "TOTAL FAT")
        fat_count += fat
        calorie = serving * nut.grab_number(text, "CALORIES")
        calorie_count += calorie
        carb = serving * nut.grab_number(text, "TOTAL CARB")
        carb_count += carb
        print(f"{calorie} calories, {fat} grams of fat, {protein} grams of protein, and {carb} grams of carbs have been added!")
        print()
    except Exception as e:
        print("Oops, something went wrong:", e)

# Grab a user input number and make sure it's valid
def number_adder(food_group):
    num = input(f"How many {food_group} did you eat?\n=>")
    if num.isdigit():
        # Add the calories to the count and print a success method.
        print(f"Great! {num} {food_group} have been added.\n")
        return int(num)
    # In case User-Input is Invalid, print an error message and have them try again.
    elif is_float(num):
        print(f"Invalid input, please round to nearest whole {food_group}")
        print()

    else:
        print(f"Invalid input, {food_group} must be a whole, positive number.")
        print()
        return number_adder(food_group)


# Helper method to check if a string is a float
def is_float(string):
    try:
        # Return true if float
        float(string)
        return True
    except ValueError:
        # Return False if Error
        return False


# Method for visualizing progress
def visualize_progress():
    print("Now we're in the progress visualizer")
    print(f"\n{'-' * 49}\n\nTotal calories consumed today: {calorie_count}")
    print(f"Total calories left for the day: {calorie_goal - calorie_count}")
    print(f"\nTotal grams of carbs consumed today: {carb_count}")
    print(f"Total grams of fat consumed today: {fat_count}")
    print(f"Total grams of protein consumed today: {protein_count}")
    if bmiscoreT:
        print(f"You have a BMI score of {BMI}\n\n{'-' * 49}")
    else:
        print(f"\n{'-' * 49}")
    if calorie_count != 0:
        make_pie()


def make_pie():
    total = carb_count + fat_count + protein_count
    labels = ["Carbs", "Fat", "Protein"]
    size = [carb_count / total, fat_count / total, protein_count / total]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0)  # To explode a slice if desired
    plt.figure(figsize=(8, 8))  # Set the size of the plot
    plt.pie(size, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')

    # Set the title of the pie chart
    plt.title('Breakdown of Macros')
    # Show the pie chart
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_splash()
    advertisement()
    command = ''
    while command != 'X':
        command = get_input()
        input_manager(command)
