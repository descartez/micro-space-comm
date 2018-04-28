from microbit import *

scanning1 = Image("90000:"
                    "00000:"
                    "90000:"
                    "00000:"
                    "90000:")
scanning2 = Image("79000:"
                    "00000:"
                    "79000:"
                    "00000:"
                    "79000:")
scanning3 = Image("57900:"
                    "00000:"
                    "57900:"
                    "00000:"
                    "57900:")
scanning4 = Image("45790:"
                    "00000:"
                    "05790:"
                    "00000:"
                    "05790:")
scanning5 = Image("04579:"
                    "00000:"
                    "04579:"
                    "00000:"
                    "04579:")
scanning6 = Image("00479:"
                    "00009:"
                    "00079:"
                    "00009:"
                    "00479:")
scanning7 = Image("00000:"
                    "00000:"
                    "00000:"
                    "00000:"
                    "00000:")
scanning8 = Image("00000:"
                    "00097:"
                    "00000:"
                    "00097:"
                    "00000:")
scanning9 = Image("00000:"
                    "00975:"
                    "00000:"
                    "00975:"
                    "00000:")
scanning10 = Image("00000:"
                    "09750:"
                    "00000:"
                    "09750:"
                    "00000:")
scanning11 = Image("00000:"
                    "97540:"
                    "00000:"
                    "97540:"
                    "00000:")
scanning12 = Image("90000:"
                    "95400:"
                    "90000:"
                    "95400:"
                    "90000:")

scanning_cycle1 = [scanning1, scanning2, scanning3, scanning4, scanning5, scanning6]
scanning_cycle2 = [scanning7, scanning8, scanning9, scanning10, scanning11, scanning12]

flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

while True:
    if button_a.was_pressed():
        for i in range(0,5,1):
            display.show(scanning_cycle1, delay=50)
            display.show(scanning_cycle2, delay=50)
            display.clear()
