# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import *
from circleshape import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	
	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		pygame.Surface.fill(screen, (0,0,0))
		for u in updatable:
			u.update(dt)
		for d in drawable:
			d.draw(screen)
		
		pygame.display.flip()

		dt = clock.tick(60) / 1000
	

print ("Starting asteroids!")
print (f"Screen width: {SCREEN_WIDTH}")
print (f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
	main()
