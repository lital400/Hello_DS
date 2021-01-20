# Author: Lital Israel
# Course: CAP 4784
# 1/20/21
# Lab 2 - Paint and BMI Calculator Assignment

def calcPaintGallons(length, width, height, doors, windows):
    totalArea = (width * height * 2 + length * height * 2) - (doors * 25) - (windows * 10)
    paintNeeded = totalArea / 315
    return paintNeeded


def calcBmi(weight, height):
    bmi = (weight * 703)/(height*height)
    if bmi < 18.5:
        status = 'Underweight'
    elif 18.5 <= bmi <= 24.9:
        status = 'Normal'
    elif 25 <= bmi <= 29.9:
        status = 'Overweight'
    else:
        status = 'Obese'
    return bmi, status


active = True
while active:
    print("Welcome to my Python program.")
    print("Menu options:")
    print("\tEnter 1 for calculating gallons of paint needed to paint a room")
    print("\tEnter 2 for calculating Body Mass Index")
    print("\tEnter any other value to quit the program")
    try:
        option = int(input('Enter menu option: '))
        if option == 1:
            print("\n-------------------------------------")
            print("Welcome to the paint needed calculator.")
            ok = True
            while ok:
                try:
                    length = float(input('Enter the length of the room: '))
                    width = float(input('Enter the width of the room: '))
                    height = float(input('Enter the height of the room: '))
                    doors = int(input('How many doors are in the room? '))
                    windows = int(input('How many windows are in the room? '))
                    gallons = calcPaintGallons(length, width, height, doors, windows)
                    print("\n------------------------------------------------")
                    print('{gallons: .2f} gallons of paint are needed to paint a room {width: .2f} feet wide by'.format(**locals()),
                          '{length: .2f} feet long by {height: .2f} feet high with {doors} doors and {windows} windows.'.format(**locals()))
                    print("------------------------------------------------\n")
                    ok = False
                except ValueError:
                    print("\nPlease enter a valid number value.\n")
        elif option == 2:
            print("\n------------------------------------------------")
            print("Welcome to the body mass index (BMI) calculator.")
            ok = True
            while ok:
                try:
                    weight = float(input('Enter your weight in pounds: '))
                    height = float(input('Enter your height in inches: '))
                    bmi, status = calcBmi(weight, height)
                    print("\n------------------------------------------------")
                    print('Your BMI is {bmi: .2f}. According to NIH, you are {status}.'.format(**locals()))
                    print("------------------------------------------------\n")
                    ok = False
                except ValueError:
                    print("\nPlease enter a valid number value.\n")
        else:
            active = False
    except ValueError:
        print("\n------------------------------------------------")
        print("Please enter a valid number value.")
        print("------------------------------------------------\n")
