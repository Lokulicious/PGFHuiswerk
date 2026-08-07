# Week 1 - Casino de Gouden Driehoek: startbudget en persoonsgegevens

## Inleiding
Tijdens deze cursus ga je werken aan een doorlopende opdracht. Dat betekent dat je elke week een stukje maakt, aanpast, toevoegt, of verwijdert. Hiermee bouw je een applicatie waarmee je de eisen van de eindopdracht (bijna) zou kunnen halen en heb je dus eigenlijk een soort van "handleiding" voor je eindopdracht. 

In deze eerste oefening ga je aan de slag met de eerste versie van **Casino de Gouden Driehoek**. Je bouwt een kleine, interactieve budgetcheck waarmee een speler kan zien of er genoeg geld is om een eerste avondje casino te starten. Daarnaast vul je meteen persoonsgegevens in, zodat het casino de speler persoonlijk kan aanspreken.

## Opdracht beschrijving

### Persoonsgegevens
Maak een programma dat de start van een casinobezoek verwerkt.  
De speler vult eerst wat persoonsgegevens in: 
- naam 
- geboortedatum
- geslacht

### Naam
Zorg dat de naam van de gebruiker altijd met een hoofdletter begint. Optioneel mag je dit ook splitsen in voornaam en achternaam, waardoor je kunt kiezen om de begroeting op alleen de achternaam te doen of voornaam + achternaam.

### Geboortedatum
Zorg ervoor dat de speler weet dat de geboortedatum moet worden ingevoerd in het format `dd-mm-yyyy`. Je hoeft dit (nog) niet af te dwingen in je code, maar het moet al wel duidelijk zijn voor de gebruiker.

### Geslacht
Je gebruikt de geslacht-waarde om in de output automatisch te kiezen tussen bijvoorbeeld `meneer {naam}` en `mevrouw {naam}`. Als de speler niet in die twee categorieën valt, mag je een neutrale aanspreekvorm gebruiken.

### Startbudget
Vervolgens geeft de speler diens startbudget op. Maak duidelijk naar de gebruiker dat het hier gaat om een bedrag in euro's. Sla de uitkomst op als een `float`.

### Vaste kosten
Naast het budget van de gebruiker, sla je ook drie vaste casino-kosten op. Dit zijn kosten die de gebruiker moet betalen om van de casino-applicatie gebruik te kunnen maken. Je mag zelf kiezen welke dat zijn. Heb je geen idee, dan is hier een suggestie:
- De prijs voor een toegangsticket
- De prijs voor een (verplicht) drankje
- De prijs voor een gok belasting 

### Berekening
Uiteindelijk rekent het programma uit hoeveel er bij elkaar wordt uitgegeven aan vaste kosten en laat zien of het budget toereikend is.

Je output zal er ongeveer zo uitzien:

```text
Casino de Gouden Driehoek
-------------------------
Welkom, meneer Jansen

Startbudget:    € 50.00
Vaste kosten:   € 16.50
Saldo:          € 33.50

Je hebt nog genoeg budget voor toegang tot het casino.
```
De laatste regel, die aangeeft of je budget toereikend is of niet, wordt dynamisch bepaald op dezelfde manier als de "begroeting".

## Randvoorwaarden
- De code voor deze applicatie staat geschreven in `main.py`.
- De applicatie bevat ten minste 4 variabelen die je van de gebruiker opvraagt.
- De applicatie bevat ten minste 3 constanten met een float waarde (euro).
- Je gebruikt de geslacht-waarde om programmatisch de aanspreekvorm te kiezen, bijvoorbeeld `meneer {name}` of `mevrouw {name}`. Je mag hier ook een non-binaire optie toevoegen.
- Je laat de persoonsgegevens, de losse kosten, het totaal, het resterende bedrag en een conclusie zien in een goed vormgegeven printout.
- Je gebruikt minimaal 1 f-string en minimaal 2 conditionele statements.

## Stappenplan

Let op: het is uitdagender om jouw eigen stappenplan te maken. Als je niet zo goed weet waar je moet beginnen, kun je onderstaand stappenplan gebruiken:

1. Begin met het thema Casino de Gouden Driehoek door een `main.py` bestand aan te maken waarin je jouw eerste Python code gaat schrijven.
2. Vraag met `input()` de naam, geboortedatum en geslacht van de speler op. Maak voor elk van deze datastukken een variabele met een passende, Engelse naam. Let erop dat je tussen de haakjes van `input()` een goede prompt invult, zodat de gebruiker weet wat er gevraagd wordt. Voor `birthdate` geef je bijvoorbeeld een prompt als `input("Wat is je geboortedatum? (dd-mm-yyyy) ")`.
3. Doe hetzelfde voor het startbudget van de speler en zet deze om naar een getal met de `float()` functie.
4. Gebruik de geslacht-waarde in een conditionele expressie (if/else) om een aanspreekvorm te kiezen, bijvoorbeeld `meneer {naam}` als het geslacht `m` is of `mevrouw {naam}` als het geslacht `v` is. Sla de gekozen aanspreekvorm op in een variabele.
5. Bepaal welke drie vaste kosten je wilt gebruiken, of kies de voorbeeld suggesties. Maak voor de drie casinokosten aparte variabelen. Zet deze variabelen op de juiste plek in je script en geef ze een Engelse naam in hoofdletters.
6. Tel de drie kosten bij elkaar op in een nieuwe variabele.
7. Bereken hoeveel geld er overblijft door het totaal van het budget af te trekken.
8. Vergelijk of het totaal kleiner is dan of gelijk is aan het budget.
9. Gebruik een conditionele expressie om te bepalen welke conclusie je aan de gebruiker laat zien, bijvoorbeeld `Je hebt nog genoeg budget voor toegang tot het casino.` of `Je hebt niet voldoende budget voor toegang tot het casino.`.
10. Print daarna de naam van het casino, de persoonlijke begroeting, het budget, de totale kosten, het resterende saldo en de conclusie. Print dit alles in een gestylede printout, door gebruik te maken van witruimtes en speciale tekens zoals `€` en `-`.


## Bonus
- Zorg dat de bedragen netjes met twee cijfers achter de komma worden getoond. Zoek op het internet hoe je dat kunt afdwingen in een f-string.
