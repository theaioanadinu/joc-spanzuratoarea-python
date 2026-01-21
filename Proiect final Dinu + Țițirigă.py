import random
import sys


def obtine_cuvinte_pe_categorii():
    return {
        "1": {
            "nume": "Animale",
            "lista": [
                "elefant", "girafa", "caine", "pisica", "tigru", "vultur", "delfin",
                "hipopotam", "crocodil", "cangur", "rinocer", "veverita", "leopard",
                "maimuta", "zebra", "urs", "lup", "vulpe", "papagal", "rechin"
            ]
        },
        "2": {
            "nume": "Tari",
            "lista": [
                "romania", "franta", "germania", "japonia", "brazilia", "canada", "egipt",
                "italia", "spania", "australia", "argentina", "portugalia", "mexic",
                "china", "grecia", "turcia", "rusia", "suedia", "norvegia", "india"
            ]
        },
        "3": {
            "nume": "IT & Tech",
            "lista": [
                "python", "tastatura", "internet", "programare", "monitor", "laptop", "server",
                "procesor", "memorie", "aplicatie", "algoritm", "retea", "sistem",
                "router", "mouse", "cablu", "baterie", "cod", "proiect", "digital"
            ]
        }
    }


def alege_cuvant_din_categorie():
    categorii = obtine_cuvinte_pe_categorii()

    while True:
        print("\nAlege o categorie:")
        for cheie, valoare in categorii.items():
            print(f"{cheie}. {valoare['nume']}")

        optiune = input("Introdu numărul categoriei dorite: ").strip()

        if optiune in categorii:
            print(f"Ai ales categoria: {categorii[optiune]['nume']}")
            lista_selectata = categorii[optiune]["lista"]
            return random.choice(lista_selectata).upper()
        else:
            print("Opțiune invalidă. Te rog alege 1, 2 sau 3.")


def afiseaza_spanzuratoarea(incercari):
    stadii = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stadii[incercari]


def joaca_o_runda():
    cuvant = alege_cuvant_din_categorie()
    litere_cuvant = set(cuvant)
    alfabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    litere_ghicite = set()

    incercari = 6

    print("\n--- ÎNCEPE RUNDA ---")

    while len(litere_cuvant) > 0 and incercari > 0:
        print(afiseaza_spanzuratoarea(incercari))

        lista_cuvant = [litera if litera in litere_ghicite else '_' for litera in cuvant]
        print("Cuvânt: ", ' '.join(lista_cuvant))
        print(f"Încercări rămase: {incercari}")
        print("Litere încercate: ", ' '.join(sorted(litere_ghicite)))

        litera_utilizator = input("Introdu o literă: ").upper()

        if litera_utilizator in alfabet - litere_ghicite:
            litere_ghicite.add(litera_utilizator)
            if litera_utilizator in litere_cuvant:
                litere_cuvant.remove(litera_utilizator)
                print(f"> Super! {litera_utilizator} este corect.")
            else:
                incercari -= 1
                print(f"> Ghinion! {litera_utilizator} nu este în cuvânt.")

        elif litera_utilizator in litere_ghicite:
            print(f"> Ai mai spus litera {litera_utilizator} odată.")

        else:
            print("> Caracter invalid.")

        print("-" * 25)

    if incercari == 0:
        print(afiseaza_spanzuratoarea(incercari))
        print(f"JOC TERMINAT! Ai pierdut. Cuvântul era: {cuvant}")
    else:
        print(f"VICTORIE! Ai ghicit cuvântul: {cuvant}")


def main():
    print("BINE AI VENIT LA SPÂNZURĂTOAREA 2.0!")
    while True:
        joaca_o_runda()

        raspuns = input("\nVrei să joci din nou? (da/nu): ").lower().strip()
        if raspuns not in ["da", "d", "y", "yes"]:
            print("La revedere! Mulțumim că ai jucat.")
            break


if __name__ == '__main__':
    main()