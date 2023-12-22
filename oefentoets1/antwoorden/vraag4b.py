def schoeisel_voorstel(weertype):
    if weertype == "zonnig":
        result = "Het is een zonnige dag, trek schoenen aan"
    elif weertype.lower() == "regenachtig":
        result = "Oops! Het is regenachtig, trek laarzen aan"
    else:
        result = f"Geen schoeiselvoorstel voor {weer_vandaag} beschikbaar"
    return result


weer_vandaag = input("Wat is het weer vandaag (Zonnig/Regenachtig):").lower()
print(schoeisel_voorstel(weer_vandaag))
