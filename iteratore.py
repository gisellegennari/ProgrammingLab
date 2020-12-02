class Colori:
 def __init__(self, rosso, giallo, verde):
  self.rosso= rosso
  self.giallo = giallo
  self.verde = verde
  
 def stop(self):
  mylist = [self.rosso, self.giallo, self.verde]
  for x in mylist:
    print ("Semaforo :", x)
    
semaforo = Colori("red", "yellow", "green")
semaforo.stop()
