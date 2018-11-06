"""
Here we call the game and it begins. 
The file 'game' feeds the data we need 
and this is where it all gets
to be processed. 

This is our game.
"""

# Make our imports
import pygame
import constants

from game import Game

def main():
	""" Our Program. Our Game."""
	# Initialize Pygame
	pygame.init()
	
	# Set up our with window dimensions
	size = [constants.screen_width, constants.screen_height]
	screen = pygame.display.set_mode(size)
	
	# Caption
	pygame.display.set_caption("Sworcery")
	
	# Setting data and objects
	done = False
	clock = pygame.time.Clock()
	
	# make an instance of our Game class
	game = Game()
	
	# main game loop
	while not done:
		# Process our events (keystrokes, mouse clicks, etc)
		done = game.process_events()
		
		# Update object positions,check for collisions, and all that jazz
		game.run_logic()
		
		# Draw the current frame
		game.display_frame(screen)
		
		# Pause for next frame and set fps
		clock.tick(60)
		
		# Displays the frame
		pygame.display.flip()
	
	# Close window and exit
	pygame.quit()
	
# Call the main function to start the game
if __name__ == "__main__":
	main()