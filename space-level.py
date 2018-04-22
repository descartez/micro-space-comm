from microbit import *



while True:
    x = accelerometer.get_x()
    if 0 >= x <= 512:
        x = 1
    elif 513 >= x <= 1024:
        x = 2
    elif 0 <= x >= -512:
        x = -1
    elif -513 <= x >= -1024:
        x = -2
    else:
        x = 0


    y = accelerometer.get_y()
    if 0 >= y <= 512:
        y = 1
    elif 513 >= y <= 1024:
        y = 2
    elif 0 <= y >= -512:
        y = -1024
    elif -513 <= y >= -1024:
        y = -2
    else:
        y = 0

    display.set_pixel((2+x),(2+y), 9)
    sleep(100)
    display.clear()