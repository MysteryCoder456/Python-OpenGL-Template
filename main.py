import pygame
from pygame.locals import *
pygame.init()

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
	(1, -1, -1), # 0
	(1, 1, -1), # 1
	(-1, 1, -1), # 2
	(-1, -1, -1), # 3
	(1, -1, 1), # 4
	(1, 1, 1), # 5
	(-1, 1, 1), # 6
	(-1, -1, 1) # 7
)

edges = (
	(0, 1),
	(0, 3),
	(0, 4),
	(1, 2),
	(1, 5),
	(2, 3),
	(2, 6),
	(3, 7),
	(4, 5),
	(4, 7),
	(5, 6),
	(6, 7)
)

surfaces = (
	(0, 1, 2, 3),
	(3, 7, 4, 0),
	(2, 3, 7, 6),
	(1, 2, 5, 6),
	(4, 5, 6, 7),
	(0, 1, 4, 5)
)





def start(FOV, width, height):
	gluPerspective(FOV, (width / height), 0.1, 50.0)

	# Put any initializing code for the GAME not PROGRAM below this line
	glTranslatef(0, 0, -4)
	glRotatef(25, 1, 0, 0)


def logic():
	# Put all code for game logic here
	glRotate(1, 0, 1, 0)


def render():
	# Put all rendering code between glClear() and pygame.display.flip()
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

	# Fill cube
	glBegin(GL_QUADS)

	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1, 0, 0))
			glVertex3fv(vertices[vertex])

	glEnd()

	# Outline cube
	glBegin(GL_LINES)

	for edge in edges:
		for vertex in edge:
			glColor3fv((1, 1, 1))
			glVertex3fv(vertices[vertex])

	glEnd()

	pygame.display.flip()





# Change the code below only if absolutely needed!!
def main():
	width = 800
	height = 600
	win = pygame.display.set_mode((width, height), DOUBLEBUF|OPENGL)
	pygame.display.set_caption("Boilerplate Title")

	clock = pygame.time.Clock()
	running = True
	FPS = 60 # Frames Per Second
	FOV = 75 # Field Of Vision (in degrees)

	start(FOV, width, height)

	while running:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		logic()
		render()


if __name__ == "__main__":
	main()
	pygame.quit()
	quit()
