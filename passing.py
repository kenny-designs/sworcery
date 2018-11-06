import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Testing get_pressed()")

clock = pygame.time.Clock()

counts = 0
i = True

while i == True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			i = False
			
		pygame.key.set_repeat(1, 10)
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_w]:
			counts += 1
			print "We are jumping! #%d" % counts 
			
		print keys
			
	clock.tick(60)
	
	pygame.display.flip()
			
			
pygame.quit()