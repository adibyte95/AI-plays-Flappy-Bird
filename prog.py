import pygame
import time
pygame.init()

display_width = 800
display_height = 600
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

carImg = pygame.image.load('car-image.png')

# to show the position of car
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
	# true parameter is for anti aliasing
	TextSurf = font.render(text, True, black)
	return TextSurf , TextSurf.get_rect()


def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()

	#  we want the message to show for only about 2 sec
	time.sleep(2)
	# re referencing the game loop if the user does not want to quit the game
	game_loop()

def crash():
	message_display("You Crashed")


def game_loop():
	x = display_width * 0.45
	y = display_height * 0.80
	x_change = 0 
	# initially we are not crashed
	gameExit = False

	while not gameExit:
		#this creates a list of events per frame 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# exiting the game if the user does not to play any more
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type ==pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
		x  += x_change
		gameDisplay.fill(white)
		car(x,y)
		if x >display_width - car_width or x< 0:
			crash()

		pygame.display.update()
		# this takes frames per second as input
		clock.tick(60)

#running game loop
game_loop()
#pygame quits 
pygame.quit()
#python quit
quit()
    
          