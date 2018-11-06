"""
We feed the information provided from levels.py into here.
This allows us to create invisible platforms
for the player to jump on.
"""

import pygame

import constants

from spritesheet_functions import SpriteSheet

class Platform(pygame.sprite.Sprite):
	""" The platforms the player can jump on 
		are made here. """
		
	def __init__(self, plat_data, collision_map):
		""" Platform constructor. Assumes constructed with user passing in
			an array of 5 numbers. """
		super(Platform, self).__init__()
		
		sprite_sheet = SpriteSheet(constants.art_dir + collision_map)
		# Grab the image for this platforms
		self.image = sprite_sheet.get_image(plat_data[0],
											plat_data[1],
											plat_data[2],
											plat_data[3])
		
		self.rect = self.image.get_rect()