import time

from ota_update import OTAUpdater
import secrets

def download_and_install_update_if_available():
	updater = OTAUpdater('https://github.com/bachi76/micropython-ota-test.git')
	updater.download_and_install_update_if_available(secrets.wifi_ssid, secrets.wifi_password)

def start():
	print("Startin app...")
	import main.app
	main.app.run()

def boot():
	download_and_install_update_if_available()
	start()

print("Booting in 5sec...")
time.sleep(5)

boot()
