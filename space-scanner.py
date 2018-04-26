from microbit import *
import radio

sensitivity_icon1 = Image("00000:"
                     "00000:"
                     "00000:"
                     "00000:"
                     "90000:")

sensitivity_icon2 = Image("00000:"
                     "00000:"
                     "00000:"
                     "09000:"
                     "99000:")

sensitivity_icon3 = Image("00000:"
                     "00000:"
                     "00900:"
                     "09900:"
                     "99900:")

sensitivity_icon4 = Image("00000:"
                     "00090:"
                     "00990:"
                     "09990:"
                     "99990:")

sensitivity_icon5 = Image("00009:"
                     "00099:"
                     "00999:"
                     "09999:"
                     "99999:")
sensitivity_icons = [sensitivity_icon1, sensitivity_icon2, sensitivity_icon3, sensitivity_icon4, sensitivity_icon5]
sensitivities = [500, 400, 300, 200, 100]
sensitivity_counter = 0

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
    level_run = False
    scanning = False
    if button_a.was_pressed():
        level_run = True

    if button_b.was_pressed():
        scanning = True

    while level_run:
        x = int(round(accelerometer.get_x(), 0)) // sensitivities[sensitivity_counter]
        if x < -2:
            x = -2
        elif x > 2:
            x = 2
        z = int(round(accelerometer.get_z(), 0)) // sensitivities[sensitivity_counter]
        if z < -2:
            z = -2
        elif z > 2:
            z = 2
        # "home" is pixel [2,2]
        display.set_pixel((x+2), (z+2), 9)

        # if "home" is hit, show crosshairs
        if display.get_pixel(2, 2) == 9:
            display.set_pixel(1, 2, 9)
            display.set_pixel(2, 3, 9)
            display.set_pixel(3, 2, 9)
            display.set_pixel(2, 1, 9)

        sleep(100)
        display.clear()
        if button_a.was_pressed():
            level_run = False

        if button_b.was_pressed():
            display.show(sensitivity_icons[sensitivity_counter])
            sleep(200)
            display.clear()
            if button_b.was_pressed():
                if (sensitivity_counter + 1) > 4:
                    sensitivity_counter = 0
                else:
                    sensitivity_counter += 1
                display.show(sensitivity_icons[sensitivity_counter])
                sleep(200)
                display.clear()

    while scanning:
        radio.config(channel=7)
        radio.config(power=7)
        radio.on()

        if button_a.was_pressed():
            scanning = False

        incoming = radio.receive()
        if incoming == 'send':
            display.show(flash, delay=100, wait=False)
            radio.send('receive')
        if incoming == 'receive':
            display.show(flash, delay=100, wait=False)

        display.show(scanning_cycle1, delay=100)
        radio.send('send')
        display.show(scanning_cycle2, delay=100)
        display.clear()
