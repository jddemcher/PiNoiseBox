import pygame.mixer
from gpiozero import Button
from time import sleep
from sys import exit

pygame.mixer.init()

belle = pygame.mixer.Sound("/gpio-soundboard/disney/belle.wav")
dream = pygame.mixer.Sound("/gpio-soundboard/disney/dream.wav")
evermore = pygame.mixer.Sound("/gpio-soundboard/disney/evermore.wav")
friend = pygame.mixer.Sound("/gpio-soundboard/disney/friend.wav")
howfar = pygame.mixer.Sound("/gpio-soundboard/disney/howfar.wav")
letgo = pygame.mixer.Sound("/gpio-soundboard/disney/letgo.wav")
love = pygame.mixer.Sound("/gpio-soundboard/disney/love.wav")
love2night = pygame.mixer.Sound("/gpio-soundboard/disney/love2night.wav")
prince = pygame.mixer.Sound("/gpio-soundboard/disney/prince.wav")
queen = pygame.mixer.Sound("/gpio-soundboard/disney/queen.wav")
riverbend = pygame.mixer.Sound("/gpio-soundboard/disney/riverbend.wav")
shiny = pygame.mixer.Sound("/gpio-soundboard/disney/shiny.wav")
showyourself = pygame.mixer.Sound("/gpio-soundboard/disney/showyourself.wav")
undersea = pygame.mixer.Sound("/gpio-soundboard/disney/undersea.wav")
unkown = pygame.mixer.Sound("/gpio-soundboard/disney/unkown.wav")
wind = pygame.mixer.Sound("/gpio-soundboard/disney/wind.wav")
wish = pygame.mixer.Sound("/gpio-soundboard/disney/wish.wav")

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

btn2.when_pressed = belle.play
btn3.when_pressed = dream.play
btn15.when_pressed = evermore.play
btn27.when_pressed = friend.play
btn22.when_pressed = howfar.play
btn23.when_pressed = letgo.play
btn25.when_pressed = love.play
btn5.when_pressed = love2night.play
btn21.when_pressed = prince.play
btn12.when_pressed = queen.play
btn13.when_pressed = riverbend.play
btn16.when_pressed = shiny.play
btn20.when_pressed = showyourself.play
btn19.when_pressed = pygame.mixer.stop
btn26.when_pressed = unkown.play
btn18.when_pressed = wind.play
btn14.when_pressed = wish.play
btn6.when_pressed = pygame.mixer.stop
btn4.when_pressed = undersea.play
btn17.when_pressed = pygame.mixer.stop

while True:
	try:
		sleep(.01)
	except KeyboardInterrupt:
		exit()
