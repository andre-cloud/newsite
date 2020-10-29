from django.db import models

# Create your models here.
from django.db import models
from polymorphic.models import PolymorphicModel


# Create your models here.

class Exercise(PolymorphicModel):

    title = models.CharField(max_length=120, help_text='Inserire un titolo esplicativo')
    text = models.TextField(help_text='Scrivere il testo del problema. Se si è utilizzato il bot che sfrutta la tecnologia OCR controllare la correttezza del teso ricevuto.')
    fig = models.ImageField(upload_to='img/', blank=True, null=True, help_text='Carica un\'eventuale immagine che completi il testo dell\'esercizio')
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    referance = models.TextField(help_text='Se è un libro: Cognome N., Titolo del testo, Casa editrice, anno di pubblicazione con edizione, pagina. Se è un sito inserire il link')
    status = models.CharField(max_length=10, default="Draft", editable=False)
    slug = models.SlugField(help_text='NON MODIFICARE') #human-friendly URL

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Esercizio'
        verbose_name_plural = 'Esercizi'



class Matematica(Exercise):

    class Argomento(models.TextChoices):
        n_reali = 'NRE', ('1. Numeri reali')
        n_complessi = 'COM', ('2. Numeri complessi')
        sp_euclideo = 'EUC', ('3. Lo spazio euclideo \(R^n\)')
        topo = 'TOP', ('4. Topologia di \(R^n\)')
        asint = 'ASI', ('5. Confronto asintotico')
        serie = 'SER', ('6. Serie')
        serie_pot = 'SEP', ('7. Serie di potenze')
        deriv = 'DER', ('8. Derivate')
        fun_ele = 'FEL', ('9. Funzioni elemntari')
        arg_complex= 'ACO', ('10. Argomento di un numero complesso')
        prim_int = 'INT', ('11. Primitive ed integrali')
        svil_serie = 'SSE', ('12. Sviluppi in serie')
        int_improp = 'INI', ('13. Integrali impropi')

    argomento = models.CharField(max_length=3, choices=Argomento.choices, help_text='Selezionare l\'argomento di appartenenza dell\'esercizio')
    grafico = models.ImageField(upload_to='graphs', blank=True, help_text='Caricare un file .png/.svg/.jpeg contenente l\'eventuale grafico necessario per la dimostrazione')
    dim = models.TextField(help_text='Scrivere la dimostrazione per risolvere il problema. È pensato anche come entry per definire l\'eventuale sistema di equazioni per risolvere il problema.')
    commento = models.TextField(help_text='Commentare il processo mentale che ha portato alla scelta di ciò che è stato caricato come "struttura" e nell\'eventuale meccanismo.')
    risultato = models.TextField(help_text='Evidenziare il risultato ottenuto dalla risoluzione delle equazioni.', blank=True)


    def __str__(self) -> str:
        return "Matematica"

    def desc(self):
        return """ La regina delle scienze. Senza di lei non esisterebbe nessuna teoria. """

    class Meta:
        verbose_name = 'Matematica'
        verbose_name_plural = verbose_name


class Chimica_Organica(Exercise):

    class Argomento(models.TextChoices):
        alcani = 'CAN', ('1. Alcani')
        alcheni = 'CHE', ('2. Alcheni')
        alchini = 'CHI', ('3. Alchini')
        aromatici = 'PHS', ('4. Aromatici')
        alogenoderivati = 'ALO', ('5. Alogenoderivati')
        alcoli = 'ALC', ('5. Alcoli e Tioli')
        ammine = 'AMM', ('6. Ammine')
        carbonile = 'RCO', ('7. Carbonile')
        sintesi = 'SIN', ('8. Sintesi')

    argomento = models.CharField(max_length=3, choices=Argomento.choices, help_text='Selezionare l\'argomento di appartenenza dell\'esercizio')
    strutture = models.ImageField(upload_to='str/',help_text='Caricare un file .png/.svg/.jpeg contenente lo schema della reazione')
    meccanismo = models.ImageField(upload_to='mech/', blank=True, help_text='Caricare un file .png/.svg/.jpeg contenente lo schema dell\'eventuale meccanismo di reazione')
    commento = models.TextField(help_text='Commentare il processo mentale che ha portato alla scelta di ciò che è stato caricato come "struttura" e nell\'eventuale meccanismo.')

    def __str__(self) -> str:
        return "Chimica Organica"

    def desc(self):
        return """ La chimica che si occupa dello studio della chimica del carbonio e come questo interagisca con gli altri elementi della tavola periodica. """

    class Meta:
        verbose_name = 'Chimica Organica'
        verbose_name_plural = verbose_name

class Chimica_Generale_Analitica(Exercise):

    class Argomento(models.TextChoices):
        intro = 'INT', ('0. Nomenclatura e Cifre significative')
        stechio = 'STE', ('1. Stechiometria')
        theo_atomica = 'ATM', ('2. Teoria atomica e Proprietà periodiche')
        reactions = 'REA', ('3. Reazioni chimiche')
        prin_therm = 'PTH', ('4. Principi di termochimica')
        bond = 'BON', ('5. Legami chimici')
        soluzioni = 'SOL', ('6. Soluzioni e concentrazioni')
        colligative = 'COL', ('7. Proprietà colligative')
        acidi_basi = 'ACB', ('8. Teorie del pH e tamponi')
        redox = 'RED', ('9. Reazioni redox')

    argomento = models.CharField(max_length=3, choices=Argomento.choices, help_text='Selezionare l\'argomento di appartenenza dell\'esercizio')
    sistema = models.TextField(help_text='Scrivere qui le varie equazioni utilizzate per risolvere il problema. Possibilmente numerarle.')
    commento = models.TextField(help_text='Commentare il processo mentale che ha portato alla scrittura delle varie equazioni utilizzate facendo rifermento.')
    risultato = models.TextField(help_text='Evidenziare il risultato ottenuto dalla risoluzione delle equazioni.')

    def __str__(self) -> str:
        return "Chimica Generale e Analitica"

    def desc(self):
        return """ La chimica che si occupa dei vari equilibri in soluzione acquosa """

    class Meta:
        verbose_name = 'Chimica Generale ed Analitica'
        verbose_name_plural = verbose_name

class Chimica_Fisica(Exercise):

    class Argomento(models.TextChoices):
        gas = 'GAS', ('1. Teorie dei gas')
        termodinamica = 'THD', ('2. Termodinamica')
        termochimica = 'THC', ('3. Termochimica')
        cinetica = 'KIN', ('4. Cinetica chimica')
        elettrodi = 'ELE', ('5. Elettrodi')

    argomento = models.CharField(max_length=3, choices=Argomento.choices, help_text='Selezionare l\'argomento di appartenenza dell\'esercizio')
    sistema = models.TextField(blank=True, help_text='Scrivere qui le varie equazioni utilizzate per risolvere il problema. Possibilmente numerarle.')
    grafico = models.ImageField(upload_to='graphs', blank=True, help_text='Caricare un file .png/.svg/.jpeg contenente l\'eventuale grafico necessario.')
    commento = models.TextField(help_text='Commentare il processo mentale che ha portato alla scrittura delle varie equazioni utilizzate facendo rifermento.')
    risultato = models.TextField(help_text='Evidenziare il risultato ottenuto dalla risoluzione delle equazioni.')

    def __str__(self) -> str:
        return "Chimica Fisica"

    def desc(self):
        return """ La chimica che si occupa di studiare la fisica che sottostà ai diversi eventi chimici """

    class Meta:
        verbose_name = 'Chimica Fisica'
        verbose_name_plural = verbose_name

import sys, inspect

materie = inspect.getmembers(sys.modules[__name__], lambda member: inspect.isclass(member) and member.__module__ == __name__ and member.__name__ != 'Exercise')

def get_modello(nome):
    for materia, modello in materie:
        if materia == nome:
            return modello
    raise Exception("Materia inesistente")