import math

cyp = list(str(input("Text to decode: ")))

alphabet = list("abcdefghijklmnopqrstuvwxyz")

# alternates aaaaaa = zbycxd

plain = ""
n = 0
for i in range(len(cyp)):
    try:
        letterIndex = alphabet.index(cyp[i])
    except:
        plain += cyp[i]
        continue
    shift = math.ceil((n+1)/2)
    print(shift)
    if n%2 == 0: #left!
        print(alphabet[(letterIndex - shift)%26])
        plain += alphabet[(letterIndex - shift)%26]
    elif n%2 == 1: #right!
        print(alphabet[(letterIndex + shift)%26])
        plain += alphabet[(letterIndex + shift)%26]
    n += 1

print(plain)
# j krth stp xjyizhagbfce yjou. lai'cu cfygx vwis vtz ducc s bme auhh.
