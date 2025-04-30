from numexpr.expressions import double
def dec_to_bin(number):

    a = str(number).split(".")[0]
    b = str(number).split(".")[1]

    if number == 0:
        return "0"

    sa = ""
    valA = int(a)
    while valA > 0:
        print(f"{valA} / 2 = {valA // 2} Rest {valA % 2}")
        r = valA % 2
        sa = str(r) + sa
        valA = valA // 2

    sa = formatString(sa)
    sa = sa[:-1]
    sa += "."

    if int(b) > 0:
        sb = ""
        r = float("0." + b)
        while r > 0:
            r = r * 2
            sb = str(int(r)) + sb
            r = r % 1.0

        sb = sb[::-1]
    else:
        sb = "0"


    return sa + sb


def formatString(val1):
    while ((len(val1) % 4) != 0):
        val1 = "0" + val1

    counter = 1
    s = ""
    for c in val1:
        s += c

        if counter % 4 == 0:
            s += " "

        counter += 1
    return s

print(dec_to_bin(float(input("Gegebene Zahl: "))))

