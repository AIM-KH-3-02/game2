import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000
win=pygame.display.set_mode((screen_width, screen_height))
tile_size = 50
pygame.display.set_caption("Platformer")
walkRight = [pygame.image.load('pygame_right_1.png'),
pygame.image.load('pygame_right_2.png'), pygame.image.load('pygame_right_3.png'),
pygame.image.load('pygame_right_4.png'), pygame.image.load('pygame_right_5.png'),
pygame.image.load('pygame_right_6.png'),]
walkLeft = [pygame.image.load('pygame_left_1.png'),
pygame.image.load('pygame_left_2.png'), pygame.image.load('pygame_left_3.png'),
pygame.image.load('pygame_left_4.png'), pygame.image.load('pygame_left_5.png'),
pygame.image.load('pygame_left_6.png'),]

bg = pygame.image.load('sky.jpg')
playerStand = pygame.image.load('pygame_idle.png')

clok = pygame.time.Clock()
x = 50
y = 925
widht = 60
height = 71
speed = 5

jump = False
jumpcoup = 10
left = False
right = False
walkcout = 0

def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(win, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(win, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))



class World():
	def __init__(self, data):
		self.tile_list = []

		#load images
		dirt_img = pygame.image.load('dirt.png')
		grass_img = pygame.image.load('grass.png')

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def d(self):
		for tile in self.tile_list:
			win.blit(tile[0], tile[1])


world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


world = World(world_data)

def draw():
    global walkcout
    win.blit(bg, (0, 0))
    if walkcout + 1 >=30:
        walkcout = 0

    if left:
        win.blit(walkLeft[walkcout // 5], (x, y))
        walkcout += 1
    elif right:
        win.blit(walkRight[walkcout // 5], (x, y))
        walkcout += 1
    else:
        win.blit(playerStand, (x, y))

    pygame.display.update()

run = True
while  run:
    clok.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1000 - widht - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        walkcout = 0

    if not(jump):
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpcoup >= -10:
            if jumpcoup < 0:
                y += (jumpcoup ** 2) / 2
            else:
                y -= (jumpcoup ** 2) / 2
            jumpcoup -= 1
        else:
            jump = False
            jumpcoup = 10

    world.d()

    draw_grid()

    draw()

pygame.quit()
