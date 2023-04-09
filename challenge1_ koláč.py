#Collatzovo (koláčovo) domněnka
#1. Zadej libovolné celé číslo N.
#2. Pokud je N sudé, pak ho poděl dvěmi.
#3. Pokud je N liché, pak ho vynásob třemi a přičti k němu 3.
#4. Doměnka zní: nehledě na to, jaké počáteční číslo n je zvoleno – výsledná posloupnost vždy nakonec dojde k číslu 1
#5. Najdi takové číslo N pro které neplatí domněnka a jdi si pro matematické ocenění.

vstup = ""      #Inicializuje řetězec vstup na prázdný řetězec
while not vstup.isnumeric():       #Spustí smyčku, která bude pokračovat, dokud nebude vstup číslo
    vstup = input("Zadej celé číslo: ")     #uživatel zadá číslo a uloží se do proměnné vstup
N = int(vstup)      #Převede vstup na celé číslo a uložíte do proměnné N

krok = 0  # Inicializuje proměnnou krok na 0 
while N > 1:     #Spustí smyčku, která bude pokračovat, dokud nebude N rovno nebo menší než 1.
    for krok, _ in enumerate(range(N)):    #zahajuje cyklus for uvnitř cyklu while, fce enumerate() společně s range(N) pro získání indexu (krok) a hodnoty prvků (ignoruje pomocí podtržítka _)
        if N % 2 == 0:     #kontroluje, zda N sudé, pokud ano, pak provede následující blok kódu 
            N = N // 2     # pokud N sudé, podělí dvěma
        else:
            N = 3 * N + 3    # pokud N liché, vynásobího 3 a přičte 3
        print(f"Krok {krok + 1}: {N}")      # zobrazí číslo aktuálního kroku a novou hodnotu N a přidá 1 k hodnotě krok, aby začínalo od 1
        if N <= 1:    # jestli N dosáhlo hodnoty 1 nebo menší
            break  # pokud N dosáhne hodnoty 1 nebo menší ukončí cyklus for 

print(f"Koláčkova domněnka byla potvrzena po {krok + 1} krocích.")


#Kód opakuje proces dělení sudých čísel 2 a násobení lichých čísel 3 a přičítání 3, dokud N nedosáhne hodnoty 1 nebo menší a sleduje počet kroků a vypisuje každý krok s aktualizovanou hodnotou N        