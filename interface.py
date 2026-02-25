import pgzrun
import random

# This game works — but the visual design has some problems.
# Can you spot them? Can you fix them?

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
    cookie.pos = (300, 300)


def update():
    global state, score

    if state != "playing":
        return

    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y > HEIGHT:
        player.y = 0
    if player.y < 0:
        player.y = HEIGHT

    if player.x > alien.x:
        alien.x += 1
    elif player.x < alien.x:
        alien.x -= 1
    if player.y > alien.y:
        alien.y += 1
    elif player.y < alien.y:
        alien.y -= 1

    if player.colliderect(cookie):
        score += 1
        cookie.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

    if player.colliderect(alien):
        state = "game_over"


def draw():
    screen.fill((0, 0, 0))

    if state == "start":
        # BUG 1: Is this start screen helpful? Does a new player know what to do?
        screen.draw.text("SPACE", center=(WIDTH // 2, HEIGHT // 2), fontsize=20, color="gray")

    elif state == "playing":
        player.draw()
        alien.draw()
        cookie.draw()
        # BUG 2: Can you read this score?
        screen.draw.text(f"{score}", (790, 590), fontsize=10, color="darkgray")

    elif state == "game_over":
        # BUG 3: Does the player know what happened or what to do next?
        screen.draw.text("OVER", center=(WIDTH // 2, HEIGHT // 2), fontsize=15, color="darkred")


def on_key_down(key):
    global state

    if state == "start" and key == keys.SPACE:
        reset_game()
        state = "playing"

    elif state == "game_over" and key == keys.R:
        state = "start"


pgzrun.go()
