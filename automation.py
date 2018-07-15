import pygame
import time
import random 
import numpy as np
import re

# initializing the game
pygame.init()

# size of the display window
display_width = 800
display_height = 600
# to change the speed of the blocks
speed = 7

# setting up the game window size
gameDisplay = pygame.display.set_mode((display_width,display_height))

# defining colours 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73
#setting up the caption of the window
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

carImg = pygame.image.load('media/car-image.png')

# to show the position of car
def car(x,y):
    gameDisplay.blit(carImg, (x,y))


def things_doged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Doged : " + str(count), True , black)
	gameDisplay.blit(text, (0,0))

def text_objects(text, font):
	# true parameter is for anti aliasing
	TextSurf = font.render(text, True, black)
	return TextSurf , TextSurf.get_rect()

# to show blocks on the screen
def things(thingx, thingy, thingh, thingw, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy,thingh, thingw])


# to display a message to screen
def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()

	#  we want the message to show for only about 2 sec
	time.sleep(2)

# when you crashed into a block
def crash():
	message_display("You Crashed")



# play the game
def game_loop():
    x = display_width * 0.45
    y = display_height * 0.80
    x_change = 0 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = speed
    thing_width = 100
    thing_height = 100
    doged = 0
    # initially we are not crashed
    gameExit = False

    while not gameExit:

        print('thing start: ', thing_startx)
        print('thing end: ' ,thing_startx+thing_width )
        print('car : ', x)
        if x > thing_startx-100 :
            if x<thing_startx+thing_width+100:
                if thing_startx-100 > 800-100-thing_startx-thing_width:
                    x_change -=5
                else:
                    x_change +=5
            else:
                x_change = 0
        else:
            x_change=0

            
        x  += x_change
        gameDisplay.fill(white)
		
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        things_doged(doged)     
        car(x,y)
		
        if x >display_width - car_width or x< 0:
            crash()
            pygame.quit()
            #python   quit
            quit()


		# by this we know that the block is off the screen
        if thing_starty > display_height:
			# so that the user gets a moment when the new block comes in
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0 , display_width)
            thing_width = random.randrange(100,200)
            if doged %10 ==0:
                thing_speed = thing_speed + 1
            doged = doged + 1



        if y < thing_starty + thing_height:
            #print('y cross over')
            if x > thing_startx and x < thing_startx + thing_width or x+car_width >thing_startx and x +car_width <thing_startx + thing_width:
                #print('x cross over')
                print('game over')
                crash()
                pygame.quit()
                #python   quit
                quit()
		
        pygame.display.update()

		# this takes frames per second as input
        clock.tick(60)


game_loop()
#pygame quits 
pygame.quit()
#python   quit
quit()