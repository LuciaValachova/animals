# Modul: zadanie_zvierata.py
# Autor: Lucia Valachová
# Dňa: 20.10.2019
# Funkcia modulu : Na pokyn počítača sa zadá 5 zvierat cez vstup z klávesnice (pomocou cyklu while).
#                  Výstupný zoznam (výpis cyklom for) nebude obsahovať tie isté zvieratá(ošetrené podmienkou if...else).
############################################################################################

zoznam = []
poradie = 0
n = pocet_zvierat = 0

while poradie != 5 and n != 5:
 zviera = input("Napíš "  + str(poradie+1) + ".zviera: ")
 zviera = zviera.split()
 for retazec in zviera:
   if not retazec in zoznam:
      zoznam.append(retazec)
   else: 
     zviera = input("\nNapíš iné "  + str(poradie+1) + ".zviera, toto je už v zozname: ")
     zviera = zviera.split()
     for retazec in zviera:
      if not retazec in zoznam:
        zoznam.append(retazec)
 poradie = poradie + 1
n = n + 1
print("\nVšetky zvieratá sa uložili do zoznamu: ")
for vypis in zoznam:
  print(vypis, end=', ')
print("\n")