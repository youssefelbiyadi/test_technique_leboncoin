#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


def map_gen(x, y, density):
    print('{}.ox'.format(y))
    card = ""
    for i in range(int(y)):
        column = ""
        for j in range(int(x)):
            if (random.randint(0, int(y)) * 2) < int(density):
                column += "o"
            else:
                column += "."
        card += column + "\n"
    return card


if __name__ == '__main__':
    print(map_gen(50, 50, 3))
