'''
Exo Sense RP example: Using Exo Sense RP's microphone

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

buf = bytearray(10000)

exo.MIC_I2S.init(rate=44100, ibuf=40000)

for _ in range(0, 10):
    ret = exo.MIC_I2S.readinto(buf)
    print("Read {} bytes".format(ret))

exo.MIC_I2S.deinit()
