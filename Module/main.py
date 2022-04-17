import hello
hello.say_hello('Junmo')
hello.say_hello2('Hyungmo')

import hello as h
h.say_hello('Junmo')

from hello import say_hello, say_hello2
say_hello('BOB')
say_hello2('ABCD')

from hello import *
say_hello3('')

import pygame

#import os
#os.getcwd()