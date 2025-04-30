import math

# Pi wird über die Formel von Ramanujan berechnet:

constant = (2 * math.sqrt(2)) / 9801

term_sum = 0

# Idee: Summe bis unendlich nur bis k=3 laufen lassen
for k in range(3):
    zaehler = math.factorial(4 * k)  # berechnet die Fakultät
    zaehler *= 1103 + 26390 * k
    nenner = math.factorial(k) ** 4 * 396 ** (4 * k)

    term_sum += zaehler / nenner

pi = 1 / (constant * term_sum)

print(pi)