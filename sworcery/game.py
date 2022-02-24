"""
This holds the class 'Game'.
The purpose is to give the main file 'sworcery' everything
the game needs to run.

In other words, this is the backbone of our game engine.
"""

# Make our imports
import pygame
from pygame.locals import*
# For constant variables, values, etc...
import constants
# for our levels such as overworld and boss
import levels
# for our player
from fella import Player
# for our boss
from boss_fella import BossFella


class Game(object):
	""" Our Game class! Provides everything sworcery.py needs to work! """
	
	# ----- Class Methods -----
	
	def __init__(self):
		""" Constructor. Be sure to initialize what we need! """
		
		# Create our player
		self.player = Player()
		
		# Create all the levels
		self.level_list = []
		self.level_list.append(levels.OverWorld(self.player))
		self.level_list.append(levels.Boss(self.player))
		self.level_list.append(levels.WinScreen(self.player))
		
		# Set current level
		self.current_level_no = 0 # temp!
		self.current_level = self.level_list[self.current_level_no]
		
		# Makes lists
		self.active_sprite_list = pygame.sprite.Group()
		self.player.level = self.current_level 
		
		self.player.rect.x = 200
		# subtracting 300 just in case errors when testing the green
		self.player.rect.y = constants.screen_height - self.player.rect.height - 50
		self.active_sprite_list.add(self.player)
		
		# loading our music
		pygame.mixer.music.load(constants.music_dir + 'title.ogg')
		pygame.mixer.music.play()
		
		# puts us on the next track
		# loading our music
		self.next_song = False
		
		# the rate the credits roll by at
		self.credit_rate = 0
		
	def process_events(self):
		""" Process all events and return true if game is over. """
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
				
			# Player movement
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					self.player.stop_a = False
					self.player.go_left()
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					self.player.go_right()
					self.player.stop_d = False
				if event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP:
					self.player.jump()
				
			
			#Stops player from moving when button released
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a or event.key == pygame.K_LEFT and self.player.change_x < 0:
					self.player.stop_a = True
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT and self.player.change_x > 0:
					self.player.stop_d = True
				if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
					self.player.now_jumping = False
					
			if self.player.stop_a == True and self.player.stop_d == True:
				self.player.stop()
				
		
		# If the player died then the game ends
		if self.player.game_over == True:
			print "You are dead! "
			return True
			
		if self.player.next_level == True:
			print "Level Up!"
			self.current_level_no += 1
			self.current_level = self.level_list[self.current_level_no]
			self.player.level = self.current_level
			self.player.rect.x = 50
			self.player.rect.y += 100
			self.player.next_level = False
			
		# adjust player position and load new song	
		if self.current_level_no == 2 and self.next_song == False:
			# loading our music
			pygame.mixer.music.stop()
			pygame.mixer.music.load(constants.music_dir + 'registration2.ogg') # temp
			pygame.mixer.music.play()
			
			self.next_song = True
			
			# adjust player position. 
			self.player.rect.x = 1280
			
		# play sound when player walks
		if int(round(self.player.walk_frame)) == 5 and self.player.tog_walk_sound == False:
			self.player.walk_sound.play()
			self.player.tog_walk_sound = True
		if int(round(self.player.walk_frame)) == 12 and self.player.tog_walk_sound == True:
			self.player.walk_sound.play()
			self.player.tog_walk_sound = False
		
		return False
		
	def run_logic(self):
		""" Runs each frame. Update positions, check collisions, etc... """
		
		# Update the player
		self.active_sprite_list.update()
		
		# Update items in the level
		# ----- Leaving off Temp -----
		self.current_level.update()
		
		# As player moves near the right, shift world to the left (-x)
		if self.player.rect.right >= 900:
			self.diff = self.player.rect.right - 900
			self.player.rect.right = 900
			self.current_level.shift_world(-self.diff, 0)
			
		# As player moves near the left, shift world to the right (+x)
		if self.player.rect.left <= 300:
			self.diff = 300 - self.player.rect.left
			self.player.rect.left = 300
			self.current_level.shift_world(self.diff, 0)
			
		# As player moves down, shift world up
		if self.player.rect.bottom >= 500:
			self.diff = self.player.rect.bottom - 500
			self.player.rect.bottom = 500
			self.current_level.shift_world(0, -self.diff)
	
		
	def display_frame(self, screen):
		""" Everything that needs to be seen/drawn gets displayed here. """
		
		# draw the background
		self.current_level.draw(screen)
		
		# Draws player and other sprites in this list
		self.active_sprite_list.draw(screen)
		
		# play credits	
		if self.current_level_no == 2 and self.current_level.world_shift <= -7250:
			if self.credit_rate <= 3230:
				self.credit_rate += 1
		
		
		# draw the foreground and credits
		self.current_level.draw_fg(screen, self.credit_rate)