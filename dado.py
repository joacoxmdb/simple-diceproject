import random


valormin = 1
valormax = 6

juegaotravez= "si"

while juegaotravez == "si" or juegaotravez == "s" or juegaotravez == "SI" or juegaotravez == "Si":
    print("Tirando los dados...")
    print("Los dados son...")
    print(random.randint(valormin, valormax))
    print(random.randint(valormin, valormax))
    juegaotravez= input("Tirar de nuevo dados?")
