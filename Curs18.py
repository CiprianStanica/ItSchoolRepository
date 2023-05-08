# Curs 18 

# O functie care sa citeasca de la tastatura un numar si incearca sa scada 2 din el. In cazul in care utilizatorul nu introduce numar, afiseaza eroare. 
def citeste_de_la_tastatura_si_afiseaza_eroare():
    inp = int(input("Introdu aici numarul tau: "))
    rezultat = inp - 2
    return rezultat
# print(citeste_de_la_tastatura_si_afiseaza_eroare())

# O functie care citeste de la tastaturs 2 numere si calculeaza a/b.  Verificati ca nu crapa in cazul in care al doilea numar este 0
def verifica_daca_nu_crapa():
    primul_numar = int(input("Primul numar: "))
    al_doilea_numar = int(input("Al doilea numar: "))
    calcul = primul_numar/al_doilea_numar
    return calcul
# print(verifica_daca_nu_crapa())

# O functie care citeste un numar `n` de la tastatura si afiseaza al n-lea element din lista: [2,4,1,4,2]. Verificati cazul in care indexul nu exista
def index_inexistent():
    lista = [2,4,1,4,2]
    inp = int(input("Introdu aici numarul: "))
    return lista[inp]
# print(index_inexistent())

# O functie in care citeste un string de la tastatura si afiseaza lungimea lui. Tratati cazul in care textul nu este string
def citeste_string():
    inp = input("Introdu aici: ")
    return len(inp)
# print(citeste_string())

# Fiind dat un dictionar, {"a":1,"b":2,"c":3}, scrie o functie care primeste ca parametru cheia si returneaza valoarea
dict = {
    "a":1,
    "b":2,
    "c":3
}
def primeste_cheie_returneaza_valoare(a):
    valoare = dict.get(a)
    return valoare
print(primeste_cheie_returneaza_valoare("b"))