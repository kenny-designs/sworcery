"""
This module holds our Player class. Or 'fella' I 
guess you could say. This is the user-controlled 
sprite on screen.
"""

import pygame
import constants

# we'd import MovingPlatform() here if we had moving platforms
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
	""" This class represents our user-controlled player. """
	
	# -- Attributes
	# Set speed vector of player
	change_x = 0
	change_y = 0
	
	# This holds all the images for the animated walk left/right
	# cycle of our player
	walking_frames_l = []
	walking_frames_r = []
	
	# This holds all the images for our idle animation
	idle_frames_l = []
	idle_frames_r = []
	
	# If I make a jumping animation
	jumping_frames_l = []
	jumping_frames_r = []
	
	# What direction is the player facing?
	direction = 'R'
	
	# List of sprites we can bump against
	level = None
	
	# mark that we are currently jumping
	now_jumping = False
	
	# If the player ran into an enemy then we end the game.
	# This bit will be analysed in processes in game.py
	game_over = False
	
	# If the player runs into the end of the level then we go to the next one
	next_level = False
	
	# If the player isn't currently moving set this to true
	idle_time = True
	
	# If the player is walking set this to True
	walking_time = False
	
	# If the player jumps set this to True
	jumping_time = False
	
	# Signifies that the player is on the ground
	grounded = True
	
	# keeps player from stopping in place with two buttons down
	stop_a = True
	stop_d = True
	
	# toggles walk sound
	tog_walk_sound = False
	
	# -- Methods
	def __init__(self):
		""" Constructor method. """
		
		# Call the parents constructor
		super(Player, self).__init__()
		
		# Where the current frame is at in each animation
		self.frame = 0
		self.walk_frame = 0
		self.jump_frame = 0
		
		# walk sound
		self.walk_sound = pygame.mixer.Sound(constants.music_dir + 'walk_1.ogg')
		
		sprite_sheet = SpriteSheet(constants.art_dir + "fella_idle_spritesheet.png")
		# Loading all right facing idle animation images into a list
		idle_image = sprite_sheet.get_image(36, 0, 32, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(143, 0, 32, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(247, 0, 29, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(351, 0, 29, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(39, 104, 29, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(143, 104, 29, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(247, 104, 29, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(351, 104, 29, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(39, 208, 29, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(143, 208, 29, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(247, 208, 29, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(351, 208, 29, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(39, 312, 29, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(140, 312, 32, 104)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(244, 312, 32, 104)
		self.idle_frames_r.append(idle_image)
		
		# Loading all right facing and flipping to the left
		idle_image = sprite_sheet.get_image(36, 0, 32, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(143, 0, 32, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(247, 0, 29, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(351, 0, 30, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(39, 104, 29, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(143, 104, 29, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(247, 104, 29, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(351, 104, 30, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(39, 208, 29, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(143, 208, 29, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(247, 208, 29, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(351, 208, 30, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(39, 312, 29, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(140, 312, 32, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(244, 312, 32, 104)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_l.append(idle_image)
		
		
		sprite_sheet = SpriteSheet(constants.art_dir + "fella_walking_spritesheet.png")
		# Loading all right facing walking images into a list
		walk_image = sprite_sheet.get_image(36, 0, 29, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(140, 0, 29, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(237, 0, 36, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(344, 0, 33, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(36, 104, 32, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(140, 104, 32, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(244, 104, 29, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(348, 104, 29, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(36, 208, 29, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(133, 208, 36, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(240, 208, 33, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(348, 208, 33, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(36, 312, 29, 104)
		self.walking_frames_r.append(walk_image)
		walk_image = sprite_sheet.get_image(140, 312, 29, 104)
		self.walking_frames_r.append(walk_image)
		
		# Loading all right facing walking images, then flip to left
		walk_image = sprite_sheet.get_image(36, 0, 29, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(140, 0, 29, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(237, 0, 36, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(344, 0, 33, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(36, 104, 32, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(140, 104, 32, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(244, 104, 29, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(348, 104, 29, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(36, 208, 29, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(133, 208, 36, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(240, 208, 33, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(348, 208, 33, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(36, 312, 29, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		walk_image = sprite_sheet.get_image(140, 312, 29, 104)
		walk_image = pygame.transform.flip(walk_image, True, False)
		self.walking_frames_l.append(walk_image)
		
		sprite_sheet = SpriteSheet(constants.art_dir + 'fella_jumping_spritesheet.png')
		# Loading all right facing images for jumping animation
		jump_image = sprite_sheet.get_image(36, 0, 29, 104)
		self.jumping_frames_r.append(jump_image)
		jump_image = sprite_sheet.get_image(140, 3, 35, 101)
		self.jumping_frames_r.append(jump_image)
		jump_image = sprite_sheet.get_image(244, 6, 35, 98)
		self.jumping_frames_r.append(jump_image)
		jump_image = sprite_sheet.get_image(344, 10, 39, 94)
		self.jumping_frames_r.append(jump_image)
		jump_image = sprite_sheet.get_image(36, 114, 35, 94)
		self.jumping_frames_r.append(jump_image)
		jump_image = sprite_sheet.get_image(140, 107, 35, 101)
		self.jumping_frames_r.append(jump_image)
		jump_image = sprite_sheet.get_image(244, 107, 39, 101)
		self.jumping_frames_r.append(jump_image)
		jump_image = sprite_sheet.get_image(344, 104, 49, 104)
		self.jumping_frames_r.append(jump_image)
		jump_image = sprite_sheet.get_image(32, 208, 59, 104)
		self.jumping_frames_r.append(jump_image)
		
		# Loading all right facing images for jumping animation
		# and flipping them
		jump_image = sprite_sheet.get_image(36, 0, 29, 104)
		jump_image = pygame.transform.flip(jump_image, True, False)
		self.jumping_frames_l.append(jump_image)
		jump_image = sprite_sheet.get_image(140, 3, 35, 101)
		jump_image = pygame.transform.flip(jump_image, True, False)
		self.jumping_frames_l.append(jump_image)
		jump_image = sprite_sheet.get_image(244, 6, 35, 98)
		jump_image = pygame.transform.flip(jump_image, True, False)
		self.jumping_frames_l.append(jump_image)
		jump_image = sprite_sheet.get_image(344, 10, 39, 94)
		jump_image = pygame.transform.flip(jump_image, True, False)
		self.jumping_frames_l.append(jump_image)
		jump_image = sprite_sheet.get_image(36, 114, 35, 94)
		jump_image = pygame.transform.flip(jump_image, True, False)
		self.jumping_frames_l.append(jump_image)
		jump_image = sprite_sheet.get_image(140, 107, 35, 101)
		jump_image = pygame.transform.flip(jump_image, True, False)
		self.jumping_frames_l.append(jump_image)
		jump_image = sprite_sheet.get_image(244, 107, 39, 101)
		jump_image = pygame.transform.flip(jump_image, True, False)
		self.jumping_frames_l.append(jump_image)
		jump_image = sprite_sheet.get_image(344, 104, 49, 104)
		jump_image = pygame.transform.flip(jump_image, True, False)
		self.jumping_frames_l.append(jump_image)
		jump_image = sprite_sheet.get_image(32, 208, 59, 104)
		jump_image = pygame.transform.flip(jump_image, True, False)
		self.jumping_frames_l.append(jump_image)
		
		
		self.image = self.walking_frames_r[0]
		
		# Set a reference to the image rect.
		self.rect = self.image.get_rect()
		
	def update(self):
		""" Move the player. """
		
		# checking our direction
		if self.change_x > 0:
			self.direction = "R"
		elif self.change_x < 0:
			self.direction = "L"
		
		# idle animation if we aren't moving
		if self.idle_time == True:
			if self.direction == "R":
				self.image = self.idle_frames_r[int(round(self.frame))]
				self.frame += 0.05
				
				if self.frame >= 14:
					self.frame = 0
			elif self.direction == "L":
				self.image = self.idle_frames_l[int(round(self.frame))]
				self.frame += 0.05
				
				if self.frame >= 14:
					self.frame = 0
		elif self.walking_time == True:
			if self.direction == "R":
				self.image = self.walking_frames_r[int(round(self.walk_frame))]
				self.walk_frame += 0.3
				
				if self.walk_frame >= 13:
					self.walk_frame = 0
			elif self.direction == "L":
				self.image = self.walking_frames_l[int(round(self.walk_frame))]
				self.walk_frame += 0.3
				
				if self.walk_frame >= 13:
					self.walk_frame = 0
		elif self.jumping_time == True:
			if self.direction == "R":
				if int(round(self.jump_frame)) <= 8:
					self.image = self.jumping_frames_r[int(round(self.jump_frame))]
					self.jump_frame += 1
				
				elif self.jump_frame >= 8:
					self.jumping_time = False
					self.jump_frame = 0
			elif self.direction == "L":
				if int(round(self.jump_frame)) <= 8:
					self.image = self.jumping_frames_l[int(round(self.jump_frame))]
					self.jump_frame += 1
					
				elif self.jump_frame >= 8:
					self.jumping_time = False
					self.jump_frame = 0
		# if we are falling despite not jumping, display last frame of jumping animation
		
		# allows us to turn left and right in mid air after jumping
		elif self.idle_time == False and self.walking_time == False:
			if self.direction == "R":
				self.image = self.jumping_frames_r[8]
			elif self.direction == "L":
				self.image = self.jumping_frames_l[8]
				
		
		# Keep jumping until false
		if self.now_jumping == True:
			self.jump()
		
		# Gravity
		self.calc_grav()
		
		# if player on the ground, we can jump again!
		#if self.change_y >= 0 and self.rect.bottom >= constants.screen_height:
		#	self.initial_jump = False
		
		# Move left/right
		self.rect.x += self.change_x
		
			
		# see if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			# If we are moving right,
			# Set our right side to the left side of the item we hit
			if self.change_x > 0:
				self.rect.right = block.rect.left
				# Hit wall, stop walking if not in air
				if self.change_y == 0 and self.change_x != 0:
					self.walking_time = False
					self.idle_time = True
			elif self.change_x < 0 and self.change_x != 0:
				# Otherwise, if we are moving left, do the opposite.
				self.rect.left = block.rect.right
				# Hit wall, stop walking if not in air
				if self.change_y == 0:
					self.walking_time = False
					self.idle_time = True
				
		# check if we hit any enemies
		enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
		for enemy in enemy_hit_list:
			self.game_over = True
			
		# check if we hit the boss
		boss_hit_list = pygame.sprite.spritecollide(self, self.level.boss_list, False)
		for boss in boss_hit_list:
			self.game_over = True
		
		# check if we can move to the next level yet
		level_hit_list = pygame.sprite.spritecollide(self, self.level.next_level_list, False)
		for marker in level_hit_list:
			self.next_level = True
		
		# Move up/down
		self.rect.y += self.change_y
		
		# Check and see if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			# Reset our position based on the top/bottom of the object.
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
				# Now that we have landed, start the walking and idle animations again
				# while making sure the jumping animation has stopped
				if self.walking_time == False and self.idle_time == False:
					if self.change_x == 0:
						self.idle_time = True
					else:
						self.walking_time = True
					self.jumping_time = False
					self.grounded = True
					
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
				
			# Stop our vertical movement
			self.change_y = 0
			
		# check if we hit any enemies
		enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
		for enemy in enemy_hit_list:
			self.game_over = True
			
		# check if we hit the boss
		boss_hit_list = pygame.sprite.spritecollide(self, self.level.boss_list, False)
		for boss in boss_hit_list:
			self.game_over = True
			
		# check if we can move to the next level yet
		level_hit_list = pygame.sprite.spritecollide(self, self.level.next_level_list, False)
		for marker in level_hit_list:
			self.next_level = True	
		
	def calc_grav(self):
		""" Calculate effect of gravity. """
		
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += 1 # 1.4
			
		# See if we are on the ground
		#if self.rect.y >= constants.screen_height - self.rect.height and self.change_y >= 0:
		#	self.change_y = 0
		#	self.rect.y = constants.screen_height - self.rect.height
			
	def jump(self):
		""" Called when user hits 'jump' button. """
		
		# move down a bit and see if there is a platform below us.
		# Move down 2 pixels because it doesn't work well if we only move down 1
		# when working with a platform moving down.
		self.rect.y += 2 
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2
		
		
		# If it is okay to jump, set our speed upwards
		# and mark that we are now jumping
		if len(platform_hit_list) > 0:
			if self.change_y >= 0:
				self.change_y -= 3 # 3.5
				self.now_jumping = True
				# start the jumping animation
				self.jumping_time = True
				# stop the walking animation
				self.walking_time = False
				# stop the idle animation
				self.idle_time = False
				# we are no longer on the ground,
				# make sure idle and jump does not play!
				self.grounded = False

		else:
			# this checks if we are airborne.
			# if so, we continue going up and up until we hit our limit
			if self.change_y < -1:
				self.change_y -= 3 # 3.5
			
			# this is our limit
			# once we hit it the whole jumping action ends 
			# and can not be done again until we land.
			if self.change_y <= -20:
				self.now_jumping = False
		
	# Player-controlled movements:
	def go_left(self):
		""" Called when user hits 'A' key. """
		
		# Do not play walking animation while in air
		if self.change_y == 0 and self.grounded == True:
			# make sure idle animation isn't playing
			self.idle_time = False
			# play walking animation
			self.walking_time = True
		
		self.change_x = -4
		#self.direction = 'L'
		
	def go_right(self):
		""" Called when the user hits the 'D' key. """
		
		# Do not play walking animation while in air
		if self.change_y == 0 and self.grounded == True:
			# Make sure idle animation isn't playing
			self.idle_time = False
			# play walking animation
			self.walking_time = True
		
		self.change_x = 4
		#self.direction = 'R'
		
	def stop(self):
		""" Called when the user lets off the keyboard. """
		
		# Do not play idle animation while in air
		if self.change_y == 0 and self.grounded == True:
			# stop walking animation
			self.walking_time = False
			# No longer moving, start idle animation
			self.idle_time = True
		
		# Note, I would modify self.direction to help indicate a 
		# idle animation. For now, this will do.
		self.change_x = 0