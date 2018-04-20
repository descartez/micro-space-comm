from microbit import *
import radio
import music

radio_send1 = Image("00000:"
                    "00000:"
                    "90000:"
                    "00000:"
                    "00000:")
radio_send2 = Image("00000:"
                    "00900:"
                    "90900:"
                    "00900:"
                    "00000:")
radio_send3 = Image("00009:"
                    "00909:"
                    "90909:"
                    "00909:"
                    "00009:")
radio_send = [radio_send1, radio_send2, radio_send3]

radio_menu1 = Image("00000:"
                    "00000:"
                    "00000:"
                    "00000:"
                    "00900:")
radio_menu2 = Image("00000:"
                    "00000:"
                    "09990:"
                    "00000:"
                    "00900:")
radio_menu3 = Image("99999:"
                    "00000:"
                    "09990:"
                    "00000:"
                    "00900:")
radio_menu = [radio_menu1, radio_menu2, radio_menu3]

temp_menu1 = Image("00000:"
                    "00000:"
                    "00000:"
                    "00000:"
                    "00900:")
temp_menu2 = Image("00000:"
                    "00900:"
                    "00900:"
                    "09990:"
                    "00900:")
temp_menu3 = Image("00900:"
                    "00900:"
                    "00900:"
                    "09990:"
                    "00900:")
temp_menu = [temp_menu1, temp_menu2, temp_menu3]

sonic_menu1 = Image("00000:"
                    "00000:"
                    "90000:"
                    "00000:"
                    "00000:")
sonic_menu2 = Image("00000:"
                    "09000:"
                    "90900:"
                    "00000:"
                    "00000:")
sonic_menu3 = Image("00000:"
                    "09000:"
                    "90909:"
                    "00090:"
                    "00000:")
sonic_menu = [sonic_menu1, sonic_menu2, sonic_menu3]

flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]
menu_items = [radio_menu, temp_menu, sonic_menu]
menu_counter = 0

radio.config(channel=7)
radio.config(power=7)
radio.on()
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.clear()
    if button_a.was_pressed():
        if menu_counter < (len(menu_items) - 1):
            menu_counter += 1
        else:
            menu_counter = 0
        display.show(menu_items[menu_counter], delay=200)
    if button_b.was_pressed() and menu_counter == 0:
        display.show(radio_send, delay=100)
        radio.send('send')
    if button_b.was_pressed() and menu_counter == 1:
        temp = temperature()
        display.scroll(str(temp) + 'C')
    if button_b.is_pressed() and menu_counter == 2:
        x = accelerometer.get_x()
        if x < 0:
            x = x * -1
        y = accelerometer.get_y()
        if y < 0:
            y = y * -1
        music.pitch(x, 10)
        music.pitch(y, 10)

    incoming = radio.receive()
    if incoming == 'send':
        display.show(flash, delay=100, wait=False)
        radio.send('receive')
    if incoming == 'receive':
        display.show(flash, delay=100, wait=False)
