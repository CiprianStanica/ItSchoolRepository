# Quiz:
raspunsuri = []
intrebari = [{"intrebare": "Cum se declara un dictionar?",
                      "raspunsuri": "a.{} b.[] c.()",
                      "corect":"a"
                    },
                    {
                        "intrebare": "Cum se defineste o functie?",
                     "raspunsuri" : "a: def functie:  b.def functie():  c.functie()",
                     "corect": "b"
                    },
                    {
                        "intrebare": "CE returneaza urmatoarea operatie: 2+3*2?",
                     "raspunsuri" : "a: 2:  b.3  c.8",
                     "corect": "c"
                    },
                    {
                        "intrebare": "fiind data lista x = [4,2,1,3], ce va afisa x[4]",
                     "raspunsuri" : "a:3  b.2  c.eroare",
                     "corect": "b"
                    },
                    {
                        "intrebare": "Ce face instructiunea elif?",
                     "raspunsuri" : "a:evitam un else si un if  b.e degeaba  c.nu stiu",
                     "corect": "b"
                    }
                    ]
# def afiseaza_intrebare(nr_intrebare):
#     print(intrebari[nr_intrebare].get("intrebare"))
#     print(intrebari[nr_intrebare].get("raspunsuri"))
#     raspuns = input("Introduceti varianta: ")
#     raspunsuri.append(raspuns)

def afiseaza_intrebari():
    for intrebare in intrebari:
        print(intrebare["intrebare"])
        print(intrebare["raspunsuri"])
        raspuns = input("Introduceti varianta: ")
        raspunsuri.append(raspuns)
        print("\n")
    

# def calculeaza_scor_si_reset():
def quiz_meniu():
    print("""
1.Start quiz
2.Next question
3.Show score and reset
4.Exit
    """)
    # for i in range(len(intrebari)):
    #     afiseaza_intrebare(i)

    # SAU

    afiseaza_intrebari()


quiz_meniu()
print(raspunsuri)