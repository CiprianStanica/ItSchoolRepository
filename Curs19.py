# class Caine():
#     animal = "caine"
#     def fuge(self):
#         print("Cainele fuge daca arunci batul")
#     def __init__(self,culoare,varsta):
#         self.culoare = culoare
#         self.varsta = varsta
#     def __str__(self):
#         return f"Cainele are culoarea {self.culoare} si varsta de {self.varsta}"

# bison = Caine("maro",5)
# doberman = Caine("negru",7)


# bison.fuge()
# doberman.fuge()

# class Om():
#     def __init__(self):
#         self.nume = input("Nume= ")
#         self.prenume = input("Prenume= ")
#         self.varsta = input("Varsta= ")
#     def salut(self):
#         print(f"Salut! Eu sunt {self.nume} {self.prenume}")
#     def __str__(self):
#         return f"Angajatul lunii este {self.nume}{self.prenume}"

# robert = Om()
# paul = Om()

# robert.salut()
# paul.salut()

# lista = [marin,dan]

# O clasa numita dreptunghi care sa aiba urmatoarele proprietati: lungime,latime
# Creati o functie numita arie care sa afiseze aria dreptunghiului(lungime*latime)
# Creati o functie numita perimetru care afiseaza perimetrul dreptunghiului 2*(lungime+latime)

# class Dreptunghi():
#     def __init__(self,lungime,latime):
#         self.lungime = lungime
#         self.latime = latime
#     def arie(self):
#         print(self.lungime * self.latime)
#     def perimetru(self):
#         print(2*(self.lungime + self.latime))

# dreptunghi = Dreptunghi(20,10)
# dreptunghi.arie()
# dreptunghi.perimetru()

# Creati o clasa numita ContBancar cu atributele balanta, numar_cont
# Creati o metoda depune care adauga bani in cont
# Creati o metoda retrage care retrage bani din cont
# Creati o metoda interogare_sold
import random 
class ContBancar():
    def genereaza_cont(self):
        cont = "ROKSJD7TUD"
        numar = random.randint(1000000000,9999999999)
        return cont + str(numar)
    def __init__(self):
        self.cont = self.genereaza_cont()
        self.balanta = int(input(f"Ce suma doriti sa introduceti in contul {self.cont}?: "))
    def depunere(self,suma):
        self.balanta += suma
    def retragere(self,suma):
        if suma <= self.balanta:
            self.balanta -= suma
    def interogare(self):
        print(f"In contul{self.cont} mai sunt {self.balanta} RON")
contulMeu = ContBancar()
contulMeu.interogare()

        
