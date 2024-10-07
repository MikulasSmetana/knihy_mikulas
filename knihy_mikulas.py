#Přidání knihy
def pridat_knihu(knihy):
    nazev = input("Zadej název knihy: ")
    autor = input(f"Zadej autora knihy {nazev}: ")
    rok = int(input("Zadej rok vydání knihy {nazev}: "))
    
    knihy[nazev] = {"autor": autor, "rok": rok}
    print(f"Kniha {nazev} byla přidána.")


#Najdi knihu



#Hlavní program
def hl_program():
    knihy = {}
    pass