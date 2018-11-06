"""
This module holds our BossFella class. This BossFella class represents
the final boss the player must encounter before reaching the gem.
His mechanic is simply a quick charge. I would like for him to 
go sliding way back after hitting the wall only to get back up 
and charge again. If there's time, and I feel up to it, I'll do that.
"""

import pygame

import constants

# to manage world shift
import levels

from spritesheet_functions import SpriteSheet

class BossFella(pygame.sprite.Sprite):
	""" This class represents the final boss. """
	
	# -- Attributes
	# Set speed vector of boss
	change_x = 0
	change_y = 0
	
	# Now we make lists for our images to make animation
	
	# idle animation
	idle_frames_l = []
	idle_frames_r = []
	
	# charging animation 
	charging_frames = []
	
	# Direction the boss is facing
	direction = 'L'
	
	# List of sprites the boss can bump against
	level = None
	
	# this makes sure we don't move the boss too far down
	# when accounting for his ducking
	bent = False
	bent_forward = False
	
	# mark whether or not we can charge
	charge = False
	
	# locks the charge animation to only the walk portion
	charge_lock = False
	
	# toggles the walking back animation
	walk_back = False
	
	# how much the world has shifted
	world_shift = 0
	
	# forces us to wait through two idle animations before charging
	idle_step = 0
	
	# for managing the charge animation
	cur_adjust = 0
	
	# toggles the bang sound
	tog_bang_sound = False
	
	# -- Methods
	def __init__(self):
		""" Constructor method. """
	
		# Call the parents constructor
		super(BossFella, self).__init__()
	
		# Where the current frame is at in each animation
		self.idle_frame = 0
		self.charge_frame = 0
		
		# charge sound
		self.charge_sound = pygame.mixer.Sound(constants.music_dir + 'boss_charge_sound.ogg')
		
		# banging sound once boss hits the end
		self.bang_sound = pygame.mixer.Sound(constants.music_dir + 'bang2.ogg')
		
		sprite_sheet = SpriteSheet(constants.art_dir + "boss_idle_spritesheet.png")
		# Loading all left facing idle animation images into a list
		idle_image = sprite_sheet.get_image(26, 0, 110, 208)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(234, 0, 110, 208)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(442, 0, 110, 208)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(650, 0, 118, 208)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(32, 214, 110, 202)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(240, 214, 110, 202)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(448, 214, 110, 202)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(650, 214, 118, 202)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(26, 422, 110, 202)
		self.idle_frames_l.append(idle_image)
		idle_image = sprite_sheet.get_image(234, 416, 110, 208)
		self.idle_frames_l.append(idle_image)
	
		# Loading all left facing and flipping to the right
		idle_image = sprite_sheet.get_image(26, 0, 110, 208)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(234, 0, 110, 208)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(442, 0, 110, 208)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(650, 0, 118, 208)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(32, 214, 110, 202)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(240, 214, 110, 202)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(448, 214, 110, 202)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(650, 214, 118, 202)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(26, 422, 110, 202)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_r.append(idle_image)
		idle_image = sprite_sheet.get_image(234, 416, 110, 208)
		idle_image = pygame.transform.flip(idle_image, True, False)
		self.idle_frames_r.append(idle_image)
		
		sprite_sheet = SpriteSheet(constants.art_dir + 'boss_charge_spritesheet.png')
		# Loading all left facing images for charing animation
		charge_image = sprite_sheet.get_image(45, 0, 111, 208)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(247, 0, 136, 208)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(448, 13, 130, 195)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(650, 19, 169, 169)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(39, 227, 156, 189)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(247, 221, 104, 195)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(455, 221, 97, 195)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(663, 221, 104, 195)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(39, 435, 156, 189)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(234, 435, 169, 189)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(442, 435, 169, 189)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(656, 429, 130, 195)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(39, 630, 136, 202)
		self.charging_frames.append(charge_image)
		charge_image = sprite_sheet.get_image(253, 624, 111, 208)
		self.charging_frames.append(charge_image)
		
		self.image = self.charging_frames[0]
		
		# Set a reference to the image rect.
		self.rect = self.image.get_rect()
	
	def update(self):
		""" Move the boss and run logic for his actions. """
		
		# check direction
		#if self.change_x > 0:
		#	self.direction = "R"
		if self.change_x < 0:
			self.direction = "L"
			
		# idle animation if we aren't moving
		# have it play twice
		if self.idle_step <= 1:
			# turn off walk back animation
			self.walk_back = False
			self.idle_func()
		elif self.idle_step == 2:
			self.charge = True
		elif self.idle_step == 3:
			self.charge = False
			# we are now playing charging animation backwards
			self.walk_back = True
		elif self.idle_step >= 4:
			self.idle_step = 0
		
		# If charging is true, play this animation
		self.charge_func()
		
		self.ai()
		#print self.idle_step
					
	# This is the very simple ai I am making for him.
	# It consists of a single charge attack then he walks back into place.
	def ai(self):
		if self.rect.x > 914 + self.world_shift and self.charge == False:
			self.change_x = 0
			if self.idle_step == 3:
				self.idle_step += 1
			# toggle bang sound
			self.tog_bang_sound = False
		if self.rect.x > 914 + self.world_shift and self.charge == True:
			self.change_x = -6
		if self.rect.x < 60 + self.world_shift:
			self.change_x = 4
			if self.idle_step == 2:
				self.idle_step += 1
			# toggle bang sound off
			if self.tog_bang_sound == False:
				# stops currents sound for the bang noise
				self.bang_sound.play()
				self.tog_bang_sound = True
		self.rect.x += self.change_x
		
	def idle_func(self):
		# Making sure boss is leveled
		if self.cur_adjust != 0:
			self.rect.y -= self.cur_adjust
			self.cur_adjust = 0
		
		if self.direction == "R":
			self.image = self.idle_frames_r[int(round(self.idle_frame))]
			self.idle_frame += 0.1
			
			if int(round(self.idle_frame)) == 4 and self.bent == False:
				self.rect.y += 6
				self.bent = True
			elif int(round(self.idle_frame)) == 9 and self.bent == True:
				self.rect.y -= 6
				self.bent = False
				
			if int(round(self.idle_frame)) == 4 and self.bent_forward == False:
				self.rect.x += 6
				self.bent_forward = True
			elif int(round(self.idle_frame)) == 7 and self.bent_forward == True:
				self.rect.x -= 6
				self.bent_forward = False
			
			if self.idle_frame >= 9:
				self.idle_frame = 0
				self.idle_step += 1
		elif self.direction == "L":
			self.image = self.idle_frames_l[int(round(self.idle_frame))]
			self.idle_frame += 0.1
			
			if int(round(self.idle_frame)) == 4 and self.bent == False:
				self.rect.y += 6
				self.bent = True
			elif int(round(self.idle_frame)) == 9 and self.bent == True:
				self.rect.y -= 6
				self.bent = False
				
			if int(round(self.idle_frame)) == 4 and self.bent_forward == False:
				self.rect.x += 6
				self.bent_forward = True
			elif int(round(self.idle_frame)) == 7 and self.bent_forward == True:
				self.rect.x -= 6
				self.bent_forward = False
			
			
			if self.idle_frame >= 9:
				self.idle_frame = 0
				self.idle_step += 1
					
	def charge_func(self):
		""" Plays the charge animation. """
		if self.charge == True:
			rounded = int(round(self.charge_frame))
			
			if rounded >= 4 and rounded <= 8:
				self.charge_lock = True
			
			# makes it so that the actual charging part of the animation repeats
			if self.charge_lock == True:
				if rounded == 8:
					self.charge_sound.play()
					self.charge_frame = 4
			
			self.image = self.charging_frames[rounded]
			self.charge_frame += 0.2
		
			# Here we level out the bosses height
			self.rect.y -= self.cur_adjust
			if rounded in [1, 12]:
				self.cur_adjust = 6
			elif rounded in [2, 5, 6, 7, 11]:
				self.cur_adjust = 13
			elif rounded in [3, 4, 8, 9, 10]:
				self.cur_adjust = 19
			else:
				self.cur_adjust = 0
			self.rect.y += self.cur_adjust
			
		elif self.walk_back == True:
			rounded = int(round(self.charge_frame))
			# make sure animation playing backwards
			if rounded <= 4 or rounded > 8:
				self.charge_frame = 8
			# plays walking sound at same rate as before
			if rounded == 8:
				self.charge_sound.play()
			self.image = self.charging_frames[rounded]
			# makes animation go backwards
			self.charge_frame -= 0.1
			
			if self.charge_frame > 13:
				self.charge_frame = 0
			
		#if self.charge_frame >= 13:
		#	self.charge_frame = 0