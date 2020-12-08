from tech import Tech

class JetPack(Tech):
  
  def __init__(self):
    super().__init__()

  def activate():
    print("Jetpack has been activated.")
  
  def deactivate():
    print("Jetpack has been deactivated.")

  def fly(speed):
    print(f"Flying with a speed of {speed}.")