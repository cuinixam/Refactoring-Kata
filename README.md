# Gilded Rose Refactoring Kata
## How to use this Kata

The simplest way is to just clone the code and start hacking away, improving the design. You'll want to look at the ["Gilded Rose Requirements"](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/master/GildedRoseRequirements.txt) which explains what the code is for. I strongly advise you that you'll also need some tests if you want to make sure you don't break the code while you refactor.

Preconditions:

* clone repo
* run `python -m pipenv install`
* run failing test-case (maybe you need to setup pytest in VSCode first)

You could write some unit tests yourself, using the requirements to identify suitable test cases. I've provided a failing unit test as a starting point.

The idea of the exercise is to do some deliberate practice, and improve your skills at designing test cases and refactoring. The idea is not to re-write the code from scratch, but rather to practice designing tests, taking small steps, running the tests often, and incrementally improving the design. 

### Gilded Rose Requirements in other languages 

- [English](GildedRoseRequirements.md)
- [German](GildedRoseRequirements_de.md)

## Better Code Hub

I analysed this repo according to the clean code standards on [Better Code Hub](https://bettercodehub.com) just to get an independent opinion of how good/bad the code is. Actually the initial score is already higher than expected. It was supposed to be 5/10, but the python version of the code has already a better basis.

[![BCH compliance](https://bettercodehub.com/edge/badge/besessener/Refactoring-Kata?branch=main)](https://bettercodehub.com/) 

Your task is to improve it!

## Pylama

There is a pylama batch file included in this repo called: `check-code-quality.bat`. If your pipenv is configured correctly, you can simply execute it and it will give you static analysis results as well. 

## Task

Make sure that there are no remaining issues until the end of the session in both `Better Code Hub` and `pylama`!
