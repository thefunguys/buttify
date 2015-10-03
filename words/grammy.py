#!/usr/bin/python
import random
import click
import sys
import time
import random

cache = {}
text = ""
num_chars = 3

def read_file(filename):
    global text
    f = open(filename, 'r')
    text = f.read()
    f.close()
    parse_text()

def cache_grab(chars):
    if len(chars) < 2:
        return ' '
    try:
        return random.choice(cache[tuple(c for c in chars)])
    except:
        return cache_grab(chars[1:])

def parse_text():
    global num_chars
    for i, c in enumerate(text):
        if i > 2:
            for j in range(2, num_chars + 2):
                key = tuple(text[i - j + k] for k in range(1, j))
                if key in cache:
                    cache[key].append(c)
                else:
                    cache[key] = [c]

def gen(size=100):
    gen = []
    gen_text_for_chars(setup_seed(), gen, size)
    print ''.join(gen)

def slow_gen():
    chars = setup_seed()
    while True:
        gen = []
        chars = gen_text_for_chars(chars, gen,  1)
        sys.stdout.write(''.join(gen))
        sys.stdout.flush()
        time.sleep(random.random() * 0.2 + 0.1)

def setup_seed():
    seed = 0
    chars = [text[s] for s in range(seed, seed + num_chars)]
    return chars

def gen_text_for_chars(chars, gen_, times):
    for i in range(times):
        gen_.append(chars[0])
        c = cache_grab(chars)
        chars.append(c)
        chars = chars[1:]
    return chars

@click.command()
@click.argument('filename')
@click.option('--depth', default=3)
@click.option('--continuous/--at-once', default=False)
@click.option('--length', default=200)
def main(filename, depth, continuous, length):
    global num_chars
    num_chars = int(depth)
    read_file(filename)
    if continuous:
        slow_gen()
    else:
        gen(length)
    


if __name__=="__main__":
    main()
