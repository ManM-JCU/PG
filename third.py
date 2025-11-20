cislo = int(input("Zadej číslo: "))

 

# funkce pro test prvočísla

def je_prvocislo(n):

    if n <= 1:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True

 

# výsledek

if je_prvocislo(cislo):

    print("prvočíslo = True")

else:

    print("prvočíslo = False")

# Fuknce pro vytvoření seznamu prvočísel

def vrat_prvocislo(maximum):
    maximum = int(maximum)
    results = []
    for i in range(1, maximum+1):
        if je_prvocislo(i):
            results.append(i)
    return results

# Výsledek seznam

seznam = vrat_prvocislo(cislo)
print(f"Prvočísla mezi 1 a {cislo}:")
print(seznam)

