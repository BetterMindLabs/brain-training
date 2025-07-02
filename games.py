import random
import time

def memory_game():
    sequence = [random.randint(1, 9) for _ in range(5)]
    return sequence

def reaction_game():
    start = time.time()
    input("Press Enter as fast as you can after seeing this message!")
    end = time.time()
    return round(end - start, 3)
