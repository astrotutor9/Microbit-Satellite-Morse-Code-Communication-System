from microbit import *
import radio

# turn on the radio using default channel 7
radio.config(channel=7)
radio.on()

dots_and_dashes = []
message_sent = False

dash_image = Image("00000:"
             "00000:"
             "09990:"
             "00000:"
             "00000")

while True:
    if button_a.is_pressed():
        dots_and_dashes.append("dot")
        display.set_pixel(2,2,9)
        sleep(200)
        display.clear()
        
    elif button_b.is_pressed():
        dots_and_dashes.append("dash")
        display.show(dash_image)
        sleep(200)
        display.clear()
        
    # send letter as string of dots and dashes
    elif accelerometer.is_gesture("up") and message_sent is False and dots_and_dashes != []:
        message_sent = True
        # create an empty string
        code = ""
        for morse_code in dots_and_dashes:            
            code = code + morse_code
        radio.send(code)
        display.show(Image.YES)
        
    # send "end of message"
    elif accelerometer.is_gesture("right") or accelerometer.is_gesture("left"):
        radio.send("end")
        display.show(Image.HAPPY)
        
    # empty the message ready to send another
    if accelerometer.is_gesture("down") and message_sent is True:
        dots_and_dashes = []
        message_sent = False
        display.clear()