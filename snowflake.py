import random
import pygame as pg

# --CONSTANTS--
# COLOURS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280 # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)


class Snowflake(pg.sprite.Sprite):
    def __init__(self, size: int):
        """
        Params:
            size: diameter of snowflake
        """
        # Super class constructor
        super().__init__()

        # Create a blank surface
        self.image = pg.Surface((size, size))

        #Draw a circle inside of it
        pg.draw.circle(self.image, WHITE, (size // 2, size // 2), size // 2)

        self.rect = self.image.get_rect()

        self.vel_x = 5
        self.vel_y = 5

        # Spawn it in the middle of the screem
        # Chooses a ramdom x-coordinate
        self.rect.centerx = random.randrange(0, WIDTH +1)

    def update(self):
        self.rect.y += self.vel_y


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variable--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock= pg.time.Clock()
    
    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Add 100 snowflakes to the all_sprites Group
    for _ in range(10):
        all_sprites.add(Snowflake(10))

    pg.display.set_caption("Snowfall Landscape")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        for _ in range(3):
            all_sprites.add(Snowflake(random.randrange(4,12)))

        # --- Update the world state
        # Updatethe state of all sprites
        all_sprites.update()

        # ---Draw items
        screen.fill(BLACK)

        # Draw all the sprites
        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock 
        clock.tick(60) # 60 fps

def main():
    start()

if __name__ == "__main__":
    main()
    
    
        
    


