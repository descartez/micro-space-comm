import radio
from microbit import *

# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

radio.config(channel=7)
radio.config(power=3)
radio.on()

while True:
    if button_a.was_pressed():
        radio.send('send')
    if button_b.was_pressed():
        temp = temperature()
        display.scroll(str(temp) + 'C')
    incoming = radio.receive()
    if incoming == 'send':
        display.show(flash, delay=100, wait=False)
        radio.send('receive')
    if incoming == 'receive':
        display.show(flash, delay=100, wait=False)
