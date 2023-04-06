import random

# prográmek na básničku kam lze zadávat libolná jména
muzske_jmeno = input("Zadej libovolné mužské jméno: ")
zenske_jmeno = input("Zadej libovolné ženské jméno: ")

vers_muz = f"{muzske_jmeno} v lese dřevo seká"
print(vers_muz)

vers_zena = f"{zenske_jmeno} na něj doma čeká"
print(vers_zena)

vers_zena = f"{zenske_jmeno} z okna vyhlíží"
print(vers_zena)

sentimenty = ["pozitivní", "negativní", "neutrální"]
verse = {
    "pozitivní": [
        "vždyť trochu slunka neublíží",
        "lidé jsou již bez obtíží",
        "smutek ho již netíží"
    ],
    "negativní": [
        "smrt se k ní blíží",
        "k Husákovi děti vzhlíží",
        "je doba plná potíží"
    ],
    "neutrální": [
        "svět je pln mříží",
        "v hlavě se mi neurony kříží",
        "měsíc si mě prohlíží"
    ]
}
nahodny_sentiment = random.choice(sentimenty)
nahodny_vers = random.choice(verse[nahodny_sentiment])
vers_muz = f"{nahodny_vers}"    #dopiš verš :-)
print(vers_muz)


