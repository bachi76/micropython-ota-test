import time
import machine

led = machine.Pin(2, machine.Pin.OUT)

while True:
	print("Hello big big world")
	time.sleep(2)
	led.value(not led.value())

