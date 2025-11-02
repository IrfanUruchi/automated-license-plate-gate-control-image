# app/gpio_out.py

import RPi.GPIO as GPIO
import atexit

YELLOW, GREEN, RED = 18, 17, 27

GPIO.setmode(GPIO.BCM)
GPIO.setup([YELLOW, GREEN, RED], GPIO.OUT, initial=GPIO.LOW)

def signal(status: str):
    GPIO.output(YELLOW, status == 'SCANNING')
    GPIO.output(GREEN,  status == 'GRANTED')
    GPIO.output(RED,    status == 'DENIED')

def cleanup():
    GPIO.output([YELLOW, GREEN, RED], GPIO.LOW)
    GPIO.cleanup()

atexit.register(cleanup)

