'''
Exo Sense RP example: Using Exo Sense RP's buzzer

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

# Buzzer ON with default tone
exo.BUZZER.on()

time.sleep(0.5)

exo.BUZZER.off()

time.sleep(0.5)

# Control via PWM:

exo.BUZZER_PWM.duty_u16(512) # 50% duty cycle

exo.BUZZER_PWM.freq(220)
time.sleep(0.5)
exo.BUZZER_PWM.freq(440)
time.sleep(0.5)
exo.BUZZER_PWM.freq(880)
time.sleep(0.5)

exo.BUZZER_PWM.duty_u16(0) # Off
