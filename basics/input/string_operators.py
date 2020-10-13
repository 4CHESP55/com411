def run():
  lives = "♥"
  level = "♦"

  print("Please enter the number of lives.")
  numLives = int(input())
  
  print("Please enter the energy level.")
  numLevel = int(input())
  
  print("Please enter the shield level.")
  numShield = int(input())
  
  print("Health has been set.")
  print("Lives: " + lives*numLives)
  print("Energy: " + level*numLevel)
  print("Shield: " + level*numShield)
