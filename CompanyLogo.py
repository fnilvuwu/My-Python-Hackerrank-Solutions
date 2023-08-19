#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    logo = {}

    for i in s:
        if i in logo:
            logo[i] = logo[i] + 1
        else:
            logo[i] = 1

    logo_count = [logo[key] for key in logo]

    logo_sorted = dict(sorted(logo.items()))
    logo_sorted = dict(
        sorted(logo_sorted.items(), key=lambda item: item[1], reverse=True)[:3])

    for key in logo_sorted:
        print(key + " " + str(logo_sorted[key]))
