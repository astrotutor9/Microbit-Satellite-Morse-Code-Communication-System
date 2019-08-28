from microbit import *
import radio

# turn on the radio using default channel 7
radio.config(channel=7)
radio.on()

while True:
    message = radio.receive()
    if message:
        radio.send(message)
        display.show(message)
        sleep(5000)
        display.clear()