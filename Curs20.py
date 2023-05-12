# class and subclass

# O clasa dreptunghi si o clasa patrat. Clasa patrat sa mosteneasca clasa dreptunghi. Patrat va avea in plus o valoare booleana = True

class Dreptunghi():
    def __init__(self,lungime,latime):
        self.lungime = lungime
        self.latime = latime
    

class Patrat(Dreptunghi):
    def __init__(self,latura):
        super().__init__(latura,latura)
        self.patrat = True

# forma = Dreptunghi(1,2)

# O clasa Avion. Din clasa Avion, creati 2 clase:
# -Avion militar
# -Avion civil
# Atat avionul militar cat si cel civil au urmatoarele proprietati:
# -Ambele zboara
# -Aambele au viteza minima de zbor
# -Ambele au un consum de combustibil

# -Avionul civil are un numar de pasageri
# -Avionul descarca bagaje

# -Avionul militar poate lansa rachete in timp ce zboara(suprascriere)
# -Avionul militar are cantitate munitie(in tone)

# class Avion():
#     def __init__(self,viteza_minima,consum_combustibil):
#         self.zboara = True
#         self.viteza_minima = 100
#         self.consum_combustibil = True

# class Avion_Civil(Avion):
#     def __init__(self):
#         self.numar_pasageri = 250
#         self.descarca_bagajele = True

# class Avion_Militar(Avion):
#     def __init__(self):
#         super().__init__(self)
#         self.lanseaza_rachete = True
#         self.munitie = 300

# F15 = Avion_Militar()
# print(F15.viteza_minima())
PATH = "Curs20/"
import csv
class Fisier():
    def __init__(self,nume,dimensiune,tip,cale):
        self.nume = nume
        self.dimensiune = dimensiune
        self.tip = tip
        self.cale = cale
class FisierCsv(Fisier):
    def __init__(self,nume,dimensiune,tip,cale):
        super().__init__(nume,dimensiune,tip,cale)
        self.coloane = 0
        self.randuri = 0
    def citire_fisier(self):
        with open(PATH+self.cale,"r") as file:
            reader = csv.reader(file)
            continut = csv.load(reader)
            for line in continut:
                print(line)
