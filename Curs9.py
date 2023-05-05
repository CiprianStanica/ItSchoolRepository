#Cursul 9. Despre functii

# def f(x):
#     variabila = x + 2
#     print(variabila)
# for i in range(10):
#     print(i)
#     f(i)
#     print("_________")
     
# def aduna(x,y):
#     print(x + y)
# aduna(2,32)

# O functie care face media aritmetica a unei liste:
# lista = [2,4,6,1,3,5,7,10]
# alta_lista = [2,4,6,8,23,4235,77,23434,1123]
# def media_aritmetica(tava):
#     suma = 0
#     for nr in tava:
#         suma = suma + nr / len(lista)
#     print(suma)
# media_aritmetica(lista)
# media_aritmetica(alta_lista)

# O functie care face suma unei liste:
# numere = [1,2,3,4,5,6,7,8,9,10]
# def suma_unei_liste(lista):
#     suma = 0
#     for nr in lista:
#         suma = suma + nr
#     print(suma)
# suma_unei_liste(numere)

# # Rescrie functia media_aritmetica folosindu-te de functia suma_unei_liste:
# numere = [1,2,3,4,5,6,7,8]

# def suma_unei_liste(lista):
#     suma = 0
#     for nr in lista:
#         suma += nr
#     return suma
# suma_unei_liste(numere)

# def media_aritmetica(lista):
#     suma = suma_unei_liste(lista) 
#     medie = suma/len(lista)
#     return medie
# media_aritmetica(numere)

# # Scrieti o functie care sa afiseze toate numerele de la 0 la 9
# def afisare_numere(numere):
#     for nr in range(numere):
#         print(nr)
# afisare_numere(10)

# # Functie care incrementeaza un numar:
# def incrementreaza(nr):
#     suma = 19
#     suma = suma + nr
#     print(suma)
# incrementreaza(20)

# # O functie care calculeaza elementele impare dintr-o lista:
# lista = [1,2,3,4,5,6,7,8,9]
# def suma_numere_impare(ceva):
#     nr_cifre_impare = 0
#     for nr in ceva:
#         if nr % 2 != 0:
#             nr_cifre_impare += 1
#     print (nr_cifre_impare)
# suma_numere_impare(lista)

# # O functie care afiseaza ultima litera a fiecarui sir de caractere dintr-o lista:
# lista_cuvinte = ["cand" , "rasare" , "soarele" , "ies" , "pe" , "s"]
# def ultima_litera(ceva):
#      for cuvant in ceva:
#           print(cuvant[-1])
# ultima_litera(lista_cuvinte)

# # O functie care returneaza ultima cifra a unui numar:
# numar = "12345"
# def ultima_cifra_a_unui_numar(ceva):
#     print(ceva[-1])
# ultima_cifra_a_unui_numar(numar)

# sau

# def ultima_cifra_a_unui_numar(nr):
#     return nr %10
# # ultima_cifra_a_unui_numar(20)

# # O functie care taie ultima cifra a unui numar:
# def taie_ultima_cifra(nr):
#     return nr // 10
# # print(taie_ultima_cifra(123))

# # O functie care, folosind ultima_cifra si taie_ultima_cifra sa scrie numarul in ordine inversa:
# def inverseaza_numar(nr):
#     invers = ""
#     while nr>0:
#         ult_cifra = ultima_cifra_a_unui_numar(nr)
#         nr = taie_ultima_cifra(nr)
#         invers += str(ult_cifra)
#     return invers
# # inverseaza_numar(12345)

# # O functie care verifica daca un numar se citeste la fel de la cap la coada:
# def verifica_citire_inversa(nr):
#     invers = inverseaza_numar(nr)
#     if nr != invers:
#         print(False)
#     else:
#         print(True)
# # verifica_citire_inversa(101)

# # O functie care face inmultirea a 2 numere:
# def inmultire(x,y):
#     return x * y
# # print(inmultire(2,3))

# # O functie care calculeaza puterea unui numar x folosind functia de inmultire de mai sus
# def putere(baza,exponent):
#     putere = baza
#     for i in range(exponent - 1):
#         putere = inmultire(putere,baza)
#     return putere
# # print(putere(2,5))

# # Variabile globale:
# nr = 100
# def mareste_numar(n):
#     global nr
#     nr = nr + n
# # mareste_numar(10)
# # mareste_numar(100)
# # print(nr)

# def mareste(x,y):
#     x = x + y
#     return x
# # print(mareste)

# # O functie care verifica daca un numar este prin
# def prim(nr):
#     flag = 0
#     for i in range(2,(nr//2 + 1)):
#         if nr % i == 0:
#             flag = 1
#     if flag == 1:
#         print("Nu este prim")
#     else:
#         print("Este prim")
# # prim(11)

# # O functie care afiseaza numarul de elemnte prime din lista:
# def eprim(nr):
#     flag = 0
#     for i in range(2,nr//2 + 1):
#         if nr % i == 0:
#             flag == 1
#     if flag == 1:
#         return True
#     else:
#         return False
# # print(eprim(12))

# def numere_prime(listadesus):
#     nrPrime = 0
#     for i in listadesus:
#         if (eprim(i)) :
#             nrPrime += 1
#     print(nrPrime)
# lista = [2,3,4,5,6,7,8,9,11]
# # numere_prime(lista)

# print(eprim(11))
        
# # O functie care primeste 2 siruri de caractere ca parametru si le concateneaza:
# def concateneaza(a,b):
#     return a + b
# print(concateneaza("nume ","prenume"))

# O functie care eleminia duplicate dintr-o lista:

# def elimina_duplicate(sir):
#     frecvente = {}
#     for el in sir:
#         if frecvente.get(el) != None:
#             frecvente[el] += 1
#         else:
#             frecvente[el] = 1
#     lista = []
#     for cheie in frecvente:
#         if frecvente[cheie] == 1:
#             lista.append(cheie)
#         print(cheie)

# lista = ["dan" , "maria" , "razvan" , "dan" , "maria" , "maria"]
            
# elimina_duplicate(lista)

# O functie care fiind dat un numar n returneaza 1*2*3*....*n:
def factorial(n):
    produs = 1
    for i in range(1, n+1):
        produs = produs*i 
    return produs
print(factorial(6))