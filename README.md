# ESP 8266 and Micropython

## Install

`pip install esptool`

`esptool.py erase_flash`

`esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash -fm dio --flash_size=detect 0 esp8266-20200911-v1.13.bin`

## Coding

Get REPL:
`miniterm /dev/ttyUSB0 115200`

Using the PyCharm Micropython plugin script:

`python3 /home/bachi/.local/share/JetBrains/PyCharm2020.2/intellij-micropython/scripts/microrepl.py /dev/ttyUSB0`

Quick Ref:
http://docs.micropython.org/en/latest/esp8266/quickref.html

Libraries:
http://docs.micropython.org/en/latest/library/index.html


## Troubleshooting

Get boot loader output:

`miniterm /dev/ttyUSB0 74880`

## OTA: 

https://github.com/rdehuyss/micropython-ota-updater

To send a new OTA update to the ESPs:

1. Create and push a git tag, e.g. `git tag -a v1.1.0 -m "1.1.0"` (`git config push.followTags true` can be useful)
2. Publish a new release on GitHub, e.g. https://github.com/bachi76/micropython-ota-test/releases/
3. On the next device boot, the new files in main/ are downloaded and after another reboot installed.
