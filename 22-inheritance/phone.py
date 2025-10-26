class Phone:
  def __init__ (self, name):
    self._name = name

  def call(self):
    print (f"{self._name} is making a call")
  
  def send_message(self):
    print(f"{self._name} is sending a message")

class Camera(Phone):
  def take_photo(self):
    print(f"{self._name} is taking a photo")

  def record_video(self):
    print(f"{self._name} is recording video")

class Smartphone(Camera):
  pass

basic_phone = Phone("Nokia")
basic_phone.call()          # Expected Output: Nokia is making a call
basic_phone.send_message()  # Expected Output: Nokia is sending a message

camera = Camera("Canon")
camera.take_photo()    # Expected Output: Canon is taking a photo
camera.record_video()  # Expected Output: Canon is recording video

smartphone = Smartphone("iPhone")
smartphone.call()          # Expected Output: iPhone is making a call
smartphone.send_message()  # Expected Output: iPhone is sending a message
smartphone.take_photo()    # Expected Output: iPhone is taking a photo
smartphone.record_video()  # Expected Output: iPhone is recording video