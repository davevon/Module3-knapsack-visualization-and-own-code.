import pygame
import sys

pygame.init()

# Set up the window dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Knapsack Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Font
font = pygame.font.Font(None, 24)

class Knapsack(pygame.sprite.Sprite):
    def __init__(self, capacity):
        super().__init__()
        self.image = pygame.Surface((300, 200))
        self.image.fill(RED)  # Fill the box with red color (you can add an image here)
        self.rect = self.image.get_rect(center=(width // 2, height // 2))
        self.capacity = capacity
        self.items = []
        self.total_weight = 0
        self.total_value = 0

    def add_item(self, item):
        if self.total_weight + item.weight <= self.capacity:
            self.items.append(item)
            self.total_weight += item.weight
            self.total_value += item.value

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total_weight -= item.weight
            self.total_value -= item.value

class Item(pygame.sprite.Sprite):
    def __init__(self, name, weight, value, x, y):
        super().__init__()
        self.name = name
        self.weight = weight
        self.value = value
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)  # Fill item with white color (you can add an image here)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def main():
    # Create the knapsack with maximum weight capacity of 15
    knapsack = Knapsack(capacity=15)

    # Create the items
    items = [
        Item("Item 1", 2, 2, 100, 100),
        Item("Item 2", 1, 1, 175, 100),
        Item("Item 3", 4, 10, 250, 100),
        Item("Item 4", 1, 2, 125, 175),
        Item("Item 5", 12, 4, 200, 175),
    ]

    # Group for sprites
    all_sprites = pygame.sprite.Group()
    all_sprites.add(knapsack)
    all_sprites.add(items)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check for item clicks and add/remove them from the knapsack
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in items if s.rect.collidepoint(pos)]
                for item in clicked_sprites:
                    if item in knapsack.items:
                        knapsack.remove_item(item)
                    else:
                        knapsack.add_item(item)

        # Clear the screen
        screen.fill(BLACK)

        # Draw the knapsack and items on the screen
        all_sprites.draw(screen)

        # Display the items and their values and weights inside the knapsack box
        text_x, text_y = knapsack.rect.x + 10, knapsack.rect.y + 10
        for item in knapsack.items:
            text = font.render(f"{item.name} - Weight: {item.weight} - Value: {item.value}", True, WHITE)
            screen.blit(text, (text_x, text_y))
            text_y += 30

        # Display the total weight and value of the knapsack
        text = font.render(f"Knapsack Weight: {knapsack.total_weight}", True, WHITE)
        screen.blit(text, (knapsack.rect.x + 10, knapsack.rect.y + 150))

        text = font.render(f"Knapsack Value: {knapsack.total_value}", True, WHITE)
        screen.blit(text, (knapsack.rect.x + 10, knapsack.rect.y + 180))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
