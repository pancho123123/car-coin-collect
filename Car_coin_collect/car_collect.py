import pygame, random, time, math
from random import randint
from utils import scale_image, blit_rotate_center, blit_text_center
pygame.font.init()

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)

GRASS = pygame.image.load("img/pasto1.png")
TRACK = pygame.image.load("img/fond.png")

TRACK_BORDER = pygame.image.load("img/fond_border.png")
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)

FINISH = pygame.image.load("img/finish.png")
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POSITION = (20,200)

RED_CAR = pygame.image.load("img/playerup.png")
GREEN_CAR = pygame.image.load("img/playerup.png")

WIDTH ,HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car collect")

MAIN_FONT = pygame.font.SysFont("comicsans", 44)

PATH = [(76, 139), (61, 176), (82, 175), (72, 121), (94, 128), (91, 111), (98, 95), 
(114, 107), (115, 88), (134, 105), (144, 84), (157, 103), (170, 83), (178, 105), (196, 84),
 (200, 107), (218, 84), (224, 103), (244, 82), (254, 104), (113, 97), (135, 92), (155, 92), 
 (186, 91), (206, 94), (233, 90), (264, 90), (286, 91), (308, 91), (325, 93), (343, 93), (362, 92),
  (382, 95), (398, 92), (418, 95), (440, 89), (455, 93), (475, 90), (492, 91), (509, 91), (265, 81), 
  (282, 80), (270, 101), (285, 100), (300, 79), (302, 98), (325, 82), (328, 107), (345, 79), (352, 100),
   (370, 83), (373, 104), (389, 80), (397, 106), (415, 82), (420, 109), (430, 80), (438, 102), (453, 78), 
   (460, 104), (478, 79), (474, 104), (496, 82), (496, 99), (516, 80), (518, 106), (532, 80), (533, 94), 
   (533, 104), (547, 83), (547, 93), (548, 100), (562, 84), (562, 93), (563, 104), (582, 85), (582, 94), 
   (583, 101), (595, 86), (612, 85), (630, 84), (642, 84), (658, 87), (670, 83), (683, 84), (586, 94), 
   (598, 93), (611, 95), (622, 95), (635, 94), (653, 95), (664, 92), (679, 92), (592, 105), (612, 103), 
   (627, 105), (642, 105), (661, 108), (676, 108), (700, 83), (722, 84), (740, 85), (762, 86), (782, 87), 
   (694, 94), (708, 93), (727, 96), (746, 97), (768, 98), (694, 107), (712, 105), (730, 105), (742, 107), 
   (757, 107), (768, 106), (786, 99), (788, 105), (798, 89), (802, 97), (804, 102), (815, 84), (819, 95),
    (820, 104), (837, 88), (838, 92), (841, 101), (854, 84), (855, 91), (855, 98), (869, 88), (872, 96), 
	(877, 104), (882, 84), (890, 93), (895, 102), (899, 85), (906, 92), (913, 99), (917, 82), (928, 89), 
	(934, 97), (928, 106), (946, 106), (957, 105), (973, 105), (986, 106), (998, 107), (1011, 108), (935, 79), 
	(948, 79), (962, 79), (980, 78), (992, 78), (1005, 81), (1017, 83), (943, 90), (955, 90), (966, 91), 
	(980, 90), (995, 91), (1010, 90), (1028, 92), (1038, 98), (1045, 109), (1054, 125), (1066, 143), 
	(1026, 111), (1030, 119), (1040, 129), (1046, 145), (1055, 140), (1041, 159), (1053, 158), (1066, 159), 
	(1065, 170), (1054, 171), (1045, 173), (1042, 185), (1057, 186), (1067, 187), (1044, 198), (1057, 199), 
	(1068, 205), (1047, 213), (1058, 213), (1066, 224), (1046, 223), (1054, 223), (1064, 240), (1049, 238), 
	(1043, 253), (1060, 256), (1071, 265), (1047, 266), (1060, 270), (1046, 281), (1065, 282), (1043, 299), 
	(1056, 298), (1069, 298), (1045, 313), (1057, 314), (1067, 317), (1043, 325), (1051, 326), (1063, 336), 
	(1046, 339), (1065, 348), (1047, 358), (1072, 370), (1053, 371), (1066, 387), (1052, 387), (1059, 405), 
	(1047, 406), (1045, 395), (1043, 374), (1069, 398), (1066, 415), (1058, 424), (1054, 438), (1039, 445), 
	(1029, 452), (1014, 462), (1009, 441), (1024, 432), (1039, 420), (1044, 428), (1033, 437), (1019, 444), 
	(999, 442), (1006, 453), (998, 464), (982, 440), (122, 465), (147, 442), (980, 463), (620, 440), 
	(391, 458), (255, 441), (217, 462), (498, 440), (701, 464), (752, 440), (828, 464), (799, 443), 
	(874, 466), (843, 440), (907, 464), (874, 440), (849, 453), (893, 452), (912, 441), (924, 463), 
	(928, 441), (942, 463), (934, 452), (920, 453), (949, 442), (952, 453), (968, 442), (978, 452), 
	(963, 461), (818, 443), (855, 465), (860, 444), (834, 450), (811, 455), (796, 460), (778, 443), 
	(782, 463), (766, 452), (752, 461), (740, 443), (731, 463), (722, 439), (725, 452), (709, 440), 
	(693, 440), (677, 443), (664, 440), (649, 442), (636, 444), (711, 452), (695, 454), (678, 455), 
	(685, 465), (668, 463), (664, 451), (652, 453), (653, 463), (639, 464), (639, 454), (60, 225), 
	(88, 225), (75, 228), (77, 439), (82, 410), (65, 388), (87, 340), (62, 299), (90, 262), (63, 241), 
	(87, 240), (89, 159), (63, 150), (65, 136), (91, 144), (83, 122), (104, 116), (77, 106), (63, 264), 
	(86, 297), (61, 338), (88, 372), (68, 364), (87, 391), (66, 417), (101, 425), (101, 450), (115, 442), 
	(93, 437), (128, 449), (173, 442), (168, 460), (212, 442), (305, 466), (289, 443), (343, 441), (437, 440),
	 (469, 463), (545, 439), (576, 440), (595, 462), (559, 465), (526, 465), (501, 465), (467, 439), 
	 (426, 465), (452, 454), (415, 451), (393, 435), (369, 440), (364, 464), (340, 464), (315, 440), 
	 (251, 461), (236, 442), (235, 451), (220, 449), (200, 451), (192, 439), (187, 452), (161, 453), 
	 (143, 456), (153, 467), (138, 466), (110, 460), (87, 449), (90, 419), (80, 424), (92, 403), (73, 402), 
	 (77, 378), (84, 357), (74, 346), (73, 322), (90, 316), (61, 316), (59, 281), (73, 277), (85, 276), 
	 (77, 253), (59, 252), (63, 400), (62, 376), (62, 353), (84, 329), (74, 304), (74, 292), (239, 103), 
	 (311, 107), (273, 452), (273, 440), (271, 462), (287, 461), (306, 454), (318, 463), (326, 451), 
	 (231, 464), (199, 464), (183, 464), (406, 462), (416, 439), (384, 446), (358, 452), (377, 464), 
	 (432, 453), (447, 464), (453, 443), (482, 453), (482, 443), (467, 450), (499, 452), (520, 440), 
	 (517, 453), (533, 452), (533, 439), (552, 451), (561, 439), (570, 451), (586, 452), (591, 441), 
	 (602, 449), (607, 440), (616, 453), (623, 462), (604, 463), (576, 463), (546, 464), (511, 464), 
	 (486, 463), (402, 446), (136, 439), (343, 111), (361, 109), (488, 110), (502, 110), (719, 465), 
	 (767, 468), (895, 440), (892, 467), (879, 453), (1021, 101), (1041, 119), (864, 112), (908, 109), 
	 (89, 190), (62, 208), (76, 209), (88, 209), (64, 192), (69, 165), (79, 152), (77, 266)]

pygame.init()
pygame.mixer.init()


clock = pygame.time.Clock()



def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_shield_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)



def show_go_screen():
	
	WIN.fill(BLACK, [0,0])
	draw_text1(WIN, "Car collect", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(WIN, "colecta las monedas", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(WIN, "Press q", 20, WIDTH // 2, HEIGHT * 3/4)
	
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

class Moneda(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = mon_images[0]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect.centerx, self.rect.centery = random.choice(PATH)
	
	def update(self):
		pass


class GameInfo():
	LEVELS = 10

	def __init__(self, level=1):
		self.level = level
		self.started = False
		self.level_start_time = 0

	def next_level(self):
		self.level += 1
		self.started = False

	def reset(self):
		self.level = 1
		self.started = False
		self.level_start_time = 0

	def game_finished(self):
		return self.level > self.LEVELS

	def start_level(self):
		self.started = True
		self.level_start_time = time.time()

	def get_level_time(self):
		if not self.started:
			return 0
		return  round(time.time() - self.level_start_time)


class AbstractCar:
	
	def __init__(self, max_vel, rotation_vel):
		self.img = self.IMG
		#self.img.set_colorkey(WHITE)
		self.max_vel = max_vel
		self.vel = 0
		self.rotation_vel = rotation_vel
		self.angle = 0
		self.x, self.y = self.START_POS
		self.acceleration = 0.1
		self.score = 0
		

	def rotate(self, left=False, right=False):
		if left:
			self.angle += self.rotation_vel
		if right:
			self.angle -= self.rotation_vel

	def draw(self,win):
		blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

	def move_forward(self):
		self.vel = min(self.vel + self.acceleration, self.max_vel)
		self.move()

	def move_backward(self):
		self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)
		self.move()

	def move(self):
		radians = math.radians(self.angle)
		vertical = math.cos(radians) * self.vel
		horizontal = math.sin(radians) * self.vel

		self.y -= vertical
		self.x -= horizontal

	def collide(self,mask, x=0 , y=0):
		car_mask = pygame.mask.from_surface(self.img)
		offset = (int(self.x - x), int(self.y - y))
		poi = mask.overlap(car_mask, offset)
		return poi

	def reset(self):
		self.x, self.y = self.START_POS
		self.angle = 0
		self.vel = 0

	

class PlayerCar(AbstractCar):
	IMG = RED_CAR
	START_POS = (60,160)
	

	def reduce_speed(self):
		self.vel = max(self.vel - self.acceleration / 2,0)
		self.move()

	def bounce(self):
		self.vel = -self.vel
		self.move()

class ComputerCar(AbstractCar):
	IMG = GREEN_CAR
	START_POS = (50,160)

	def __init__(self, max_vel, rotation_vel, path=[]):
		super().__init__(max_vel, rotation_vel)
		self.path = path
		self.current_point = 0
		self.vel = max_vel

	def draw_points(self, win):
		for point in self.path:
			pygame.draw.circle(win,(255,0,0), point, 5)

	def draw(self, win):
		super().draw(win)
		#self.draw_points(win)

	def calculate_angle(self):
		target_x , target_y = self.path[self.current_point]
		x_diff = target_x - self.x
		y_diff = target_y - self.y

		if y_diff == 0:
			desired_radian_angle = math.pi / 2
		else:
			desired_radian_angle = math.atan(x_diff/y_diff)

		if target_y > self.y:
			desired_radian_angle += math.pi

		difference_in_angle = self.angle - math.degrees(desired_radian_angle)
		if difference_in_angle >= 180:
			difference_in_angle -= 360

		if difference_in_angle > 0:
			self.angle -= min(self.rotation_vel, abs(difference_in_angle))
		else:
			self.angle += min(self.rotation_vel, abs(difference_in_angle))

	def update_path_point(self):
		target = self.path[self.current_point]
		rect = pygame.Rect(self.x , self.y, self.img.get_width(), self.img.get_height())
		if rect.collidepoint(*target):
			self.current_point += 1


	def move(self):
		if self.current_point >= len(self.path):
			return

		self.calculate_angle()
		self.update_path_point()
		super().move()

	#def next_level(self, level):
		#self.reset()
		#self.vel = self.max_vel + (level -1)*0.2
		#self.current_point = 0


def draw(win,images, player_car, game_info):
	for img, pos in images:
		win.blit(img, pos)

	level_text = MAIN_FONT.render(f"Level {game_info.level}", 1 , (255,255,255))
	win.blit(level_text,(10, HEIGHT - level_text.get_height()-70))

	time_text = MAIN_FONT.render(f"Time: {game_info.get_level_time()}s", 1 , (255,255,255))
	win.blit(time_text,(10, HEIGHT - time_text.get_height()-40))

	vel_text = MAIN_FONT.render(f"Vel: {round(player_car.vel)}px/s", 1 , (255,255,255))
	win.blit(vel_text,(10, HEIGHT - vel_text.get_height()-10))

	player_car.draw(win)
	#computer_car.draw(win)
	pygame.display.update()

def move_player(player_car):
	keys = pygame.key.get_pressed()
	moved = False

	if keys[pygame.K_a]:
		player_car.rotate(left=True)
	if keys[pygame.K_d]:
		player_car.rotate(right=True)
	if keys[pygame.K_w]:
		moved = True
		player_car.move_forward()
	if keys[pygame.K_s]:
		moved = True
		player_car.move_backward()

	if not moved:
		player_car.reduce_speed()

def handle_collision(player_car, game_info):
	if player_car.collide(TRACK_BORDER_MASK) != None:
		player_car.bounce()

	
	player_finish_poi_collide = player_car.collide(FINISH_MASK,*FINISH_POSITION)
	if player_finish_poi_collide != None:
		if player_finish_poi_collide[1] == 0:
			pass#player_car.bounce()
		else:
			pass
			#game_info.next_level()
			#player_car.reset()
			#computer_car.next_level(game_info.level)

mon_images = []
mon_list = ["img/mon.png"]
for img in mon_list:
	mon_images.append(pygame.image.load(img).convert())

Run = True
clock = pygame.time.Clock()
images = [(TRACK,(0,0)), (FINISH,(FINISH_POSITION)), (TRACK_BORDER,(0,0))]
player_car = PlayerCar(8,8)
#computer_car = ComputerCar(2,6,PATH)
game_info = GameInfo()
moneda = Moneda()

all_sprites = pygame.sprite.Group()
all_sprites.add(moneda)
mon_list = pygame.sprite.Group()
player_car.score = 0

while Run:
	clock.tick(60)

	
	draw(WIN, images, player_car, game_info)
	all_sprites.draw(WIN)
	draw_text1(WIN, str(player_car.score), 25, WIDTH // 2, 10)

	# Checar colisiones - jugador - monedas
	if player_car.collide(moneda.mask, moneda.rect.centerx,moneda.rect.centery) != None:
		moneda.kill()
		player_car.score += 50
		moneda = Moneda()
		all_sprites.add(moneda)
		mon_list.add(moneda)

	while not game_info.started:
		blit_text_center(WIN, MAIN_FONT, f"Press any key to start level {game_info.level}!")
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				break
			if event.type == pygame.KEYDOWN:
				game_info.start_level()

	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Run = False
			break

		#if event.type == pygame.MOUSEBUTTONDOWN:
			#pos = pygame.mouse.get_pos()
			#computer_car.path.append(pos)

	move_player(player_car)
	#computer_car.move()

	handle_collision(player_car, game_info)

	if game_info.game_finished():
		pass
		#blit_text_center(WIN,MAIN_FONT,"You Won!")
		#pygame.display.update()
		#pygame.time.wait(5000)
		#game_info.reset()
		#player_car.reset()
		
	
#print(computer_car.path)
pygame.quit()

