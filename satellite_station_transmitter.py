from microbit import *
import radio

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
        print("Dot")
        display.set_pixel(2,2,9)
        sleep(200)
        display.clear()

    elif button_b.is_pressed():
        dots_and_dashes.append("dash")
        print("Dash")
        display.show(dash_image)
        sleep(200)
        display.clear()

        # Continues on next page
        # send single letter as string of dots and dashes
        # NEXT TWO LINES TYPE IN AS ONE LINE - TOO LONG FOR THIS PAGE!

    elif accelerometer.is_gesture("up") and message_sent is False and dots_and_dashes != []:
        # create the string of dots/dashes into one
        # send as a complete word
        code = ''.join(dots_and_dashes)
        radio.send(code)
        message_sent = True
        dots_and_dashes = []
        display.show(Image.YES)
        print("Message sent")
        print(code)

    # send "space" to indicate end of word
    elif accelerometer.is_gesture("right"):
        radio.send("space")
        message_sent = True
        dots_and_dashes = []
        print("Space")
        display.show(Image.YES)
        sleep(200)
        display.clear()

    # send "end of message"
    elif accelerometer.is_gesture("left"):
        radio.send("end")
        message_sent = True
        print("End")
        display.show(Image.HAPPY)

    # empty the word message ready to send another
    elif accelerometer.is_gesture("down") and message_sent is True:
        dots_and_dashes = []
        message_sent = False
        print("Clear message")
        display.clear()