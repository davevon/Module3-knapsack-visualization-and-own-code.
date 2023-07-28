#install - "pip3 install pygame"

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Toll booth configuration
NUM_BOOTH = 3
BOOTH_CAPACITY = 15

# Initialize Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Toll Booth Knapsack Simulation")

class Vehicle:
    def __init__(self, x, y, color, toll, weight):
        self.x = x
        self.y = y
        self.color = color
        self.toll = toll
        self.weight = weight
        self.passed_booth = False

    def move(self):
        self.y -= 2  # Adjust the speed of vehicles

def draw_toll_booths():
    for i in range(NUM_BOOTH):
        pygame.draw.rect(screen, WHITE, (100 + i * 250, 200, 100, 150))
        font = pygame.font.Font(None, 24)
        booth_label = font.render(f"Toll Booth {i+1}", True, BLACK)
        screen.blit(booth_label, (120 + i * 250, 230))

def knapsack_algorithm(vehicles, capacity):
    n = len(vehicles)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if vehicles[i - 1].weight <= w:
                dp[i][w] = max(vehicles[i - 1].toll + dp[i - 1][w - vehicles[i - 1].weight], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_vehicles = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_vehicles.append(vehicles[i - 1])
            w -= vehicles[i - 1].weight
        i -= 1

    return selected_vehicles

def main():
    vehicles = []

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Create new vehicles randomly
        if random.randint(1, 50) == 1:
            x = random.randint(110, 350) + random.choice([0, 250, 500])
            y = SCREEN_HEIGHT
            color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            toll = random.randint(1, 10)  # Random toll amount for each vehicle
            weight = random.randint(1, 20)  # Random weight for each vehicle
            vehicles.append(Vehicle(x, y, color, toll, weight))

        # Clear the screen
        screen.fill(BLACK)

        # Draw the toll booths
        draw_toll_booths()

        # Update and draw vehicles
        for vehicle in vehicles:
            vehicle.move()
            pygame.draw.rect(screen, vehicle.color, (vehicle.x, vehicle.y, 80, 40))

        # Check if vehicles reach the toll booth
        for vehicle in vehicles:
            if 200 <= vehicle.y <= 350 and not vehicle.passed_booth:
                if vehicle.weight <= BOOTH_CAPACITY:
                    vehicle.passed_booth = True
                else:
                    font = pygame.font.Font(None, 44)
                    error_label = font.render("exceed weight: Vehicle takes another path ", True, RED)
                    screen.blit(error_label, (120 + (vehicle.x % 250), 200))

        # Remove passed vehicles from the list
        vehicles = [v for v in vehicles if v.y > 0]

        # Optimize toll collection with the knapsack algorithm for each booth
        for i in range(NUM_BOOTH):
            booth_vehicles = [v for v in vehicles if 100 + i * 250 <= v.x <= 200 + i * 250]
            selected_vehicles = knapsack_algorithm(booth_vehicles, BOOTH_CAPACITY)

            # Draw the selected vehicles at each toll booth
            for j, vehicle in enumerate(selected_vehicles):
                pygame.draw.rect(screen, vehicle.color, (120 + i * 250, 250 + j * 50, 80, 40))
                font = pygame.font.Font(None, 20)
                toll_label = font.render(f"Toll: {vehicle.toll}", True, BLACK)
                weight_label = font.render(f"Weight: {vehicle.weight}", True, BLACK)
                screen.blit(toll_label, (130 + i * 250, 270 + j * 50))
                screen.blit(weight_label, (130 + i * 250, 290 + j * 50))

        # Update the display
        pygame.display.update()

if __name__ == "__main__":
    main()
