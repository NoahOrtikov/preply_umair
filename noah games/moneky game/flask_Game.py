from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import pygame
import random
import threading

app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('input_event')
def handle_input_event(data):
    # Process input data and update game state
    emit('update_event', {'message': 'Game state updated'})

def run_flask():
    socketio.run(app, host='0.0.0.0', port=5000)

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Monkey Game")

# Load images
background = pygame.image.load("bg.webp")
background = pygame.transform.scale(background, (width, height))
monkey = pygame.image.load("game_monkey.png")
monkey = pygame.transform.scale(monkey, (200, 200))
barrel = pygame.image.load("Barrel.jpg")
barrel = pygame.transform.scale(barrel, (100, 100))

# Initial position of the monkey
monkey_x, monkey_y = 100, 400
jumping = False

jump_speed = 11.5
gravity = 0.25
monkey_y_speed = 1

# Barrel settings
barrel_speed = 5
barrel_frequency = 1500  # milliseconds
barrels = []

# Score
score = 0
font = pygame.font.Font(None, 36)

# Set up the clock for frame rate
clock = pygame.time.Clock()
FPS = 60

# Timer for generating barrels
pygame.time.set_timer(pygame.USEREVENT, barrel_frequency)

# Run the Flask app in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping and not game_over:
                jumping = True
                monkey_y_speed = -jump_speed
        if event.type == pygame.USEREVENT and not game_over:
            barrel_x = width
            barrel_y = 500  # assuming ground level is at y = 500
            barrels.append(pygame.Rect(barrel_x, barrel_y, 100, 100))

    if not game_over:
        # Handle game logic here
        if jumping:
            monkey_y_speed += gravity
            monkey_y += monkey_y_speed
            if monkey_y >= 400:  # assuming ground level is at y = 400
                monkey_y = 400
                jumping = False
                monkey_y_speed = 0

        # Move barrels
        for barrel_rect in barrels:
            barrel_rect.x -= barrel_speed
            if barrel_rect.right < 0:
                barrels.remove(barrel_rect)
                score += 1  # Increase score when the barrel goes off screen

        # Check for collisions
        monkey_rect = pygame.Rect(monkey_x, monkey_y, 200, 200)
        for barrel_rect in barrels:
            if monkey_rect.colliderect(barrel_rect):
                game_over = True

    # Update the display
    window.blit(background, (0, 0))
    window.blit(monkey, (monkey_x, monkey_y))
    for barrel_rect in barrels:
        window.blit(barrel, barrel_rect)

    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        window.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

    pygame.display.update()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
