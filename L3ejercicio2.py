
print("**Calculadora masa corporal**\n")

peso = float (input("Introduce tu peso en kg: "))
estatura = float (input("Introduce tu estatura en metros: "))
imc = peso / estatura **2
print(f"Tu indice de masa corporal es de : {round(imc, 2)}")
      
