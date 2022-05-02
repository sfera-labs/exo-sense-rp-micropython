'''
Exo Sense RP example: Using Exo Sense RP's LED light

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
import time

while True:
    exo.LED_BLUE.toggle()
    
    led = exo.LED_BLUE()
    print("LED {}".format("ON" if led == 1 else "OFF"))
    
    time.sleep(1)
