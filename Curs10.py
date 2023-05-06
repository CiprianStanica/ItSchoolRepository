# Acesta este cursul 10

# O functie care primeste ca parametri 3 numere si afiseaza maximul dintre acestea(fara for si fara while):
def afiseaza_maxim(a,b,c):
    lista = []
    lista.extend((a,b,c))
    return max(lista)
# print(afiseaza_maxim(1,2,3))

# O functie care calculeaza suma tuturor elementelor dintr-o lista definita inaintea functiei(nu ca parametru):
# lista = [1,2,3,4,5,6,7,8,9]
def suma_elemente():
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma
# print(suma_elemente())

# Aceeasi functie de mai sus dar de data asta transmite lista ca parametru:
def suma_elmente_lista(lista2):
    suma_initiala = 0
    for nr in lista2:
        suma_initiala += nr
    return suma_initiala
# print(suma_elmente_lista(lista))

# O functie care sa inverseze un sir de caractere primit ca parametru si sa il returneze:
def inverseaza_sir_de_caractere(sir):
    return sir[::-1]
# print(inverseaza_sir_de_caractere("anamaria"))

# Scrie o functie care returneaza produsul factorial al unui numar primit ca parametru:(10 factorial = 1*2*3...*10):
def factorial(nr):
    produs = 1
    for i in range(1,nr+1):
        produs = produs * i
    return produs
# print(factorial(6))

# O functie care returneaza elementele pare dintr-o lista:
def elemente_pare(lista):
    for el in lista:
        if el % 2 == 0:
            print(el)
        else:
            pass
    return elemente_pare
# print(elemente_pare(lista))

# O functie care returneaza elementele impare dintr-o lista:
def elemente_impare(lista):
    for el in lista:
        if el % 2 != 0:
            print(el)
        else:
            pass
    return el
# print(elemente_impare(lista))

# O functie care returneaza True atunci cand un numar primit ca parametru se afla in intervalul 3-10 si returneaza False in caz contrat:
def parametru(a):
    if a in range(3,10+1):
        print(True)
    else:
        print(False)
# print(parametru(7))

# O functie care primeste un sir de caractere ca parametru si afiseaza numarul de caractere mari si nr de caractere mici:
def nr_caractere(cuvant):
    mare = 0
    mica = 0
    for caracter in cuvant:
        if (caracter.isupper()):
            mare += 1
        elif (caracter.islower()):
            mica += 1
    print(mare)
    print(mica) 
# print(nr_caractere("AlaBala"))

# O functie care primeste ca parametru un sir de caractere si returneaza doua siruri de caractere:unul cu litere mari, iar altul cu litere mici:
def siruri(sir):
    sir_mare = []
    sir_mic = []
    for caracter in sir:
        if caracter.isupper():
            sir_mare.append(caracter)
        elif caracter.islower():
            sir_mic.append(caracter)
    # print(sir_mic)
    # print(sir_mare)
    return sir_mare , sir_mic
# print(siruri("AlaBalaPortocala"))

# O functie care sa afiseze toate numerele prime dintr-o lista:
lista = [1,2,3,4,5,6,7,8,9,11]
def prime(lista):
    for nr in lista:
        prim = True
        for divizor in range(2,nr):
            if nr % divizor == 0:
                prim = False
        if prim == True:
            print(nr)
# prime(lista)

