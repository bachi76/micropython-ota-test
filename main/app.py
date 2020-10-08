import time
import machine

def run():
	led = machine.Pin(2, machine.Pin.OUT)

	while True:
		print("Hello big big world V2")
		time.sleep(0.5)
		led.value(not led.value())

