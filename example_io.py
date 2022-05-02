'''
Exo Sense RP example: using I/Os interfaces

Simple example showing the main functionalities for I/O control

Copyright (C) 2022 Sfera Labs S.r.l. - All rights reserved.

For information, see:
http://www.sferalabs.cc/

This code is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
See file LICENSE.txt for further informations on licensing terms.
'''

import exosense as exo
from machine import Pin
import time

# configure TTL1 as input and TTL2 as output
exo.TTL1.init(mode=Pin.IN)
exo.TTL2.init(mode=Pin.OUT)

# handler for DI1 interrupt (see below)
def on_di1_change(pin):
    global exo
    # set TTL2 to follow TTL1
    exo.TTL2(pin())

# configure interrupt on DI1 to call on_di1_change() when its state changes
exo.DI1.irq(handler=on_di1_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)

while True:
    print("------------")

    # print all I/Os sate
    print("DI1 = {}".format(exo.DI1()))
    print("DI2 = {}".format(exo.DI2()))
    print("TTL1 = {}".format(exo.TTL1()))
    print("TTL2 = {}".format(exo.TTL2()))
    print("DO1 = {}".format(exo.DO1()))

    # toggle DO1
    exo.DO1.toggle()

    time.sleep(1)
