import pygame
import sys
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knapsack Algorithm - Portmore Toll Road and Mandela Road")

# Toll stations: (value, weight)
america_toll_road = [
      (2, 2),
    (1, 1),
    (10, 4),
    (2, 1),
    (4, 12),
]

mandela_road = [
       (2, 2),
    (1, 1),
    (10, 4),
    (2, 1),
    (4, 12),
]

max_capacity = 15

def knapsack(toll_road, max_capacity):
    n = len(toll_road)
    dp = [[0] * (max_capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_capacity + 1):
            value, weight = toll_road[i - 1]
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_tolls = []
    w = max_capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_tolls.append(toll_road[i - 1])
            w -= toll_road[i - 1][1]

    return selected_tolls
def load_car_images():
    car_images = []
    for i in range(1, 6):
        image_path = os.path.join(os.path.dirname(__file__), f"car{1}.png")
        image_path = os.path.join(os.path.dirname(__file__), f"car{2}.png")
        car_image = pygame.image.load(image_path).convert_alpha()
        car_images.append(pygame.transform.scale(car_image, (50, 50)))
    return car_images

def draw_toll_road(toll_road, road_name, x_offset, car_images):
    for i, (value, weight) in enumerate(toll_road):
        x = 40 + x_offset + i * 120
        y = 400 - weight * 30
        window.blit(car_images[i], (x, y))
        font = pygame.font.Font(None, 24)
        text = font.render(f"{road_name}", True, (0, 0, 0))
        window.blit(text, (x + 10, y + 60))

def draw_selected_tolls(selected_tolls, x_offset, car_images):
    for i, (value, weight) in enumerate(selected_tolls):
        x = 40 + x_offset + i * 120
        y = 400 - weight * 30
        window.blit(car_images[i], (x, y))
        pygame.draw.rect(window, (255, 255, 0), (x, y, 50, 50), 2)

def draw_summary(selected_tolls, x_offset):
    total_weight = sum(toll[1] for toll in selected_tolls)
    total_value = sum(toll[0] for toll in selected_tolls)

    font = pygame.font.Font(None, 30)
    text = font.render(f"Total Weight: {total_weight}", True, (0, 0, 0))
    window.blit(text, (45 + x_offset, 500))
    text = font.render(f"Total Value: {total_value}", True, (0, 0, 0))
    window.blit(text, (45 + x_offset, 540))

def main():
    car_images = load_car_images()
    selected_tolls_america = []
    selected_tolls_mandela = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not selected_tolls_america:
            selected_tolls_america = knapsack(america_toll_road, max_capacity)
        
        if not selected_tolls_mandela:
            selected_tolls_mandela = knapsack(mandela_road, max_capacity)

        window.fill((25, 255, 255))
        draw_toll_road(america_toll_road, "America's Toll Road", 0, car_images)
        draw_toll_road(mandela_road, "Mandela Road", 400, car_images)

        if selected_tolls_america:
            draw_selected_tolls(selected_tolls_america, 0, car_images)
            draw_summary(selected_tolls_america, 0)
            selected_tolls_america = selected_tolls_america[:-1]  # Remove the last toll for animation effect
        
        if selected_tolls_mandela:
            draw_selected_tolls(selected_tolls_mandela, 400, car_images)
            draw_summary(selected_tolls_mandela, 400)
            selected_tolls_mandela = selected_tolls_mandela[:-1]  # Remove the last toll for animation effect

        pygame.display.flip()
        pygame.time.delay(500)  # Add a delay to slow down the animation

if __name__ == "__main__":
    main()
