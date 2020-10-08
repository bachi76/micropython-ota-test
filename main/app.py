import time
import machine

def run():
	led = machine.Pin(2, machine.Pin.OUT)

	while True:
		print("Hello big big world V3")
		time.sleep(0.1)
		led.value(not led.value())

