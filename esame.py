class ExamException(Exception):
    pass


class CSVTimeSeriesFile:
    def __init__(self, name):

        # Setto il nome del file
        self.name = name

    def get_data(self):
        # Inizializzo una lista vuota per salvare i valori
        values = []
        values2 = []  #lista che contiene giorno per giorno

        # Provo ad aprire il file per estrarci i dati. Se non ci riesco, prima avverto del'errore,
        # poi devo abortire. Questo e' un errore "un-recoverable", ovvero non posso proseguire con
        # la lettura dei dati se non riesco ad aprire il file!
        try:
            my_file = open(self.name, 'r')
        except Exception as e:

            # Stampo l'errore
            print('Errore nella lettura del file: "{}"'.format(e))

            # Esco dalla funzione tornando "niente".
            return None

        # Ora inizio a leggere il file linea per linea
        for line in my_file:

            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'epoch' and elements[1] != 'temperature':

                # Setto la data ed il valore
                #date  = elements[0]
                value = elements[0]
                value2 = elements[1]

                # La variabile "value" al momento e' ancora una stringa, poiche' ho letto da file di testo,
                # quindi converto a valore floating point, e se nel farlo ho un errore avverto. Questo e'
                # un errore "recoverable", posso proseguire (semplicemente salto la linea).
                try:
                    value = int(value)
                    value2 = float(value2)
                except Exception as e:

                    # Stampo l'errore
                    print('Errore nela conversione a float: "{}"'.format(e))

                    # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                    continue

                # Infine aggiungo alla lista dei valori questo valore
                values.append(value)
                values.append(value2)

                #inserisco i primi valori della lista nella lista
                values2.append(values)
                values = []

        # Chiudo il file
        my_file.close()

        # Quando ho processato tutte le righe, ritorno i valori
        return values2

    def daily_stats(self, time_series):

        listApp = []  #####da cancellare
        day_start_epoch = 0
        nmin = []
        nmax = []
        risultato = []
        nmedia = 0
        count_n = 0
        i = 0
        ii = 0
        while i < len(time_series):
            #day_start_epoch = time_series[i][0] - (time_series[i][0] % 86400)
            #memory = day_start_epoch = time_series[ii][0] - (time_series[ii][0] % 86400)
            day_start_epoch = time_series[i][0]
            memory = time_series[ii][0]

            if memory == day_start_epoch:
                #nmin += str(time_series[i][1]) + "-"
                nmin.append(time_series[i][1])
                nmax.append(time_series[i][1])
                nmedia += time_series[i][1]  ### inizio a fare il conteggio per la media
                count_n += 1
            else:
                nmedia = nmedia / count_n
                listApp.append(min(nmin))
                listApp.append(max(nmax))
                listApp.append(int(nmedia))
                risultato.append(listApp)
                nmedia = 0
                nmin = []
                nmax = []
                listApp = []
                count_n = 0
                ii = i
                i -= 1

            if i == len(time_series) - 1:
                listApp.append(min(nmin))
                listApp.append(max(nmax))
                listApp.append(int(nmedia/count_n))
                risultato.append(listApp)
            i += 1
        return risultato


#======================
# Corpo del programma
#======================

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
time_series2 = time_series_file.daily_stats(time_series)

print('Dati contenuti nel file: "{}"'.format(time_series2))

