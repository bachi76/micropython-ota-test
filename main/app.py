import time
import machine

def run():
	led = machine.Pin(2, machine.Pin.OUT)

	while True:
		print("Hello big big world V4")
		time.sleep(0.2)
		led.value(not led.value())

