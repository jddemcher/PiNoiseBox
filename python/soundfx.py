import pygame
from gpiozero import Button
from time import sleep
from sys import exit

pygame.init()

aoogah = pygame.mixer.Sound("/gpio-soundboard/soundfx/aoogah.wav")
bicycle_bell = pygame.mixer.Sound("/gpio-soundboard/soundfx/bicycle_bell.wav")
blip = pygame.mixer.Sound("/gpio-soundboard/soundfx/blip.wav")
bloop_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/bloop_x.wav")
blurp_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/blurp_x.wav")
boing2 = pygame.mixer.Sound("/gpio-soundboard/soundfx/boing2.wav")
boing3 = pygame.mixer.Sound("/gpio-soundboard/soundfx/boing3.wav")
boing_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/boing_x.wav")
burp2_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/burp2_x.wav")
burp_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/burp_x.wav")
buzzer_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/buzzer_x.wav")
car_horn_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/car_horn_x.wav")
car_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/car_x.wav")
cash_register_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/cash_register_x.wav")
cow_toy = pygame.mixer.Sound("/gpio-soundboard/soundfx/cow_toy.wav")
creak_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/creak_x.wav")
cymbals = pygame.mixer.Sound("/gpio-soundboard/soundfx/cymbals.wav")
fart_z = pygame.mixer.Sound("/gpio-soundboard/soundfx/fart_z.wav")
floop2_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/floop2_x.wav")
flush_y = pygame.mixer.Sound("/gpio-soundboard/soundfx/flush_y.wav")
gong = pygame.mixer.Sound("/gpio-soundboard/soundfx/gong.wav")
hit_with_frying_pan_y = pygame.mixer.Sound("/gpio-soundboard/soundfx/hit_with_frying_pan_y.wav")
kiss_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/kiss_x.wav")
modem1 = pygame.mixer.Sound("/gpio-soundboard/soundfx/modem1.wav")
phone_ring2 = pygame.mixer.Sound("/gpio-soundboard/soundfx/phone_ring2.wav")
quick_fart_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/quick_fart_x.wav")
thunder_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/thunder_x.wav")
zag_x = pygame.mixer.Sound("/gpio-soundboard/soundfx/zag_x.wav")


btn2 = Button(2)
btn3 = Button(3)
btn14 = Button(14)
btn15 = Button(15)
btn4 = Button(4)
btn17 = Button(17)
btn18 = Button(18)
btn27 = Button(27)
btn22 = Button(22)
btn23 = Button(23)
btn25 = Button(25)
btn5 = Button(5)
btn6 = Button(6)
btn12 = Button(12)
btn13 = Button(13)
btn16 = Button(16)
btn20 = Button(20)
btn19 = Button(19)
btn26 = Button(26)
btn21 = Button(21)


btn2.when_pressed = aoogah.play
btn3.when_pressed = bicycle_bell.play
btn15.when_pressed = bloop_x.play
btn27.when_pressed = boing_x.play
btn22.when_pressed = burp2_x.play
btn23.when_pressed = burp_x.play
btn25.when_pressed = buzzer_x.play
btn5.when_pressed = car_horn_x.play
btn21.when_pressed = car_x.play
btn12.when_pressed = cash_register_x.play
btn13.when_pressed = cow_toy.play
btn16.when_pressed = creak_x.play
btn20.when_pressed = cymbals.play
btn19.when_pressed = fart_z.play
btn26.when_pressed = floop2_x.play
btn18.when_pressed = gong.play
btn14.when_pressed = hit_with_frying_pan_y.play
btn6.when_pressed = kiss_x.play
btn4.when_pressed = quick_fart_x.play
btn17.when_pressed = zag_x.play

while True:
	try:
		sleep(.01)
	except KeyboardInterrupt:
		exit()
