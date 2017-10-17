from phue import Bridge
import signal
import time
import sys
b = Bridge('10.0.101.23')

lightNumber = int(sys.argv[1])
light = b.get_light_objects("id")[lightNumber]

oldHue = light.hue
oldSaturation = light.saturation
oldBrightness = light.brightness
oldState = light.on

hueProsent = 64000/100
saturationProsent = 255/100
brightnessProsent = 255/100

def beforeSuicide(signum, frame):
	light.hue = oldHue
	light.saturation = oldSaturation
	light.brightness = oldBrightness
	light.on = oldState
	exit(1)

signal.signal(signal.SIGINT, beforeSuicide)
signal.signal(signal.SIGTERM, beforeSuicide)

brightness = 0
hue = 0
saturation = 0

light.on = True
light.transitiontime = 4
while True:
	light.hue = min(hue*hueProsent, 64000)
	light.saturation = min(int(saturation*saturationProsent), 255)
	light.brightness = min(int(brightness*brightnessProsent), 255)
	if brightness < 100:
		brightness += 5
	if saturation < 100 and brightness == 100:
		saturation += 20
	if brightness == 100 and saturation == 100:
		hue = (hue + 1.5) % 100
	time.sleep(0.2)
