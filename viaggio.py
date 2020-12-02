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
     self.impianti_sciistici = impianti_sciistici
    
    def costo_aggiuntivo(self, luogo, percentuale):
      self.luogo = luogo
      self.percentuale = percentuale
    
    def stampa(self):
      print(self.luogo, self.percentuale)

class VacanzaEstiva:
    def __init__(self, tragitto, escursioni_marine):
    
     self.tragitto = tragitto
     self.escursioni_marine = escursioni_marine

    def costo_aggiuntivo(self, escursioni_coppia):
      self.escursioni_coppia = escursioni_coppia
   
    def stampa(self):
     print(self.escursioni_marine)


class Azienda:
    def __init__(self, denominazione, responsabile_aziendale_viaggio):
    
      self.denominazione = denominazione
      self.responsabile_aziendale_viaggio = responsabile_aziendale_viaggio
    
    def guadagno(self):
        self.costo = 10 - 47/100
        #print("Costo totale: ", self.costo)
        return(self.costo)
        
    
viaggio1 = Viaggio("Voyage", "10/11/2021", "17/11/2021", "San Paolo", "Grand Hotel", "1200€", "12", "Pippo Oppip")
viaggio1.stampa()

winter = VacanzaInvernale("skipass", "impianti_sciistici")
winter.costo_aggiuntivo("Cortina", "+15%")
winter.stampa()

winter2 = VacanzaInvernale("skipass", "impianti_sciistici")
winter2.costo_aggiuntivo("San Mortiz", "+10%")
winter2.stampa()

winter3 = VacanzaInvernale("skipass", "impianti_sciistici")
winter3.costo_aggiuntivo("Generico", "+5%")
winter3.stampa()

#societa = Azienda("GiselleS.P.A", "Arcangelo")

summer = VacanzaEstiva("tragitto", "Deep Diving")
summer.costo_aggiuntivo("escursioni_coppia + 10%")
summer.stampa()  
