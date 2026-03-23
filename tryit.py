import pgzrun
import random

WIDTH = 400
HEIGHT = 600

state = "start"
score = 0

GRAVITY = 0.3
FLAP = -6.5
GAP = 130
SPEED = 3

bird = Actor('bird1', (75, 300))
bird.vy = 0

pipe_top = Actor('top', anchor=('left', 'bottom'))
pipe_bottom = Actor('bottom', anchor=('left', 'top'))


def reset_pipes():
    gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, gap_y + GAP // 2)


def reset_game():
    global score
    score = 0
    bird.pos = (75, 300)
    bird.vy = 0
    reset_pipes()


def update():
    global state, score

    if state != "playing":
        return

    if keyboard.space:
        bird.vy = FLAP

    bird.vy += GRAVITY
    bird.y += bird.vy

    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED

    if pipe_top.right < 0:
        reset_pipes()
        score += 1

    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        state = "game_over"

    if bird.y > HEIGHT or bird.y < 0:
        state = "game_over"


def draw():
    screen.fill((0, 0, 0))

    if state == "start":
        screen.draw.text("Press SPACE", center=(WIDTH // 2, HEIGHT // 2), fontsize=20, color="white")

    elif state == "playing":
        pipe_top.draw()
        pipe_bottom.draw()
        bird.draw()
        screen.draw.text(str(score), (370, 570), fontsize=14, color="white")

    elif state == "game_over":
        screen.draw.text("Game Over", center=(WIDTH // 2, HEIGHT // 2), fontsize=30, color="white")


def on_key_down(key):
    global state

    if state == "start" and key == keys.SPACE:
        reset_game()
        state = "playing"

    elif state == "game_over" and key == keys.R:
        state = "start"


pgzrun.go()
