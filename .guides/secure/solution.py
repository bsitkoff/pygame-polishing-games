import pgzrun
import random

WIDTH = 400
HEIGHT = 600

state = "start"
score = 0

GRAVITY = 0.5
FLAP = -6
GAP = 140
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

    if state == "start" and keyboard.space:
        reset_game()
        state = "playing"
        return

    if state == "game_over" and keyboard.r:
        state = "start"
        return

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
    screen.fill((70, 180, 220))

    if state == "start":
        screen.draw.text("Flappy!", center=(WIDTH // 2, HEIGHT // 3), fontsize=60, color="white")
        screen.draw.text("Tap SPACE to flap. Don't hit the pipes.", center=(WIDTH // 2, HEIGHT // 2), fontsize=18, color=(255, 255, 255))
        screen.draw.text("Press SPACE to start", center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=22, color="yellow")

    elif state == "playing":
        pipe_top.draw()
        pipe_bottom.draw()
        bird.draw()
        screen.draw.text(str(score), center=(WIDTH // 2, 40), fontsize=50, color="white")

    elif state == "game_over":
        screen.draw.text("Game Over!", center=(WIDTH // 2, HEIGHT // 3), fontsize=50, color="white")
        screen.draw.text(f"Score: {score}", center=(WIDTH // 2, HEIGHT // 2), fontsize=36, color="yellow")
        screen.draw.text("Press R to try again", center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=22, color="white")


pgzrun.go()
