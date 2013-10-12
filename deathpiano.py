#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time


pwm = PWM(0x40, debug=True)

m = 375

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

def snooze():
  time.sleep(.3)

def tap():
  pwm.setPWM(2, 0, 300)	
  snooze()
  pwm.setPWM(2, 0, 450)
  snooze()
  pwm.setPWM(2, 0, 300)
  print "tapped"

def check_range(m):
  if m < 150:
    m = 150
  elif m > 600:
    m = 600
  return m

pwm.setPWM(1, 0, 375)
time.sleep(.5)
pwm.setPWM(2, 0, 300)
time.sleep(.1)
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()

pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 375)
time.sleep(.5)
pwm.setPWM(2, 0, 300)
time.sleep(.1)
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()

pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 375)
time.sleep(.5)
pwm.setPWM(2, 0, 300)
time.sleep(.1)
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()

pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 375)
time.sleep(.5)
pwm.setPWM(2, 0, 300)
time.sleep(.1)
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()

pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 375)
time.sleep(.5)
pwm.setPWM(2, 0, 300)
time.sleep(.1)
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()

pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 500)
tap()
pwm.setPWM(1, 0, 600)
tap()
pwm.setPWM(1, 0, 330)
tap()
pwm.setPWM(1, 0, 255)
tap()


