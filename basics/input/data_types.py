def run():
  print("What is your name human?")
  name = input()
  print("How old are you (in years)?")
  age = input()
  print("How tall are you (in meters)?")
  height = float(input())
  print ("How much do you weigh (in kilograms)?")
  weight = float(input())
  BMI = str(round((weight/(height**2)),2))

  print(name +" you are " + age + " years old and your bmi is " + BMI +".")