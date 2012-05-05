#! /usr/bin/env python

# Copyright (C) <2012> Addy Singh <addy689@gmail.com>


# Welcome to THE REAL HANGMAN

# Hang Man is a simple, yet fun to play game. It automatically selects a random word from a list of words that numbers over 200,000! This means that you will almost never get the same word.

# The objective of the game is as follows:-

# You will be given a secret word. Unlock the secret word by guessing one character at a time, but keep in mind that you have only 10 attempts for this, after which the hangman will hang his victim!

# ENJOY!

import sys
from os import system
from urllib import *

urlretrieve('http://andromeda.nitc.ac.in/~addy/Hangman_src.py','Hangman_src.py')
from Hangman_src import *

if __name__ == '__main__':
	wordfile = getlist(getvalue()) + 'load'
	t = randomizeLists(wordfile)
	if len(sys.argv) > 1:
		s = t[0] + sys.argv[1]
	else:
		s = t[0] + 'movies'
	system(s)
