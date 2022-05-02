'''
Utility library for Exo Sense RP

Copyright (C) 2022 Sfera Labs S.r.l. - All rights reserved.

For information, see:
http://www.sferalabs.cc/

This code is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
See file LICENSE.txt for further informations on licensing terms.
'''

from micropython import const
from machine import Pin
from machine import Signal
from machine import PWM
from machine import UART
from machine import I2S

__version__ = '1.0.0'

PIN_DI1 = const(28)
PIN_DI2 = const(29)
PIN_TTL1 = const(26)
PIN_TTL2 = const(27)
PIN_DO1 = const(10)
PIN_LED_BLUE = const(14)
PIN_LED_GREEN_N = const(11)
PIN_BUZZER = const(13)
PIN_BUZZER_PWM = const(12)
PIN_PIR = const(23)
PIN_RS485_TX = const(16)
PIN_RS485_RX = const(17)
PIN_RS485_TXEN_N = const(15)
PIN_I2S_SCK = const(6)
PIN_I2S_WS = const(7)
PIN_I2S_SD = const(8)
PIN_I2C_SDA = const(0)
PIN_I2C_SCL = const(1)

I2C_ADDR_SENS_TEMP_RH = const(0x44)
I2C_ADDR_SENS_LIGHT = const(0x45)
I2C_ADDR_SENS_SYS_TEMP_U9 = const(0x48)
I2C_ADDR_SENS_SYS_TEMP_U16 = const(0x49)
I2C_ADDR_SENS_VIBR = const(0x55)
I2C_ADDR_SENS_VOC = const(0x59)
I2C_ADDR_SECELEM = const(0x60)
I2C_ADDR_RTC = const(0x6f)
I2C_ADDR_RTC_EEPROM = const(0x57)
I2C_ADDR_EERAM_SRAM = const(0x50)
I2C_ADDR_EERAM_CTRL = const(0x18)



DI1 = Pin(PIN_DI1, mode=Pin.IN)
DI2 = Pin(PIN_DI2, mode=Pin.IN)
TTL1 = Pin(PIN_TTL1)
TTL2 = Pin(PIN_TTL2)
DO1 = Pin(PIN_DO1, mode=Pin.OUT)

LED_BLUE = Pin(PIN_LED_BLUE, mode=Pin.OUT)
LED_GREEN = Signal(Pin(PIN_LED_GREEN_N, mode=Pin.OUT), invert=True)

BUZZER = Pin(PIN_BUZZER, mode=Pin.OUT)
BUZZER_PWM = PWM(Pin(PIN_BUZZER_PWM))

PIR = Pin(PIN_PIR, mode=Pin.IN)

class _RS485:
    def __init__(self):
        self._txen_n = Pin(PIN_RS485_TXEN_N, mode=Pin.OUT)
        self.init()

    def init(self, baudrate=9600, bits=8, parity=None, stop=1, **kwargs):
       self._uart = UART(0, baudrate=baudrate, bits=bits, parity=parity, stop=stop, tx=Pin(PIN_RS485_TX), rx=Pin(PIN_RS485_RX), **kwargs)

    def __getattr__(self, attr):
        return getattr(self._uart, attr)
    
    def txen(self, enable):
        self._txen_n(not enable)
        
RS485 = _RS485()

class _MIC_I2S:
    def __init__(self):
        self.init()

    def init(self, rate=0, ibuf=1):
        self._i2s = I2S(0, sck=Pin(PIN_I2S_SCK), ws=Pin(PIN_I2S_WS), sd=Pin(PIN_I2S_SD), mode=I2S.RX, bits=32, format=I2S.MONO, rate=rate, ibuf=ibuf)

    def __getattr__(self, attr):
        return getattr(self._i2s, attr)
    
MIC_I2S = _MIC_I2S()
MIC_I2S.deinit()
