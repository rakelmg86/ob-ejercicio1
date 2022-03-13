ni = int(input("Introduce un numero inicial: "))
nf = int(input("Introduce un numero final: "))

for n in range(ni,nf):
    if n % 2 != 0:
         print(n, end=" ")
