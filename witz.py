#generiert einen zufälligen Witz

from urllib.request import *
import json, random

a = urlopen("https://raw.githubusercontent.com/Cows-vs-Ducks/game/main/ww.json").read().decode()
witze = json.loads(a)
i = 0
for witz1 in witze:
    i += 1
    
witz = witze[str(random.randint(1, i))]
print(witz)
