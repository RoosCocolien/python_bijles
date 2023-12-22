# Oefentoets 1

## Vraag 1

Schrijf een python-programma (verkeerslicht) dat controleert op de volgende voorwaarden:  

- Als het licht groen is, mag de auto doorrijden
- Als het licht oranje is, moet de auto stoppen
- Als het licht rood is, moet de auto stoppen
- Bij een andere input: geef een foutmelding

Tips:
- vraag de gebruiker welke kleur het verkeerslicht heeft
- gebruik een while loop in combinatie met if/else statement
- sla de toegestane kleuren op in een lijst

Voorbeeld:
```
Welke kleur heeft het verkeerslicht?: rood
Stop de auto
Welke kleur heeft het verkeerslicht?: geel
Stop de auto
Welke kleur heeft het verkeerslicht?: groen
Je mag doorrijden
Welke kleur heeft het verkeerslicht?: blauw
Deze kleur herken ik niet
```

## Vraag 2
Schrijf een Python-programma om te controleren of een string een palindroom is of niet.  
Laat de gebruiker een woord invoeren.
Hoofd- en kleine letters zijn hetzelfde.

Een palindroom is een woord, zin of reeks die achterwaarts hetzelfde leest als voorwaarts, bijvoorbeeld:  
reinier, redder, droommoord, racecar, legovogel, nedertreden, meetsysteem, kok, lepel, level

Extra:
- Maak een functie die True of False returned
- Voeg een while loop toe zodat de gebruiker om een woord wordt gevraagd totdat de gebruiker 'stop' of 'exit' invoert

## Vraag 3
Schrijf een functie (```is_schrikkeljaar()```) die 1 parameter accepteert (jaartal). De functie moet controleren of het ingevoerde jaartal een schrikkeljaar is of niet.  
Extra:
- De functie geeft True of False terug.
- Voeg een while loop toe die de gebruiker jaartallen blijft vragen tot de gebruiker 'stop' of 'exit' invoert.

Schrikkeljaar regels:
- Een jaartal dat deelbaar is door 4, maar niet door 100, is een schrikkeljaar
- Het jaartal is ook een schrikkeljaar als het deelbaar is door 400
- Andere jaartallen deelbaar door 100 zijn gewone jaren

Voorbeelden:
```
Geef een jaartal: 2016
2016 is een schrikkeljaar

Geef een jaartal: 2017
2017 is niet een schrikkeljaar

Geef een jaartal: 1600
1600 is een schrikkeljaar
```

## Vraag 4
Schrijf een programma dat op basis van het weer schoeisel voorstelt. Vraag de gebruiker naar het weer buiten met twee opties: zonnig of regenachtig.

Geef daarna een schoeisel suggestie (schoenen of laarzen).

Maak gebruik van een functie.

Voorbeelden:
```
Wat is het weer vandaag (zonnig/regenachtig): zonnig
Het is een zonnige dag, trek schoenen aan

Wat is het weer vandaag (zonnig/regenachtig): regenachtig
Oeps! Het is regenachtig, trek laarzen aan
```

## Vraag 5
Schrijf een programma dat de gebruiker om twee getallen vraagt.  
Vraag vervolgens welke bewerking gedaan moet worden: optellen, aftrekken, delen, of vermenigvuldigen.
Voer de gekozen bewerking uit op de getallen. Toon niet alleen het antwoord, maar ook de bewerking.

Schrijf vier functies, 1 voor elke wiskundige bewerking:
```
optellen()
aftrekken()
vermenigvuldigen()
delen()
```

## Vraag 6
Schrijf een programma dat een woord van de gebruiker accepteert en het omdraait.

```
Geef een woord die je om wilt draaien: Het is vandaag vrijdag
gadjirv gaadnav si teH
```

## Vraag 7
Schrijf een Python-programma dat over de gehele getallen van 1 tot 50 itereert.

Voor veelvouden van 3 print je "Fizz" in plaats van het getal.
Voor veelvouden van 5 print je "Buzz" in plaats van het getal.
Voor nummers die veelvouden zijn van zowel drie als vijf, print je "FizzBuzz" af.
