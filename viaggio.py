class Viaggio:
    def __init__(self, nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile_viaggio):
    
      self.nome_viaggio = nome_viaggio
      self.data_partenza = data_partenza
      self.data_ritorno = data_ritorno
      self.localita = localita
      self.resort = resort
      self.prezzo = prezzo
      self.partecipanti = partecipanti
      self.responsabile_viaggio = responsabile_viaggio
    
    def scheda_viaggio(self):
        return self.nome_viaggio
    pass
    
    def stampa(self):
        print(self.nome_viaggio, self.data_partenza, self.data_ritorno, self.localita, self.resort, self.prezzo, self.partecipanti, self.responsabile_viaggio)
    pass
    
    def periodo(self):
        print("Giorni programmati: ", Viaggio.data_ritorno - Viaggio.data_partenza)
    pass 
    
class VacanzaInvernale: 
    def __init__(self, skipass, impianti_sciistici):
    
     self.skipass = skipass
     self.impianti_sciistici = impianti.sciistici
    
    def costo_aggiuntivo(self, luogo, percentuale):
      self.luogo = luogo
      self.percentuale = percentuale


class VacanzaEstiva:
    def __init__(self, tragitto, escursioni_marine):
    
     self.tragitto = tragitto
     self.escursioni_marine = escursioni_marine

    def costo_aggiuntivo(self, escursioni_coppia):
      self.escursioni_coppia = escursioni_coppia
   
class Azienda:
    def __init__(self, denominazione, responsabile_aziendale_viaggio):
    
      self.denominazione = denominazione
      self.responsabile_aziendale_viaggio = viaggio.responsabile_viaggio
    
    def guadagno(self, costo):
        self.costo = costo - 47/100
        print("Costo totale: ", self.costo)
        
    
viaggio1 = Viaggio("Voyage", "10/11/2021", "17/11/2021", "San Paolo", "Grand Hotel", "1200€", "12", "Pippo Oppip")
viaggio1.stampa()
#winter = VacanzaInvernale("skipass", "impianti_sciistici")
#Cortina = costo_aggiuntivo(skipass + 15/100)
#San Mortiz = costo_aggiuntivo(skipass + 10/100)
#Generico = costo_aggiuntivo(skipass + 5/100)
#winter.stampa()
#summer = VacanzaEstiva("tragitto", "Deep Diving")
#escursioni_coppia = costo_aggiuntivo(costo.Azienda + 10/100)
    

    
    
