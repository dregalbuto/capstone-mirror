import RPi.GPIO as GPIO

class Button:

    def __init__(self, pinNum):
        # set GPIO mode and set selected pin for input
        self.pinNum=pinNum
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinNum, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		
    def get_state(self):
        # return whether pin is "ON" or "OFF"
        return GPIO.input(self.pinNum)
    def get_pin(self):
        return self.pinNum
