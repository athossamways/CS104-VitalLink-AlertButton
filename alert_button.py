import time
import RPi.GPIO as GPIO
import requests
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False
while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        requests.post("https://api.telegram.org/bot8705096213:AAH8oaIM7Kr-oi8qVKF_6kpnKsnl8KNw71M/sendMessage", 
                      json={"chat_id": "8473375894", "text": "Someone pressed the alert button!"})
        button_pressed = True

    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False
