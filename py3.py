import pygame, random, math

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, speed)
        self.original_image = pygame.image.load(player_image)
        self.angle = random.uniform(0, 360)
        self.start_size = (size_x, size_y)
        self.count = 0
    def update(self):
        x = math.cos(math.radians(self.angle)) * self.speed
        y = math.sin(math.radians(self.angle)) * self.speed
        self.rect.x += x
        self.rect.y += y
        if self.count >= 20:
            self.rect.width += 1
            self.rect.height += 1
            self.image = pygame.transform.scale(self.original_image, (self.rect.width, self.rect.height))
            self.count = 0
        self.count += 1
        if self.rect.left < 0 or self.rect.right > window_width or self.rect.top < 0 or self.rect.bottom > window_height:
            self.rect.width, self.rect.height = self.start_size
            self.image = pygame.transform.scale(self.original_image, (self.rect.width, self.rect.height))
            # Респавн на периметре окружности
            x, y, angle = get_spawn_position()
            self.rect.x = x
            self.rect.y = y
            self.angle = angle

pygame.init()

window_width = 700
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Сквозь вселенную')

background = pygame.transform.scale(pygame.image.load('C:/Users/solda/OneDrive/Документы/Python/Bcelennay/black.png'), (window_width, window_height))

# Параметры окружности для появления врагов
center_x = window_width // 2
center_y = window_height // 2
spawn_radius = 5  # Радиус окружности для появления врагов

def get_spawn_position():
    """Возвращает случайную позицию на периметре окружности"""
    angle = random.uniform(0, 360)
    x = center_x + spawn_radius * math.cos(math.radians(angle))
    y = center_y + spawn_radius * math.sin(math.radians(angle))
    return x, y, angle

enemy_size = 2
enemy_speed = 4
enemies = pygame.sprite.Group()

for i in range(33):
    x, y, angle = get_spawn_position()
    enemy = Enemy('C:/Users/solda/OneDrive/Документы/Python/Bcelennay/belo.jpg', x, y, enemy_size, enemy_size, enemy_speed)
    enemy.angle = angle
    enemies.add(enemy)
for i in range(33):
    x, y, angle = get_spawn_position()
    enemy = Enemy('C:/Users/solda/OneDrive/Документы/Python/Bcelennay/Purple.jpg', x, y, enemy_size, enemy_size, enemy_speed)
    enemy.angle = angle
    enemies.add(enemy)
for i in range(33):
    x, y, angle = get_spawn_position()
    enemy = Enemy('C:/Users/solda/OneDrive/Документы/Python/Bcelennay/PurpleBlack.jpg', x, y, enemy_size, enemy_size, enemy_speed)
    enemy.angle = angle
    enemies.add(enemy)

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(background, (0, 0))

    enemies.update()
    enemies.draw(window)

    pygame.display.update()

    clock.tick(60)

pygame.quit()