class Frutta:
  def __init__(self, frutta):
    self.frutta = frutta

    #test o next, è solo il nome della funzione attuale, purchè poi lo cambio anche giu
  def test(self):
    myit = iter(self.frutta)
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))

pippo = Frutta("banana")
#test o next
pippo.test()
