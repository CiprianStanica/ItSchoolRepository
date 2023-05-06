# O functie care afiseaza suma a doua numere:
def suma_a_doua_numere(a,b):
    return a + b
# print(suma_a_doua_numere(2,6))

# O functie care afiseaza produsul a doua numere:
def produsul_a_doua_numere(a,b):
    return a * b
# print(produsul_a_doua_numere(2,3))

# O functie care afiseaza in ordine crescatoare toate valorile cuprinse intre 2 numere primite de la tastatura:
def afiseaza_interval(a,b):
    a = int(input("Introdu aici primul numar: "))
    b = int(input("Introdu aici al 2 lea numar: "))
    for i in range(a+1,b):
        print(i)
# afiseaza_interval()

# MENIU: cititi 2 numere de la tastatura si intrebati apoi utilizatorul ce functie doreste sa apeleze astfel:
# pentru a afisa suma a doua numere, introduceti cifra 1
# pentru a afisa produsul a doua numere, introduceti cifra 2
# pentru a afisa intervalul, introduceti cifra 3
# pentru a iesi, introduceti cifra 4

def meniu():
    primul_numar = int(input("Introdu primul numar: "))
    al_doilea_numar = int(input("Introdu al doilea numar: "))
    introdu_numar = int(input("""Salut! 
Acesta este meniul:
pentru a afisa suma a doua numere, introduceti cifra 1,
pentru a afisa produsul a doua numere, introduceti cifra 2,
pentru a afisa intervalul, introduceti cifra 3,
pentru a iesi, introduceti cifra 4,
Introdu aici numarul care corespunde cu cerinta ta: """))
    if introdu_numar == 1:
        print(suma_a_doua_numere(primul_numar,al_doilea_numar))
    elif introdu_numar == 2:
        print(produsul_a_doua_numere(primul_numar,al_doilea_numar))   
    elif introdu_numar == 3:
        print(afiseaza_interval(primul_numar,al_doilea_numar))
    elif introdu_numar == 4:  
        print("Multumesc pentru vizita!") 
        breakpoint 
# meniu()

# O functie care citeste de la tastatura 5 elemente de la tastatura si le incarca intr-o lista:
def citite_si_adaugate_in_lista():
    lista = []
    for i in range(5):
        inpu = input("Introdu aici: ")
        lista.append(inpu)
    return lista
# lista =citite_si_adaugate_in_lista()

# O functie care afiseaza fiecare element si pozitia lui. Ex: sir[0] = valoare
def afiseaza_elemente():
    for el in range(len(lista)):
        print(f"pozitia este {el} iar valoarea este {lista[el]}")
# afiseaza_elemente()

# O functie care citeste valori de la tastatura pana se introduce cuvantul "gata"
def citeste_de_la_tastatura():
    while True:
        inp = input("Introdu ceva aici: ")
        if inp.lower() == "gata":
            break
    return
# citeste_de_la_tastatura()

# O functie care afiseaza toate valorile dintr-un sir pana la intalnirea unui numar impar:
# sir = [2,4,6,8,9,1,2,3]
def pana_la_impar(lista):
    for el in lista:
        if el % 2 == 1:
            break
        else:
            print(el)
# print(pana_la_impar(sir))

# O functie care afiseaza toate valorile dintr-un sir pana la intalnirea unui numar impar cu while:
def pana_la_impar_cu_while(ceva):
    index = 0
    while ceva[index] % 2 == 0:
        print(ceva[index])
        index += 1
# pana_la_impar_cu_while(sir)

# O functie care face suma tuturor numerelor dintr-un sir pana la intalnirea unui numar par:
sir = [1,3,5,9,11,22]
def suma_din_sir_pana_la_numar_par(ceva):
    suma = 0
    for el in ceva:
        if el % 2 == 0:
            break
        else:
            suma = suma + el
    print(suma)
# suma_din_sir_pana_la_numar_par(sir)

# O functie care calculeaza suma cifrelor unui numar:

def suma_cifrelor_unui_numar(numar):
    suma = 0
    while numar > 0:
        cifra = numar%10
        suma += cifra
        numar = numar// 10
    return suma
# print(suma_cifrelor_unui_numar(432))

# O functie care verifica daca un string contine doar litere:
def verifica_daca_contine_doar_litere(ceva):
    flag = True
    for el in ceva:
        if el.isalpha() == False:
            flag = False
    return flag 
# print(verifica_daca_contine_doar_litere("alabala"))

# O functie care inregistreaza utilizatorul:
def sign_up():
    username = input("username: ")
    while username.isalpha():
        username = input("username: ")
    return
sign_up()
        




