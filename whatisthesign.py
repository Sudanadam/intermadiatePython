
from itertools import combinations
import random

sayi_listesi = random.sample(range(1, 100), 10)
islemin_sonucu = 7

listenin_toplami = sum(sayi_listesi)

fark_sayi = (listenin_toplami - islemin_sonucu) / 2

tum_kumeler = []
guzel_kumeler = []


if fark_sayi == 0:
    print(str(sayi_listesi).replace('[', '').replace(']', '').replace(' ', '').replace(',', ' + '), end=" ")
    print("= " + str(islemin_sonucu))
else:
    cikti = ""
    tum_kumeler = []
    for i in range(0, len(sayi_listesi) + 1):
        temp = [list(x) for x in combinations(sayi_listesi, i)]
        if len(temp) > 0:
            tum_kumeler.extend(temp)

    for kumeler in tum_kumeler:
        if sum(kumeler) == fark_sayi:
            guzel_kumeler.append(kumeler)

    print(guzel_kumeler)

    for kume in guzel_kumeler:
        for sayi in sayi_listesi:
            if sayi not in kume:
                cikti = cikti + " + " + str(sayi)
            else:
                cikti = cikti + " - " + str(sayi)
        print(cikti, end=" ")
        print("= " + str(islemin_sonucu))
        cikti = ""
