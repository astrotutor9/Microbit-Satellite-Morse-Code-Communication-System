from microbit import *
import radio

# turn on the radio using default channel 7
radio.config(channel=7)
radio.on()

morse_alphabet = {"dotdash": "a", "dashdotdotdot": "b", "dashdotdashdot": "c",
                "dashdotdot": "d", "dot": "e", "dotdotdashdot": "f",
                "dashdashdot": "g", "dotdotdotdot": "h", "dotdot": "i",
                "dotdashdashdash": "j", "dashdotdash": "k", "dotdashdotdot": "l",
                "dashdash": "m", "dashdot": "n", "dashdashdash": "o",
                "dotdashdashdot": "p", "dashdashdotdash": "q", "dotdashdot": "r",
                "dotdotdot": "s", "dash":"t", "dotdotdash": "u",
                "dotdotdotdash": "v", "dotdashdash": "w", "dashdotdotdash": "x",
                "dashdotdashdash": "y", "dashdashdotdot": "z",
                "dotdashdashdashdash": "1", "dotdotdashdashdash": "2",
                "dotdotdotdashdash": "3", "dotdotdotdotdash": "4",
                "dotdotdotdotdot": "5", "dashdotdotdotdot": "6",
                "dashdashdotdotdot": "7", "dashdashdashdotdot": "8",
                "dashdashdashdashdot": "9", "dashdashdashdashdash": "0"}

letters_received = []
plain_language_message = []

while True:
    message = radio.receive()
    if message:
        if message != "end":  # is not 6 dots end of message
            letters_received.append(message)
            print(message)
        
        if message == "end":  # is 6 dots end of message
            print("translating")
            # read letters_received one at a time
            for letters in letters_received:
                # compare to morse_alphabet
                for morse_letters in morse_alphabet:
                    # convert to real letters and write to translated message
                    if morse_letters == letters:
                        plain_language_message.append(morse_alphabet[morse_letters])
            # convert plain_language_message list to ordinary text
            plain_text = ""
            for plain_letters in plain_language_message:
                plain_text = plain_text + plain_letters
            display.scroll(plain_text)
            print(plain_text)
            letters_received = []
            plain_language_message = []
        sleep(10)