def zonnig():
    result = "Het is een zonnige dag, trek schoenen aan"
    return result


def regenachtig():
    result = "Oops! Het is regenachtig, trek laarzen aan"
    return result


weer_vandaag = input("Wat is het weer vandaag (Zonnig/Regenachtig):").lower()
if weer_vandaag == "zonnig":
    print(zonnig())
elif weer_vandaag == "regenachtig":
    print(regenachtig())
else:
    print(f"Geen schoeiselvoorstel voor {weer_vandaag} beschikbaar")
