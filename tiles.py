import random
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Random Room")

tile1Img = pygame.image.load('Tile1.png')
tile2Img = pygame.image.load('Tile2.png')
tile3Img = pygame.image.load('Tile3.png')
tile4Img = pygame.image.load('Tile4.png')
tile5Img = pygame.image.load('Tile5.png')
tile6Img = pygame.image.load('Tile6.png')
tile7Img = pygame.image.load('Tile7.png')
tile8Img = pygame.image.load('Tile8.png')
tile9Img = pygame.image.load('Tile9.png')
tile10Img = pygame.image.load('Tile10.png')
tile11Img = pygame.image.load('Tile11.png')
tile12Img = pygame.image.load('Tile12.png')
tile13Img = pygame.image.load('Tile13.png')
tile14Img = pygame.image.load('Tile14.png')
tile15Img = pygame.image.load('Tile15.png')
tile16Img = pygame.image.load('Tile16.png')

def draw_tile1(x, y):
    screen.blit(tile1Img, (x, y))


class TilePreset:
    def __init__(self, north_wall, east_wall, south_wall, west_wall, number, image):
        self.north_wall = north_wall
        self.east_wall = east_wall
        self.south_wall = south_wall
        self.west_wall = west_wall
        self.tile_number = number
        self.image = image


Tile1 = TilePreset(True, False, False, False, "╦", tile1Img)  # Single Wall Tiles    [N, E, S, W]
Tile2 = TilePreset(False, True, False, False, "╣", tile2Img)
Tile3 = TilePreset(False, False, True, False, "╩", tile3Img)
Tile4 = TilePreset(False, False, False, True, "╠", tile4Img)
Tile5 = TilePreset(True, True, False, False, "╗", tile5Img)  # Corner Wall Tiles    [N, E, S, W]
Tile6 = TilePreset(False, True, True, False, "╝", tile6Img)
Tile7 = TilePreset(False, False, True, True, "╚", tile7Img)
Tile8 = TilePreset(True, False, False, True, "╔", tile8Img)
Tile9 = TilePreset(True, True, True, False, "╸", tile9Img)  # U Wall Tiles    [N, E, S, W]
Tile10 = TilePreset(False, True, True, True, "╹", tile10Img)
Tile11 = TilePreset(True, False, True, True, "╺", tile11Img)
Tile12 = TilePreset(True, True, False, True, "╻", tile12Img)
Tile13 = TilePreset(True, False, True, False, "═", tile13Img)  # Parallel Wall Tiles    [N, E, S, W]
Tile14 = TilePreset(False, True, False, True, "║", tile14Img)
Tile15 = TilePreset(False, False, False, False, "╬", tile15Img)  # All Wall Tiles    [N, E, S, W]
Tile16 = TilePreset(True, True, True, True, " ", tile16Img)  # No Wall Tiles    [N, E, S, W]


tile_dict = {}


tile_dict[(True, False, False, False)] = Tile1
tile_dict[(False, True, False, False)] = Tile2
tile_dict[(False, False, True, False)] = Tile3
tile_dict[(False, False, False, True)] = Tile4
tile_dict[(True, True, False, False)] = Tile5
tile_dict[(False, True, True, False)] = Tile6
tile_dict[(False, False, True, True)] = Tile7
tile_dict[(True, False, False, True)] = Tile8
tile_dict[(True, True, True, False)] = Tile9
tile_dict[(False, True, True, True)] = Tile10
tile_dict[(True, False, True, True)] = Tile11
tile_dict[(True, True, False, True)] = Tile12
tile_dict[(True, False, True, False)] = Tile13
tile_dict[(False, True, False, True)] = Tile14
tile_dict[(False, False, False, False)] = Tile15
tile_dict[(True, True, True, True)] = Tile16


class Room:
    def __init__(self, x_max, y_max, seed):
        self.x_max = x_max
        self.y_max = y_max
        self.seed = seed
        self.d = {}
        self.generate()

    def generate(self):
        for width in range(self.x_max):
            for height in range(self.y_max):
                temp_tile = [None, None, None, None]  # [N, E, S, W]
                if width == 0:
                    temp_tile[3] = True
                if width == (self.x_max - 1):
                    temp_tile[1] = True
                if height == 0:
                    temp_tile[0] = True
                if height == (self.y_max - 1):
                    temp_tile[2] = True
                if width > 0:
                    temp_tile[3] = self.d[((width - 1), height)].east_wall
                if height > 0:
                    temp_tile[0] = self.d[(width, (height - 1))].south_wall
                for temp_tile_range in range(4):
                    if temp_tile[temp_tile_range] is None:
                        temp_tile[temp_tile_range] = random.choice([True, False])

                self.d[(width, height)] = tile_dict[(temp_tile[0], temp_tile[1], temp_tile[2], temp_tile[3])]

    def draw(self):
        for j in range(self.y_max):
            for i in range(self.x_max):
                # print(self.d[(i, j)].tile_number, end="  ")
                screen.blit(self.d[(i, j)].image, ((i*50), (j*50)))
            print()


myRoom = Room(10, 10, 0)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            myRoom.generate()
            myRoom.draw()

    pygame.display.update()


# [x, y, tile]
# 0, 3, 14
# 01  07  03  15
# 16  04  04  02
# 07  05  04  03
# 16  04  04  02

# ╚ ╔ ╩ ╦ ╠ ═ ╬╣ ║ ╗ ╝
