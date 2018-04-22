from microbit import *

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

while True:
    level_run = False
    if button_a.was_pressed():
        level_run = True

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