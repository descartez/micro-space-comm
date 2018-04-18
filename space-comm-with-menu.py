from microbit import *
import radio
menu_items = [Image.HEART_SMALL, Image.HEART, Image.TRIANGLE]
menu_counter = 0
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]
radio.config(channel=7)
radio.config(power=3)
radio.on()
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.clear()
    if button_a.was_pressed():
        if menu_counter < (len(menu_items) - 1):
            menu_counter += 1
        else:
            menu_counter = 0
        display.show(menu_items[menu_counter])
    if button_b.was_pressed() and menu_counter == 0:
        display.show(Image.CLOCK12)
        radio.send('send')
    if button_b.was_pressed() and menu_counter == 1:
        display.show(Image.CLOCK12)
        for i in range(0, 5):
            radio.send('send')
    if button_b.was_pressed() and menu_counter == 2:
        display.show(Image.CLOCK12)
        temp = temperature()
        display.scroll(str(temp) + 'C')
    incoming = radio.receive()
    if incoming == 'send':
        display.show(flash, delay=100, wait=False)
        radio.send('receive')
    if incoming == 'receive':
        display.show(flash, delay=100, wait=False)
