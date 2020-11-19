# Una classe persona con anagrafica
class Persona:
  def __init__(self, ruolo, nome, cognome, im):
    self.ruolo = ruolo 
    self.nome = nome 
    self.cognome = cognome
    self.im= im
  def bonjour(self):
    print(self.ruolo, " : ", self.nome, " : ", self.cognome, " : ", self.im)
  def buongiono(self):
    print(self.ruolo, " : ", self.nome, " : ", self.cognome, " : ", self.im)
pass

# Una sotto-classe Docente che modella una persona
# per la quale ho anche un corso associato, come docente.
class Docente(Persona):

  def __init__(self, nome, cognome, corso):
    super().__init__("Docente UNITS", nome, cognome)
    self.corso = corso
    
  def bonjour(self): 
    Persona.bonjour(self) 
    print("> Docente del corso:", self.corso)
pass


# Una sotto-classe Studente che modella una persona
# per la quale ho anche un corso associato
class Studente(Persona):
    
    # Per costruirla prendo tutti i dati che mi servono
    # (incluso quelli di Persona), ed anche un corso.    
    # Nella costruzione richiamo __init__ di Persona 
    # (che gia mi salva nome/cognome e ruolo) e poi
    # lavoro con le variabili specifiche Di Studente
  def __init__(self, nome, cognome, corso,im):
    super().__init__("Studente UNITS", nome, cognome, im)
    self.corso = corso
    self.immatricolazione = im
    # Ridefinisco il metodo di Persona. La stampa per
    # lo studente deve riportare ANCHE il corso seguito.
  def bonjour(self): 
    Persona.bonjour(self) # Che uso qui esplicitamente
    print("> Frequento il corso:", self.corso)
  
  def buongiono(self):
    Persona.buongiono(self)
    print("° benvenuto", self.im)

# Creo un oggetto della superclasse Persona
obj_unaPersona = Studente("qualcuno", "Giselle", "Caravagna", "278183")
obj_unaPersona.bonjour()
obj_unaPersona.buongiono()
