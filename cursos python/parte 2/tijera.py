import time
from time import sleep
import random

sus = "-" * 35
depo = ["piedra", "papel", "tijera"]
while True:
    x = raw_input("Que elijes? Piedra, Papel, o tijera : ")
    if x not in depo:
        print("No hagas Trampa!!!")
        continue

    pc = random.choice(depo)
    sleep(0.5)
    print(("Computadora elijio {}.").format(pc))
    if x == pc:
        print("\nEmpate.")
    elif x == "piedra" and pc == "tijera":
        print ("\n Ganaste")
    elif x == "papel" and pc == "piedra":
        print ("\n Ganaste")
    elif x == "tijera" and pc == "papel":
        print ("\n Ganaste")
    else:
        print ("Perdimos. {} gana {} \n{}".format(pc,x))
    print(sus)
