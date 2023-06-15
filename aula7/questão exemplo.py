import time

for minutos in range(9, -1, -1):
    for segundos in range(59, -1, -1):
        print(f"{minutos:02d}:{segundos:02d}")
        time.sleep(1)
