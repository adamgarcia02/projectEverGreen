# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import Adafruit_TCS34725
import smbus
tcs = Adafruit_TCS34725.TCS34725()
from neopixel import *


# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

# Or you can change the integration time and/or gain:
tcs = Adafruit_TCS34725.TCS34725(integration_time=Adafruit_TCS34725.TCS34725_INTEGRATIONTIME_101MS,
                                 gain=Adafruit_TCS34725.TCS34725_GAIN_4X)
# Disable interrupts (can enable them by passing true, see the set_interrupt_limits function too).
tcs.set_interrupt(False)

#Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
                r, g, b, c = tcs.get_raw_data()
                rcomp = r
                gcomp= g
                bcomp = b
                # Print out the values.
                print('Color: red={0} green={1} blue={2} clear={3}'.format(r, g, b, c))

                if(r < 800):
                        rcomp + ((800-r)*(0.2125))                        
                        print('Red Spectrum Compensation')
                        time.sleep(100/100)
                        
                        
                if(g < 900):
                        gcomp +((900-g)*(0.2125))
                        print('Green Spectrum Compensation')
                        time.sleep(100/100)
                        
                if(b < 1200):
                        bcomp +((1200-b)*(0.2125))
                        print('Blue Spectrum Compensation')
                        time.sleep(100/100)

                else:
                        print('All good baby ;)')
                        for i in range(strip.numPixels()):
                                strip.setPixelColor(i, Color((0), (0), (0)))
                                strip.show()
                        time.sleep(500/100)

                for i in range(strip.numPixels()):
                                strip.setPixelColor(i, Color((rcomp), (gcomp), (bcomp)))
                                strip.show()
        
                                                  
                
# Enable interrupts and put the chip back to low power sleep/disabled.
#                tcs.set_interrupt(True)
#                tcs.disable()
