# Exo Sense RP MicroPython

Here you find a utility library and examples to program your Exo Sense RP with MicroPython.

For details on how to set up the MicroPython environment, refer to the [Raspberry Pi Pico Python SDK documentation](https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf).

## Quick start

Follow these steps to run the MicroPython examples using the Thonny IDE from your host computer connected to Exo Sense RP via USB.

- Download and install [Thonny](https://thonny.org/)
- Download the content of this repository to your computer
- Open Thonny and from the Files view (menu *View* > *Files*) navigate to the downloaded "micropython" folder
- Click on the bottom-right corner of the Thonny window to select "MicroPython (Raspberry Pi Pico)" as interpreter
- Remove power to Exo Sense RP
- Connect the USB cable to Exo Sense RP
- Connect a wire jumper to the BOOTSEL CN3 header
- Turn on power supply to the Exo Sense RP
- Remove the BOOTSEL jumper
- Click on the STOP sign button in the top bar of Thonny
- A pop-up will ask you to install MicroPython, go ahead and proceed with the installation
- In the Files view you will now see a "Raspberry Pi Pico" section showing the files uploaded to Exo Sense RP
- From the Files view right-click on the "lib" folder, select "Upload to /" and wait for the upload to finish
- Double-click on one of the example files to open it in the main editor
- Press on the "Play" (&#9658;) button in the top bar of Thonny to run the example on your Exo Sense RP

![exo-sense-rp-micropython-thonny](https://user-images.githubusercontent.com/6586434/166239355-fc8fc089-4e12-414e-8f2e-74b72be18c8f.png)
