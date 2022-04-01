def numero_primo(numero):
    for n in range(2, numero):
       if numero % n == 0:
           return("No es primo")
       else:
            return("Es primo")

print(numero_primo(5))
