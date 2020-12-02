class Colori:
 def __init__(self, a, b, c):
  self.a = a
  self.b = b
  self.c = c
  
 def stop(self):
  mylist = [self.a, self.b, self.c]
  for colore in mylist:
    if(colore == "rosso"):
      print("Semaforo: ", colore, ": Fermati!")
    #print ("Semaforo :", colore)
    elif(colore == "giallo"):
      print("Semaforo: ", colore, ": Veloce..")
    else:
      print("Semaforo: ", colore, ": Vai tranquillo!")
    
semaforo = Colori("rosso", "giallo", "verde")
semaforo.stop()
