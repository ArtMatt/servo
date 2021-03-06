#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address.
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servoMin = 500  # Min pulse length out of 4096
servoMinn = 1  # Min pulse length out of 4096
servoMax = 550  # Max pulse length out of 4096
servoMid = 375
servoMaxx = 740
servoMaxxx = 760 
y = "yes"
m = 1


def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

while (True):
  pwm.setPWM(1, 0, servoMin)
  time.sleep(.5)
  pwm.setPWM(1, 0, servoMax)
  time.sleep(.5)
  pwm.setPWM(1, 0, servoMin)
  time.sleep(.5)
 
