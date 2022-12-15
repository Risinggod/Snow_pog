import random
import os
import time
import shutil
colum,line=shutil.get_terminal_size()




floke= ["*"," ", "+"] * colum
random.shuffle(floke)


for x in range(line):
    print(floke)
    time.sleep(0.5)





























