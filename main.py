from ota_update import OTAUpdater

def download_and_install_update_if_available():
	updater = OTAUpdater('https://github.com/sergiuszm/cae_fipy')
	updater.download_and_install_update_if_available('wifi-ssid', 'wifi-password')

def start():
	print("Startin app...")
	import main.app

def boot():
	download_and_install_update_if_available()
	start()




boot()
