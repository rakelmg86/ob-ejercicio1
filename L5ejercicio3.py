import calendar

#opcion1 calcular año bisiesto
def año_bisiesto(año):
  if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
      return("el año es bisiesto")
  else:
      return("el año no es bisiesto")

print(año_bisiesto(1958))


#opcion2 importando calendar
def esBisiesto(año):
    return calendar.isleap(año)

print(esBisiesto(1958))

