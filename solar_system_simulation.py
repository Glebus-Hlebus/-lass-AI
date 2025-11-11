import pygame
import math
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Солнечная система")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)
ORANGE = (255, 165, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)
BROWN = (165, 42, 42)

# Создание случайных "звёзд" в космосе
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(200)]

# Настройка планет: (имя, цвет, радиус орбиты, скорость вращения, размер планеты)
planets = [
    ("Меркурий", GRAY, 50, 0.04, 5),
    ("Венера", ORANGE, 80, 0.035, 8),
    ("Земля", BLUE, 110, 0.03, 10),
    ("Марс", RED, 140, 0.025, 9),
    ("Юпитер", ORANGE, 180, 0.02, 20),
    ("Сатурн", BROWN, 230, 0.018, 17),
    ("Уран", LIGHT_BLUE, 280, 0.015, 14),
    ("Нептун", DARK_BLUE, 330, 0.012, 14)
]

# Угол вращения каждой планеты
angles = [random.uniform(0, 2*math.pi) for _ in planets]

# Центр Солнца
sun_x, sun_y = WIDTH // 2, HEIGHT // 2

# Основной цикл игры
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Рисуем звёзды
    for star in stars:
        pygame.draw.circle(screen, WHITE, star, 2)

    # Рисуем Солнце
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), 30)

    # Рисуем и обновляем планеты
    for i, planet in enumerate(planets):
        name, color, orbit_radius, speed, size = planet
        angles[i] += speed
        planet_x = sun_x + orbit_radius * math.cos(angles[i])
        planet_y = sun_y + orbit_radius * math.sin(angles[i])
        pygame.draw.circle(screen, color, (int(planet_x), int(planet_y)), size)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

# Закрываем Pygame корректно
pygame.quit()
