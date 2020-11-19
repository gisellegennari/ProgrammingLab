# Una classe persona con anagrafica
class Persona:
  def __init__(self, ruolo, nome, cognome):
    self.ruolo = ruolo 
    self.nome = nome 
    self.cognome = cognome

  def bonjour(self):
    print(self.ruolo, ":", self.nome, self.cognome)

# Una sotto-classe Docente che modella una persona
# per la quale ho anche un corso associato, come docente.
class Docente(Persona):

  def __init__(self, nome, cognome, corso):
    super().__init__("Docente UNITS", nome, cognome)
    self.corso = corso
    
  def bonjour(self): 
    Persona.bonjour(self) 
    print("> Docente del corso:", self.corso)

# Una sotto-classe Studente che modella una persona
# per la quale ho anche un corso associato
class Studente(Persona):
    
    # Per costruirla prendo tutti i dati che mi servono
    # (incluso quelli di Persona), ed anche un corso.    
    # Nella costruzione richiamo __init__ di Persona 
    # (che gia mi salva nome/cognome e ruolo) e poi
    # lavoro con le variabili specifiche Di Studente
  def __init__(self, nome, cognome, corso):
    super().__init__("Studente UNITS", nome, cognome)
    self.corso = corso
    
    # Ridefinisco il metodo di Persona. La stampa per
    # lo studente deve riportare ANCHE il corso seguito.
  def bonjour(self): 
    Persona.bonjour(self) # Che uso qui esplicitamente
    print("> Frequento il corso:", self.corso)

# Creo un oggetto della superclasse Persona
obj_unaPersona = Studente("qualcuno", "Giulio", "Caravagna")
obj_unaPersona.bonjour()

# Creo un oggetto e chiamo la funzione bonjour()
obj_Giulio = Studente("Giulio", "Caravagna", "Programmazione")
obj_Giulio.bonjour()

obj_Giuseppi = Studente("Giuseppi", "Conte", "Programmazione")
obj_Giuseppi.bonjour()

obj_ProfRusso = Docente("Stefano Alberto", "Russo", "Programmazione")
obj_ProfRusso.bonjour()
