import pygame
from gpiozero import Button
from time import sleep
from sys import exit

pygame.init()

bugs_goodbye = pygame.mixer.Sound("/gpio-soundboard/looneytunes/bugs_goodbye.wav")
bugs_here_i_come = pygame.mixer.Sound("/gpio-soundboard/looneytunes/bugs_here_i_come.wav")
bugs_whats_up_doc = pygame.mixer.Sound("/gpio-soundboard/looneytunes/bugs_whats_up_doc.wav")
chicken_hawk = pygame.mixer.Sound("/gpio-soundboard/looneytunes/chicken_hawk.wav")
daffy_are_u_nuts = pygame.mixer.Sound("/gpio-soundboard/looneytunes/daffy_are_u_nuts.wav")
daffy_cut_that_out = pygame.mixer.Sound("/gpio-soundboard/looneytunes/daffy_cut_that_out.wav")
daffy_despicable = pygame.mixer.Sound("/gpio-soundboard/looneytunes/daffy_despicable.wav")
elmer_be_very_quiet = pygame.mixer.Sound("/gpio-soundboard/looneytunes/elmer_be_very_quiet.wav")
elmer_come_back = pygame.mixer.Sound("/gpio-soundboard/looneytunes/elmer_come_back.wav")
elmer_hunting = pygame.mixer.Sound("/gpio-soundboard/looneytunes/elmer_hunting.wav")
elmer_screwy = pygame.mixer.Sound("/gpio-soundboard/looneytunes/elmer_screwy.wav")
marvin_angry = pygame.mixer.Sound("/gpio-soundboard/looneytunes/marvin_angry.wav")
marvin_bit_nice = pygame.mixer.Sound("/gpio-soundboard/looneytunes/marvin_bit_nice.wav")
porky_thats_all_folks = pygame.mixer.Sound("/gpio-soundboard/looneytunes/porky_thats_all_folks.wav")
roadrunner2 = pygame.mixer.Sound("/gpio-soundboard/looneytunes/roadrunner2.wav")
sylvester_sufferin = pygame.mixer.Sound("/gpio-soundboard/looneytunes/sylvester_sufferin.wav")
taz = pygame.mixer.Sound("/gpio-soundboard/looneytunes/taz.wav")
tweety_bad2 = pygame.mixer.Sound("/gpio-soundboard/looneytunes/tweety_bad2.wav")
tweety_puddy_tat = pygame.mixer.Sound("/gpio-soundboard/looneytunes/tweety_puddy_tat.wav")
yosemite_toads = pygame.mixer.Sound("/gpio-soundboard/looneytunes/yosemite_toads.wav")

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

btn2.when_pressed = bugs_goodbye.play
btn3.when_pressed = bugs_here_i_come.play
btn15.when_pressed = bugs_whats_up_doc.play
btn27.when_pressed = chicken_hawk.play
btn22.when_pressed = daffy_are_u_nuts.play
btn23.when_pressed = daffy_cut_that_out.play
btn25.when_pressed = daffy_despicable.play
btn5.when_pressed = elmer_be_very_quiet.play
btn21.when_pressed = elmer_come_back.play
btn12.when_pressed = elmer_hunting.play
btn13.when_pressed = elmer_screwy.play
btn16.when_pressed = marvin_angry.play
btn20.when_pressed = marvin_bit_nice.play
btn19.when_pressed = porky_thats_all_folks.play
btn26.when_pressed = roadrunner2.play
btn18.when_pressed = sylvester_sufferin.play
btn14.when_pressed = taz.play
btn6.when_pressed = tweety_bad2.play
btn4.when_pressed = tweety_puddy_tat.play
btn17.when_pressed = yosemite_toads.play


while True:
	try:
		sleep(.01)
	except KeyboardInterrupt:
		exit()
