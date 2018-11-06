"""
This is out gem module. The main point of it
is to let the gem animation play and if the
player touches the gem then the game ends and 
they win!
"""

import pygame

import constants

from spritesheet_functions import SpriteSheet

class Gem(pygame.sprite.Sprite):
	""" This class represents the gem. """
	
	# -- Attributes
	# blank for now
	
	# Now make the lists for our images to make the animation
	
	# idle animation
	idle_frames_gem = []
	
	# since the gem has no real 'direction' we won't 
	# need to set one
	
	# -- Methods
	def __init__(self):
		""" Constructor method. """
		
		# Call the parents constructor
		super(Gem, self).__init__()
		
		# Where the current frame is at in the animation
		self.idle_frame = 0
		
		sprite_sheet = SpriteSheet(constants.art_dir + "gem_idle_spritesheet.png")
		# Loading all idle animation images for gem into a list
		idle_image = sprite_sheet.get_image(0, 0, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(64, 0, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(128, 0, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(192, 0, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(0, 64, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(64, 64, 64, 64)
		self.idle_frames_gem.append(idle_image) 
		idle_image = sprite_sheet.get_image(128, 64, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(192, 64, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(0, 128, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(64, 128, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(128, 128, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(192, 128, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(0, 192, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_frame = sprite_sheet.get_image(64, 192, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(128, 192, 64, 64)
		self.idle_frames_gem.append(idle_image)
		idle_image = sprite_sheet.get_image(192, 192, 64, 64)
		self.idle_frames_gem.append(idle_image)
		
		self.image = self.idle_frames_gem[0]
		
		# Set a reference to the image rect.
		self.rect = self.image.get_rect()
		
	def update(self):
		""" Let the gem run through it's animation and logic. """
		
		# idle animation
		self.image = self.idle_frames_gem[int(round(self.idle_frame))]
		self.idle_frame += 0.25
		
		if self.idle_frame >= 15:
			self.idle_frame = 0