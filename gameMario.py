import pgzrun

# Define the screen dimensions
WIDTH = 800
HEIGHT = 600

# Define a player character
player = Actor("player")
player.pos = (WIDTH / 2, HEIGHT / 2)

# Define an enemy character
enemy = Actor("enemy")
enemy.pos = (100, 100)

# Define game variables
score = 0

# Define the update function
def update():
    global score

    # Move the enemy towards the player
    if player.x < enemy.x:
        enemy.x -= 2
    else:
        enemy.x += 2

    if player.y < enemy.y:
        enemy.y -= 2
    else:
        enemy.y += 2

    # Check for collision with the player and update the score
    if player.colliderect(enemy):
        score -= 1
        enemy.pos = (100, 100)

# Define the draw function
def draw():
    # Clear the screen
    screen.clear()

    # Draw the player and enemy characters
    player.draw()
    enemy.draw()

    # Draw the score on the screen
    screen.draw.text("Score: " + str(score), (10, 10), color="white", fontsize=40)

# Define keyboard input to move the player character
def on_key_down(key):
    if key == keys.LEFT:
        player.x -= 10
    elif key == keys.RIGHT:
        player.x += 10
    elif key == keys.UP:
        player.y -= 10
    elif key == keys.DOWN:
        player.y += 10

# Run the game
pgzrun.go()
