#Problem J1: Body Mass Index - 2008 (SirNooby)
weight = float(input())
height = float(input())

bmi = weight / (height * height)

if bmi < 18.5:
    print("Underweight")
elif bmi > 25:
    print("Overweight")
else:
    print("Normal weight")