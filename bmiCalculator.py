
#bmi = weight(kg)/ height^2(m^2)

weight=input("Enter your weight in kg: ")
height=input("Enter your height in meters: ")
status=""
bmi= round(((float(weight))/(float(height)*float(height))),1)
print(bmi)
if bmi >= 30.0:
    print("Obese weight")
elif bmi >=29.9 and bmi<=25.0:
    print("Overweight")
elif bmi >= 18.5  and bmi<=24.9:
    print("Normal weight")
elif bmi < 18.5:
    print("Underweight")
else:
    print("Error")
