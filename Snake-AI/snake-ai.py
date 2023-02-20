import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (in pixels)
WIDTH = 600
HEIGHT = 400

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the font for displaying the score
FONT = pygame.font.SysFont(None, 25)

# Set the title of the game
pygame.display.set_caption("Snake Game AI")

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the clock for controlling the speed of the game
clock = pygame.time.Clock()

# Set the initial direction of the snake
direction = "right"

# Define the size of each block in the grid (in pixels)
BLOCK_SIZE = 10

# Set the initial position of the snake
x = WIDTH / 2
y = HEIGHT / 2

# Set the initial speed of the snake
speed = 10

# Set the initial length of the snake
snake_list = []
snake_length = 1

# Define the function to display the score
def display_score(score):
    score_text = FONT.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [0, 0])

# Define the function to display the snake
def draw_snake(snake_list):
    for x,y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, BLOCK_SIZE, BLOCK_SIZE])

# Define the function to generate a random food location
def generate_food():
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
    return food_x, food_y

# Set the initial position of the food
food_x, food_y = generate_food()

# Define the function to detect collisions with the food
def detect_food_collision(x1, y1, x2, y2):
    if x1 >= x2 and x1 <= x2 + BLOCK_SIZE:
        if y1 >= y2 and y1 <= y2 + BLOCK_SIZE:
            return True
    return False

# Define the game loop
def game_loop():
    global direction, x, y, speed, snake_list, snake_length, food_x, food_y

    # Set the initial score
    score = 0

    # Set the initial game state
    game_over = False
    game_close = False

    # Start the game loop
    while not game_over:

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                elif event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"

        # Move the snake in the chosen direction
        if direction == "left":
            x -= speed
        elif direction == "right":
            x += speed
        elif direction == "up":
            y -= speed
        elif direction == "down":
            y += speed

        # Check for collisions with the walls
        if x >= WIDTH - BLOCK_SIZE or x < 0 or y >= HEIGHT - BLOCK_SIZE or y < 0:
            game_close = True

        # Check for collisions with the food
        if detect_food_collision(x, y, food_x, food_y):
            # Increase the score
            score += 1

            # Generate a new food location
            food_x, food_y = generate_food()

            # Increase the length of the snake
            snake_length += 1

        # Add the current position of the snake to the snake list
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        # Remove the oldest position of the snake if the length exceeds the snake_length
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collisions with the snake's body
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Fill the screen with black color
        screen.fill(BLACK)

        # Draw the food
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Draw the snake
        draw_snake(snake_list)

        # Display the score
        display_score(score)

        # Update the screen
        pygame.display.update()

        # Control the speed of the game
        clock.tick(20)

    # Quit Pygame
    pygame.quit()

    # Quit Python
    quit()

# Call the game loop function
game_loop()
