# PiNoiseBox

This project is using python running on RaspberryPi to map sounds to buttons through the GPIO pins. The design chosen here is using 1/2" MDF board in the form of a small box, but the housing can really be designed in any shape or form that works best for the designer. Optional LED lights were added using the 5V circuit and wired to toggle switches. The excel document included helps with creating the lines of code used in the python script that map buttons to individual sound WAV files.

# Hardware & Parts List

* Raspberry Pi Model 3 A or greater - [Link](https://vilros.com/collections/raspberry-pi-boards/products/raspberry-pi-model-3-a)
* Arcade buttons or momentary switches - [Link](https://www.amazon.com/gp/product/B01N5JRU2R/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1)
* 22AWG wire - [Link](https://www.amazon.com/gp/product/B00B4ZRPEY/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* (optional) LED - [Link](https://www.amazon.com/gp/product/B07G49PJLG/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* (optional) LED housing - [Link](https://www.amazon.com/gp/product/B07D9JL55L/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* 5V USB power adapter (an old phone charger will work fine in most cases) - [Link](https://vilros.com/products/2-5a-micro-usb-power-supply-raspberry-pi)
* (optional) Toggle Switches - [Link](https://www.amazon.com/gp/product/B07DJ62BJJ/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* Speaker Cages - [Link](https://www.amazon.com/gp/product/B07XQ8LG7N/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* Speaker Kit - [Link](https://www.amazon.com/gp/product/B07CRVRG83/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* Volume control knobs - [Link](https://www.amazon.com/gp/product/B0196J6TDC/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* Lumber/Composite/Housing - this is really up to the designer/maker

# Software
* Python 3
* Raspbian Lite (latest version)

# Auto Launch
To auto launch the python script at startup, I simply added this line to the '/etc/profile' file:

* 'sudo python3 /gpio-soundboard/soundfx/soundfx.py'

The python script uses a button module to interface with the GPIO pins and map them to sound files. The sound files must be in WAV format, and can be sourced from various sound board web pages that offer numerous clips of random sounds from all over.

 Here's a photo of the finished product:
 
![Image of PiNoiseBox](https://github.com/jddemcher/PiNoiseBox/blob/master/images/soundfx-box1.jpg)
