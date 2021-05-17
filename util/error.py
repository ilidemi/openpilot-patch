import time

while True:
    brightness_path = '/sys/class/leds/lcd-backlight/brightness'
    with open(brightness_path, 'w') as brightness_f:
        brightness_f.write('63')
    time.sleep(1.0)
    with open(brightness_path, 'w') as brightness_f:
        brightness_f.write('127')
    time.sleep(1.0)
