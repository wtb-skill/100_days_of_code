from cookie import game
import time


ratio = 0.5

while ratio < 1:
    game(ratio)
    time.sleep(30)
    ratio += 0.025
