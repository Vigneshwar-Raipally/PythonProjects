def BMICalculator(name, weight, height):
    bmi=(weight*703)/(height*height)
    return bmi
n="vignesh"
w=80
h=69
YourBMI=BMICalculator(n, w, h)
b=round(YourBMI,2)
print(b)
if b < 18.5:
    print(n, "You are underweight")
elif b <= 24.9:
    print(n, "You are Normal weight")
elif b <= 29.9:
    print(n, "You are Overweight")
elif b >= 30:
    print(n, "You are Obese")
else:
    print("Invalid Input")