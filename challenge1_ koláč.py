#Collatzovo (koláčovo) domněnka
#1. Zadej libovolné celé číslo N.
#2. Pokud je N sudé, pak ho poděl dvěmi.
#3. Pokud je N liché, pak ho vynásob třemi a přičti k němu 3.
#4. Doměnka zní: nehledě na to, jaké počáteční číslo n je zvoleno – výsledná posloupnost vždy nakonec dojde k číslu 1
#5. Najdi takové číslo N pro které neplatí domněnka a jdi si pro matematické ocenění.

vstup = ""
while not vstup.isnumeric():
    vstup = input("Zadej celé číslo: ")
N = int(vstup)

while N > 1:
    #zde doplň kód
    ...