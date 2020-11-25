class Viaggio
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
        print(Viaggio.nome_viaggio, Viaggio.data_partenza, Viaggio.data_ritorno, Viaggio.localita, Viaggio.resort, Viaggio.prezzo, Viaggio.partecipanti, Viaggio.responsabile_viaggio):
    pass
    
    def periodo(self):
        print("Giorni programmati: ", Viaggio.data_ritorno - Viaggio.data_partenza)
    pass 
    
class VacanzaInvernale 
    def __init__(self, skipass, impianti_sciistici):
    
    self.skipass = skipass
    self.impianti_sciistici = impianti.sciistici
 
class VacanzaEstiva
    def __init__(self, tragitto, escursioni_marine):
    
    self.tragitto = tragitto
    self.escursioni_marine = escursioni_marine
   
class Azienda
    def __init__(self, denominazione, responsabile_aziendale_viaggio):
    
    self.denominazione = denominazione
    self.responsabile_aziendale_viaggio = viaggio.responsabile_viaggio
    
    def guadagno(self, costo):
        self.costo = costo - 47/100
        print("Costo totale: ", self.costo)
        
    

    
    
