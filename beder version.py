import random
import time
import os

def random_line():
    types_of_snowflakes=[".", "+", "*"]
    snowflakes_per_line= random.randint(0, 7)
    length_line= 150

    line=[]

    for _ in range(snowflakes_per_line):
        i= random.randint(0, len(types_of_snowflakes) - 1)
        line.append(types_of_snowflakes[i])

    for _ in range(length_line - snowflakes_per_line):
        line.append(" ")

    random.shuffle(line)

    return line

def graphic_handler(lines):
    os.system("clear")

    for line in lines:
        string= " "

        for char in line:
            string += char

    time.sleep(0.5)

random.seed("snowfall")

lines= []
numbers_of_lines=15
for i in range(numbers_of_lines):
    lines.append(random_line())

while True:
    lines.pop(0)
    lines.append(random_line())

    graphic_handler(lines)
