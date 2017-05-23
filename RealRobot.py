import sys
import traceback
import pygame
import drive

def drawArrow_left():
	xL = 0
	yL = 30
	pygame.draw.polygon(window, white, ((30 + xL, 10 + yL), (30 + xL, 20 + yL), (10 + xL, 20 + yL), (10 + xL, 30 + yL), (0 + xL, 15 + yL), (10 + xL, 0 + yL), (10 + xL, 10 + yL)))
	return

def drawArrow_right():
	xR = 200
	yR = 30
	pygame.draw.polygon(window, white, ((0 + xR, 10 + yR), (0 + xR, 20 + yR), (20 + xR, 20 + yR), (20 + xR, 30 + yR), (30 + xR, 15 + yR), (20 + xR, 0 + yR), (20 + xR, 10 + yR)))
	return

def drawText(text):
	label = myfont.render(text, 1, white)
	window.blit(label, (80, 35))
	return

pygame.init()
window = pygame.display.set_mode((230, 100))
myfont = pygame.font.SysFont("monospace", 20)
black = (0, 0, 0)
white = (255, 255, 255)

forwards = False
backwards = False
left = False
right = False

try:
	while True:
		window.fill(black)	#intention is to clear the window

		for event in pygame.event.get():

			if (event.type == pygame.QUIT):
 				raise KeyboardInterrupt

			if (event.type == pygame.KEYDOWN):

				if (event.key == pygame.K_w):
					forwards = True
				elif (event.key == pygame.K_s):
					backwards = True

				if (event.key == pygame.K_d):
					right = True
				elif (event.key == pygame.K_a):
					left = True

			if (event.type == pygame.KEYUP):

				if (event.key == pygame.K_w):
					forwards = False
				elif (event.key == pygame.K_s):
					backwards = False
				
				if (event.key == pygame.K_d):
					right = False
				elif (event.key == pygame.K_a):
					left = False


		if right and (not left):
			drawArrow_right()

			if forwards and (not backwards):
				drive.move_forward_right()
				drawText("forward")
			elif backwards and (not forwards):
				drive.move_backward_right()
				drawText("backward")
			else:
				drive.turn_right()
		elif left and (not right):
			drawArrow_left()

			if forwards and (not backwards):
				drive.move_forward_left()
				drawText("forward")
			elif backwards and (not forwards):
				drive.move_backward_left()
				drawText("backward")
			else:
				drive.turn_left()
		else:
			if forwards and (not backwards):
				drive.move_forward()
				drawText("forward")
			elif backwards and (not forwards):
				drive.move_backward()
				drawText("backward")
			else:
				drive.stop()
				drawText("stop")
		
		pygame.display.update()

except KeyboardInterrupt:
	print("exit")

except:
	print("Error occured")
	traceback.print_exc()

finally:
	drive.cleanup()
	sys.exit()
