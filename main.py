from machine import Pin, PWM # type: ignore
import _thread
import time

thread_run = 0
process_count = 0

#====== led pins ======
led_all = Pin(2, Pin.OUT)
led_blue = Pin(4, Pin.OUT)
led_green = Pin(17, Pin.OUT)
led_red = Pin(18, Pin.OUT)
led_white = Pin(16, Pin.OUT)

#====== buttons ======
button_red = Pin(19, Pin.IN, Pin.PULL_UP)
button_green = Pin(21, Pin.IN, Pin.PULL_UP)
button_blue = Pin(23, Pin.IN, Pin.PULL_UP)
button_white = Pin(22, Pin.IN, Pin.PULL_UP)
button_disko = Pin(5, Pin.IN, Pin.PULL_UP)

#====== on start status ======
led_all.value(1)
led_blue.value(1)
led_green.value(1)
led_red.value(1)
led_white.value(0)

def on_color(color):
    if color == 'red':
        led_red.value(0)
    if color == 'green':
        led_green.value(0)
    if color == 'blue':
       led_blue.value(0)
    if color == 'white':
        led_white.value(1)

def off_all():
    led_blue.value(1)
    led_green.value(1)
    led_red.value(1)
    led_white.value(0)

def check_buttons():
    try:
        global thread_run
    except:
        pass
    if button_red.value() == 0:
        thread_run = 0
        off_all()
        on_color('red')
    if button_green.value() == 0:
        thread_run = 0
        off_all()
        on_color('green')
    if button_blue.value() == 0:
        thread_run = 0
        off_all()
        on_color('blue')
    if button_white.value() == 0:
        thread_run = 0
        off_all()
        on_color('white')
    if button_disko.value() == 0:
        thread_run = 1

def disko_on():
    while 1:
        if thread_run == 1:
            off_all()
            led_red.value(0)
            time.sleep(0.1)
            off_all()
            led_green.value(0)
            time.sleep(0.1)
            off_all()
            led_blue.value(0)
            time.sleep(0.1)
        time.sleep(0.01)

_thread.start_new_thread(disko_on, ())

while 1:
    check_buttons()
    time.sleep(0.01)





