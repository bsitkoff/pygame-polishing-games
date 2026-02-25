import pgzrun
import random

WIDTH = 800
HEIGHT = 600

state = "start"
score = 0

player = Actor('happy')
alien = Actor('alien')
cookie = Actor('cookie')

def reset_game():
    global score
    score = 0
    player.pos = (WIDTH // 2, HEIGHT // 2)
    alien.pos = (100, 100)
    cookie.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

def update():
    global state, score

    if state != "playing":
        return

    if keyboard.left:
        player.x -= 4
    if keyboard.right:
        player.x += 4
    if keyboard.up:
        player.y -= 4
    if keyboard.down:
        player.y += 4

    player.x = max(0, min(WIDTH, player.x))
    player.y = max(0, min(HEIGHT, player.y))

    if alien.x < player.x:
        alien.x += 1
    elif alien.x > player.x:
        alien.x -= 1
    if alien.y < player.y:
        alien.y += 1
    elif alien.y > player.y:
        alien.y -= 1

    if player.colliderect(cookie):
        score += 1
        cookie.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

    if player.colliderect(alien):
        state = "game_over"

def draw():
    screen.fill((0, 0, 0))

    if state == "start":
        # TODO: design a better start screen
        screen.draw.text("Press SPACE to start", center=(WIDTH // 2, HEIGHT // 2), fontsize=30, color="white")

    elif state == "playing":
        player.draw()
        alien.draw()
        cookie.draw()
        # TODO: improve score display (position, size, color, font)
        screen.draw.text(f"Score: {score}", (10, 10), fontsize=24, color="white")

    elif state == "game_over":
        # TODO: design a better game over screen
        screen.draw.text("Game Over", center=(WIDTH // 2, HEIGHT // 2), fontsize=40, color="red")
        screen.draw.text("Press R to restart", center=(WIDTH // 2, HEIGHT // 2 + 60), fontsize=24, color="yellow")

def on_key_down(key):
    global state
    if state == "start" and key == keys.SPACE:
        reset_game()
        state = "playing"
    elif state == "game_over" and key == keys.R:
        state = "start"

pgzrun.go()
