"""
This is where are levels are! We will have two for this game.
The first I'll call world and it will be the main game
before the boss.
The final level is going to be refered to as just boss.
In here the player must defeat the final enemy and acquire the gem!
"""

# make our imports as always
import pygame

import constants

# Allows us to make our invisible platforms
import make_platform

# our boss
from boss_fella import BossFella

# our gem
from gem import Gem

class Level(object):
	""" Super-class for our levels. Children will further define them. """
	
	# List of sprites to be used. Add/remove as needed
	# also, these are place holders. May be removed later
	platform_list = None
	enemy_list = None
	next_level_list = None
	boss_list = None
	
	# Background image. The vibe factory I might say!
	background = None
	
	# Foreground image. Give the game a little depth will ya?
	foreground = None
	
	# the ending credits
	credits = None
	
	# How far this world has been scrolled left/right
	world_shift = 0
	# How far this world has been scrolled up/down
	world_shift_y = 0
	# the limit should be adjusted for the level. 
	# be sure to alter this when initializing! Set to None for now.
	# level_limit = None
	
	def __init__(self, player):
		""" Constructor. Pass in a handle to player. Needed for when moving platforms
			that collide with the player."""
			
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.next_level_list = pygame.sprite.Group()
		self.boss_list = pygame.sprite.Group()
		# this makes an instance of our player thus allowing us to play!
		self.player = player
		
	def update(self):
		""" Update everything in this level. """
		
		self.platform_list.update()
		self.enemy_list.update()
		self.next_level_list.update()
		self.boss_list.update()
		
	def draw(self, screen):
		""" Draw everything on this level. """
		
		# Draw the background
		# We can adjust the background to be shifted slower than the sprites
		# to giving a feeling of depth. For now, I'll leave this off until I update
		# my art assets. 
		# for a slowed background effect do the following:
		#	screen.blit(self.background, (self.world_shift // 3, 0))
		# for now, doing the following until we can properly implement this
		screen.fill(constants.overworld_color)
		
		# Put back in later if needed:
		# screen.blit(self.background, (self.world_shift // 3, self.world_shift_y))
		
		# the line above replacement
		screen.blit(self.background, (self.world_shift, self.world_shift_y))
		
		# Draw all the sprite lists that we have
		#self.platform_list.draw(screen)
		#self.enemy_list.draw(screen)
		#self.next_level_list.draw(screen)
		self.boss_list.draw(screen)
		
	def draw_fg(self, screen, roll):
		""" Draws the foreground elements. """
		
		# leaving blank until credits
		pass
		
	def shift_world(self, shift_x, shift_y): # add a shift_y!
		""" When the user moves left/right and we need to scroll everything: """
		
		# This works for shifting along the x-axis. Redo this for the y-axis!
		
		# Keep track of the shift amount
		self.world_shift += shift_x
		self.world_shift_y += shift_y
		
		# Go through all the sprite lists and shift
		for platform in self.platform_list:
			platform.rect.x += shift_x
			platform.rect.y += shift_y
			
		for enemy in self.enemy_list:
			enemy.rect.x += shift_x
			enemy.rect.y += shift_y
			
		for level in self.next_level_list:
			level.rect.x += shift_x
			level.rect.y += shift_y
		
		for boss in self.boss_list:
			boss.rect.x += shift_x
			boss.rect.y += shift_y
			

class OverWorld(Level):
	""" Define the Over World. """
	
	def __init__(self, player):
		""" Create Over World. """
		
		# Call the parent constructor
		Level.__init__(self, player)
		
		# load the background
		self.background = pygame.image.load(constants.art_dir + 'overworld_testing.png').convert()
		# allow white spots to be transparent if there is no alpha
		self.background.set_colorkey(constants.white)
		
		# Leaving out foreground for now
		self.foreground = None
		
		# set the directory where we retrieve the ground and enemy collisions from
		self.ground = 'ground_collision.png'
		
		# Array with all our platforms from ground_collision.png
		# Sadly, we have to manually put each one in
		# based off of coordinates found in photoshop.
		# Since I'm not going for tiles, this makes things
		# more difficult but we can manage.
		plat_a = (144, 676, 638, 21)
		plat_b = (126, 44, 20, 652)
		plat_c = (776, 642, 74, 35)
		plat_d = (843, 602, 73, 42)
		plat_e = (914, 617, 71, 20)
		plat_f = (974, 524, 299, 96)
		plat_g = (1271, 578, 58, 255)
		plat_h = (1268, 825, 81, 70)
		plat_i = (1268, 895, 43, 326)
		plat_j = (1302, 1210, 43, 133)
		plat_k = (1267, 1342, 43, 97)
		plat_l = (145, 1, 2153, 51)
		plat_m = (2289, 49, 49, 104)
		plat_n = (2248, 148, 50, 256)
		plat_o = (2137, 396, 122, 24)
		plat_p = (2137, 416, 37, 303)
		plat_q = (2097, 716, 109, 65)
		plat_r = (2174, 780, 39, 193)
		plat_s = (2211, 947, 131, 27)
		plat_t = (2323, 972, 29, 193)
		plat_u = (2350, 1105, 201, 60)
		plat_v = (2549, 991, 50, 115)
		plat_w = (2597, 839, 74, 159)
		plat_x = (2669, 837, 193, 18)
		plat_y = (2850, 853, 70, 272)
		plat_z = (2918, 958, 64, 210)
		
		plat_a2 = (2979, 825, 174, 146)
		plat_b2 = (3145, 766, 306, 61)
		plat_c2 = (3423, 825, 34, 203)
		plat_d2 = (3423, 1027, 126, 57)
		plat_e2 = (3547, 1026, 110, 150)
		plat_f2 = (3655, 972, 51, 119)
		plat_g2 = (3705, 963, 135, 35)
		plat_h2 = (2174, 1350, 51, 90)
		plat_i2 = (2222, 1350, 1618, 25)
		plat_j2 = (2665, 1273, 60, 79)
		plat_k2 = (2722, 1199, 52, 154)
		plat_l2 = (3147, 1274, 78, 78)
		plat_m2 = (3223, 1124, 109, 228)
		plat_n2 = (3330, 1199, 46, 152)
		plat_o2 = (3828, 993, 12, 366)
		
		
		tree_1 = (1378, 481, 90, 76)
		tree_2 = (1996, 525, 105, 77)
		tree_3 = (1572, 676, 77, 73)
		tree_4 = (1447, 975, 105, 76)
		tree_5 = (1650, 1124, 76, 76)
		tree_6 = (1947, 1289, 89, 70)
		
		level = [[plat_a, plat_a[0], plat_a[1]],
				[plat_b, plat_b[0], plat_b[1]],
				[plat_c, plat_c[0], plat_c[1]],
				[plat_d, plat_d[0], plat_d[1]],
				[plat_e, plat_e[0], plat_e[1]],
				[plat_f, plat_f[0], plat_f[1]],
				[plat_g, plat_g[0], plat_g[1]],
				[plat_h, plat_h[0], plat_h[1]],
				[plat_i, plat_i[0], plat_i[1]],
				[plat_j, plat_j[0], plat_j[1]],
				[plat_k, plat_k[0], plat_k[1]],
				[plat_l, plat_l[0], plat_l[1]],
				[plat_m, plat_m[0], plat_m[1]],
				[plat_n, plat_n[0], plat_n[1]],
				[plat_o, plat_o[0], plat_o[1]],
				[plat_p, plat_p[0], plat_p[1]],
				[plat_q, plat_q[0], plat_q[1]],
				[plat_r, plat_r[0], plat_r[1]],
				[plat_s, plat_s[0], plat_s[1]],
				[plat_t, plat_t[0], plat_t[1]],
				[plat_u, plat_u[0], plat_u[1]],
				[plat_v, plat_v[0], plat_v[1]],
				[plat_w, plat_w[0], plat_w[1]],
				[plat_x, plat_x[0], plat_x[1]],
				[plat_y, plat_y[0], plat_y[1]],
				[plat_z, plat_z[0], plat_z[1]],
				[plat_a2, plat_a2[0], plat_a2[1]],
				[plat_b2, plat_b2[0], plat_b2[1]],
				[plat_c2, plat_c2[0], plat_c2[1]],
				[plat_d2, plat_d2[0], plat_d2[1]],
				[plat_e2, plat_e2[0], plat_e2[1]],
				[plat_f2, plat_f2[0], plat_f2[1]],
				[plat_g2, plat_g2[0], plat_g2[1]],
				[plat_h2, plat_h2[0], plat_h2[1]],
				[plat_i2, plat_i2[0], plat_i2[1]],
				[plat_j2, plat_j2[0], plat_j2[1]],
				[plat_k2, plat_k2[0], plat_k2[1]],
				[plat_l2, plat_l2[0], plat_l2[1]],
				[plat_m2, plat_m2[0], plat_m2[1]],
				[plat_n2, plat_n2[0], plat_n2[1]],
				[plat_o2, plat_o2[0], plat_o2[1]],
				[tree_1, tree_1[0], tree_1[1]],
				[tree_2, tree_2[0], tree_2[1]],
				[tree_3, tree_3[0], tree_3[1]],
				[tree_4, tree_4[0], tree_4[1]],
				[tree_5, tree_5[0], tree_5[1]],
				[tree_6, tree_6[0], tree_6[1]],
				]
		
		# Here we put those platforms in place
		for platform in level:
			block = make_platform.Platform(platform[0], self.ground)
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
		
		# Here we are constructing our enemies such as spike traps and falling
		fall_death = (1308, 1412, 865,  28)
		
		# First set of spikes
		spike_a = (2669,  854, 183, 142)
		spike_b = (2695,  995,  22,  19)
		spike_c = (2703, 1013,   8,  19)
		spike_d = (2746,  995,  33,  49)
		spike_e = (2756, 1043,  13,  31)
		spike_f = (2813, 1025,  14,  23)
		spike_g = (2808,  995,  25,  31)
		
		# Second spike
		spike_h = (2866, 1334, 32, 17)
		spike_i = (2869, 1319, 23, 16)
		spike_j = (2873, 1302, 10, 18)
		spike_k = (2875, 1291,  4, 12)
		
		# Third spike
		spike_l = (3073, 1295, 51, 57)
		spike_m = (3082, 1237, 26, 59)
		spike_n = (3088, 1199, 10, 39)
		spike_o = (3090, 1182,  5, 18)
		
		# Fourth and final spike
		spike_p = (3251, 1110, 67, 15)
		spike_q = (3262, 1076, 50, 34)
		spike_r = (3275, 1038, 29, 39)
		spike_s = (3284, 1012, 13, 27)
		# seems to be giving player unfair stress
		#spike_t = (3289,  996,  6, 17)
		
		level_enemies = [[fall_death, fall_death[0], fall_death[1]],
						[spike_a, spike_a[0], spike_a[1]],
						[spike_b, spike_b[0], spike_b[1]],
						[spike_c, spike_c[0], spike_c[1]],
						[spike_d, spike_d[0], spike_d[1]],
						[spike_e, spike_e[0], spike_e[1]],
						[spike_f, spike_f[0], spike_f[1]],
						[spike_g, spike_g[0], spike_g[1]],
						[spike_h, spike_h[0], spike_h[1]],
						[spike_i, spike_i[0], spike_i[1]],
						[spike_j, spike_j[0], spike_j[1]],
						[spike_k, spike_k[0], spike_k[1]],
						[spike_l, spike_l[0], spike_l[1]],
						[spike_m, spike_m[0], spike_m[1]],
						[spike_n, spike_n[0], spike_n[1]],
						[spike_o, spike_o[0], spike_o[1]],
						[spike_p, spike_p[0], spike_p[1]],
						[spike_q, spike_q[0], spike_q[1]],
						[spike_r, spike_r[0], spike_r[1]],
						[spike_s, spike_s[0], spike_s[1]],
						#[spike_t, spike_t[0], spike_t[1]],
						]
						
		# Now we put those enemies in their place
		for enemy in level_enemies:
			kill_block = make_platform.Platform(enemy[0], self.ground)
			kill_block.rect.x = enemy[1]
			kill_block.rect.y = enemy[2]
			kill_block.player = self.player
			self.enemy_list.add(kill_block)
		
		# this portion sets up the block that allows us to advance to the next level
		next_level = (3815, 993, 16, 365)
		
		level_block = make_platform.Platform(next_level, self.ground)
		level_block.rect.x = next_level[0]
		level_block.rect.y = next_level[1]
		level_block.player = self.player
		self.next_level_list.add(level_block)
		
# Boss level	
class Boss(Level):
	""" Definition for Boss level. """
	
	def __init__(self, player):
		""" Create level Boss. """
		
		# Call the parent constructor
		Level.__init__(self, player)
		
		# Set background
		self.background = pygame.image.load(constants.art_dir + 'boss_testing.png').convert()
		# set white spots transparent
		self.background.set_colorkey(constants.white)
		
		# leaving foreground out for now
		self.foreground = None
		
		# setting up collisions for ground and enemies
		self.ground = 'boss_ground_collision.png'
		
		# Array with all our platforms
		# thus defining the ground
		plat_a = (   0,  250,   24, 373)
		plat_b = (  23,  600,  293,  18)
		plat_c = ( 310,  573,  217,  35)
		plat_d = ( 523,  538,  184,  42)
		plat_e = (   0,  231,   50,  21)
		plat_f = ( 705,  526,   50,  33)
		plat_g = ( 750,  500,  114,  60)
		plat_h = ( 857,  550,   43,  26)
		plat_i = ( 898,  567,   28,  36)
		plat_j = ( 864,  595,   36,  32)
		plat_k = ( 839,  615,   38,  35)
		plat_l = ( 816,  646,   35,  28)
		plat_m = ( 788,  665,   37,  35)
		plat_n = ( 763,  692,   37,  33)
		plat_o = ( 591,  720,  185,  31)
		plat_p = ( 270,  736,  327,  38)
		plat_q = (  28,  737,  243,  46)
		plat_r = (  26,  781,   33, 623)
		plat_s = (  54, 1397, 1207,  15)
		plat_t = (1248,  869,   23, 535)
		plat_u = (1195, 857, 68, 19)
		plat_v = (1123, 866, 79, 35)
		plat_w = (1044, 858, 93, 18)
		plat_x = (947, 865, 102, 42)
		plat_y = (797, 898, 157, 29)
		plat_z = (823, 875, 92, 27)
		plat_a2 = (900, 825, 32, 58)
		plat_b2 = (925, 800, 42, 37)
		plat_c2 = (952, 777, 59, 33)
		plat_d2 = (1002, 753, 32, 31)
		plat_e2 = (1024, 723, 64, 40)
		plat_f2 = (1077, 701, 83, 30)
		plat_g2 = (1150, 649, 57, 64)
		plat_h2 = (1198, 599, 46, 59)
		plat_i2 = (1234, 475, 24, 132)
		plat_j2 = (1248, 312, 23, 169)
		plat_k2 = (1223, 298, 40, 26)
		plat_l2 = (1147, 270, 85, 36)
		plat_m2 = (1074, 243, 88, 37)
		plat_n2 = (874, 209, 216, 44)
		plat_o2 = (824, 170, 60, 57)
		plat_p2 = (691, 155, 154, 23)
		plat_q2 = (600, 150, 100, 75)
		plat_r2 = (548, 139, 71, 35)
		plat_s2 = (470, 130, 89, 21)
		plat_t2 = (300, 136, 177, 65)
		plat_u2 = (277, 134, 35, 39)
		plat_v2 = (143, 114, 143, 40)
		plat_w2 = (67, 133, 84, 70)
		plat_x2 = (46, 185, 28, 41)
		plat_y2 = (19, 209, 33, 25)
		
		# the additional platforms I made to fix the fight
		new_a = (924, 1019, 128, 57)
		new_b = (874, 994, 70, 32)
		new_c = (505, 973, 385, 28)
		new_d = (699, 923, 198, 54)
		new_e = (398, 998, 139, 82)
		new_f = (323, 1072, 154, 28)
		new_g = (247, 1096, 130, 30)
		#new_h = (813, 1010, 120, 42)
		#new_i = (910, 1040, 142, 35)
		new_j = (1024, 1067, 71, 58)
		new_k = (1071, 1118, 182, 59)
		
		level = [[plat_a, plat_a[0], plat_a[1]],
				[plat_b, plat_b[0], plat_b[1]],
				[plat_c, plat_c[0], plat_c[1]],
				[plat_d, plat_d[0], plat_d[1]],
				[plat_e, plat_e[0], plat_e[1]],
				[plat_f, plat_f[0], plat_f[1]],
				[plat_g, plat_g[0], plat_g[1]],
				[plat_h, plat_h[0], plat_h[1]],
				[plat_i, plat_i[0], plat_i[1]],
				[plat_j, plat_j[0], plat_j[1]],
				[plat_k, plat_k[0], plat_k[1]],
				[plat_l, plat_l[0], plat_l[1]],
				[plat_m, plat_m[0], plat_m[1]],
				[plat_n, plat_n[0], plat_n[1]],
				[plat_o, plat_o[0], plat_o[1]],
				[plat_p, plat_p[0], plat_p[1]],
				[plat_q, plat_q[0], plat_q[1]],
				[plat_r, plat_r[0], plat_r[1]],
				[plat_s, plat_s[0], plat_s[1]],
				[plat_t, plat_t[0], plat_t[1]],
				[plat_u, plat_u[0], plat_u[1]],
				[plat_v, plat_v[0], plat_v[1]],
				[plat_w, plat_w[0], plat_w[1]],
				[plat_x, plat_x[0], plat_x[1]],
				[plat_y, plat_y[0], plat_y[1]],
				[plat_z, plat_z[0], plat_z[1]],
				[plat_a2, plat_a2[0], plat_a2[1]],
				[plat_b2, plat_b2[0], plat_b2[1]],
				[plat_c2, plat_c2[0], plat_c2[1]],
				[plat_d2, plat_d2[0], plat_d2[1]],
				[plat_e2, plat_e2[0], plat_e2[1]],
				[plat_f2, plat_f2[0], plat_f2[1]],
				[plat_g2, plat_g2[0], plat_g2[1]],
				[plat_h2, plat_h2[0], plat_h2[1]],
				[plat_i2, plat_i2[0], plat_i2[1]],
				[plat_j2, plat_j2[0], plat_j2[1]],
				[plat_k2, plat_k2[0], plat_k2[1]],
				[plat_l2, plat_l2[0], plat_l2[1]],
				[plat_m2, plat_m2[0], plat_m2[1]],
				[plat_n2, plat_n2[0], plat_n2[1]],
				[plat_o2, plat_o2[0], plat_o2[1]],
				[plat_p2, plat_p2[0], plat_p2[1]],
				[plat_q2, plat_q2[0], plat_q2[1]],
				[plat_r2, plat_r2[0], plat_r2[1]],
				[plat_s2, plat_s2[0], plat_s2[1]],
				[plat_t2, plat_t2[0], plat_t2[1]],
				[plat_u2, plat_u2[0], plat_u2[1]],
				[plat_v2, plat_v2[0], plat_v2[1]],
				[plat_w2, plat_w2[0], plat_w2[1]],
				[plat_x2, plat_x2[0], plat_x2[1]],
				[plat_y2, plat_y2[0], plat_y2[1]],
				[new_a, new_a[0], new_a[1]],
				[new_b, new_b[0], new_b[1]],
				[new_c, new_c[0], new_c[1]],
				[new_d, new_d[0], new_d[1]],
				[new_e, new_e[0], new_e[1]],
				[new_f, new_f[0], new_f[1]],
				[new_g, new_g[0], new_g[1]],
				#[new_h, new_h[0], new_h[1]],
				#[new_i, new_i[0], new_i[1]],
				[new_j, new_j[0], new_j[1]],
				[new_k, new_k[0], new_k[1]],
				]
				
		# Now we put the platforms in place
		for platform in level:
			block = make_platform.Platform(platform[0], self.ground)
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
			
		# this portion sets up the gem that allows us to go to the
		# next level. The win screen!
		self.gem = Gem()
		
		self.gem.rect.x = 1160
		self.gem.rect.y = 1234
		self.gem.player = self.player
		self.next_level_list.add(self.gem)
			
		# making an instance of our boss
		self.final_boss = BossFella()
		
		self.final_boss.rect.x = 915
		self.final_boss.rect.y = 1186
		self.final_boss.player = self.player
		self.boss_list.add(self.final_boss)
		
	def update(self):
		""" Update everything in this level. """
		
		self.platform_list.update()
		self.enemy_list.update()
		self.next_level_list.update()
		
		self.final_boss.world_shift = self.world_shift
		
		self.boss_list.update()
		
	def draw(self, screen):
		""" Draw everything on this level. """
		
		# Draw the background
		# We can adjust the background to be shifted slower than the sprites
		# to giving a feeling of depth. For now, I'll leave this off until I update
		# my art assets. 
		# for a slowed background effect do the following:
		#	screen.blit(self.background, (self.world_shift // 3, 0))
		# for now, doing the following until we can properly implement this
		screen.fill(constants.photoshop_color)
		
		# Put back in later if needed:
		# screen.blit(self.background, (self.world_shift // 3, self.world_shift_y))
		
		# the line above replacement
		screen.blit(self.background, (self.world_shift, self.world_shift_y))
		
		# Draw all the sprite lists that we have
		#self.platform_list.draw(screen)
		#self.enemy_list.draw(screen)
		self.next_level_list.draw(screen)
		self.boss_list.draw(screen)

# A rewarding screen that let's the player know
# they won after obtaining the gem
class WinScreen(Level):
	""" Create Win Screen. """
	
	def __init__(self, player):
		""" Create Win Screen. """
		
		# Call the parent constructor
		Level.__init__(self, player)
		
		# loading our background image
		self.background = pygame.image.load(constants.art_dir + "winscreen.png").convert()
		# white is the alpha
		self.background.set_colorkey(constants.white)
		
		# no foreground, for now
		self.foreground = pygame.image.load(constants.art_dir + 'winscreen_fg.png').convert()
		self.foreground.set_colorkey(constants.white)
		
		# the ending credits that will play once the player reaches the end
		self.credits = pygame.image.load(constants.art_dir + 'sworcery_credits.png').convert()
		self.credits.set_colorkey(constants.black)
		
		# array with all our platforms
		# thus defining the ground
		plat_a = (881, 0, 53, 661)
		plat_b =  (881, 658, 7440, 63)
		plat_c = (8262, 0, 60, 658)
		
		level = [[plat_a, plat_a[0], plat_a[1]],
				 [plat_b, plat_b[0], plat_b[1]],
				 [plat_c, plat_c[0], plat_c[1]],
				 ]
				 
		# now we put the platforms in place
		for platform in level:
			block = make_platform.Platform(platform[0], 'winscreen.png')
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
	
	# credits are now drawn too along with the foreground!
	def draw_fg(self, screen, roll):
		""" Draws the foreground elements. """
		
		# After the background and player is drawn, we call this to draw the fg!
		
		screen.blit(self.foreground, (self.world_shift, self.world_shift_y)) # took out plus 1
		
		# also throwing in the credits to be drawn with it
		screen.blit(self.credits, (self.world_shift, self.world_shift_y - roll))
