import alpha

def speak(self):
  print "what is up " + self.name

def patch():
  alpha.Alpha.speak = speak

