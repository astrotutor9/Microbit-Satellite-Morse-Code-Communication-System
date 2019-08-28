from microbit import *
import radio

# turn on the radio using default channel 7
radio.config(channel=7)
radio.on()

while True:
    if button_a.is_pressed():
        radio.send("Hello Planet Earth")
        display.show("m")
        sleep(500)
        display.clear()